from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from dotenv import load_dotenv
load_dotenv(".env")
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)
print("Name the people in the project team")
response = index.query("what is 2+2")
print(response)