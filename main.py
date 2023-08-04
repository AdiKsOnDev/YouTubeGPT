import os
import sys
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from pytube import extract

import modules.constants as constants
from modules.get_transcript import get_transcript

if constants.API_KEY == "":
    sys.exit("!ERROR, NO API KEY! \nPlease write your openAI API key in the 'modules/constants.py'")

URL = input("Please paste the URL of the video: ")
VIDEO_ID = extract.video_id(URL)

get_transcript(VIDEO_ID)

# Set the API key
os.environ["OPENAI_API_KEY"] = constants.API_KEY

# Use "transcript.txt" as the training data
loader = TextLoader('data/transcript.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

while True:
    print("------------------------------------")
    query = input("Ask me a question about the video or type 'Quit' to exit the program\n")
    print("------------------------------------")

    if query.lower() == "quit":
        break

    print(index.query(query, llm=ChatOpenAI()))