# app/services/summarization.py

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

prompt_template = """
Please provide a concise and informative summary in the language {language} of the content found at the following URL. The summary should be approximately 300 words and should highlight the main points, key arguments, and any significant conclusions or insights presented in the content. Ensure that the summary is clear and easy to understand for someone who has not accessed the original content.

URL Content:
{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text", "language"])

async def summarize_content(groq_api_key: str, url: str, language: str, language_codes: dict) -> str:
  model = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-70b-versatile")

  # Load the URL content
  if "youtube.com" in url:
      loader = YoutubeLoader.from_youtube_url(url, language=language_codes[language], add_video_info=True)
  else:
      loader = UnstructuredURLLoader(
          urls=[url], ssl_verify=False, headers={"User-Agent": "Mozilla/5.0"}
      )

  docs = loader.load()

  # Combine the documents
  text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
  texts = text_splitter.split_documents(docs)
  combined_text = " ".join([doc.page_content for doc in texts])

  # Create the chain
  chain = (
      {"text": RunnablePassthrough(), "language": lambda _: language}
      | prompt
      | model
      | StrOutputParser()
  )

  # Run the chain
  output = chain.invoke(combined_text)
  return output