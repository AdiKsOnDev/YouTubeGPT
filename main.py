import os
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

import modules.constants as constants
from modules.get_transcript import get_transcript

get_transcript(constants.VIDEO_ID)

# Set the API key
os.environ["OPENAI_API_KEY"] = constants.API_KEY

# Use "transcript.txt" as the training data
loader = TextLoader('data/transcript.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

while True:
    print("------------------------------------")
    print("Ask me a question about the video =)")
    query = input("")
    print("------------------------------------")

    print(index.query(query, llm=ChatOpenAI()))