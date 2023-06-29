# YouTube Video analyzing AI
This is a simple Python script for using OpenAI API on a transcript from a YouTube video.
Feel free to use this to ask questions about the video, ask for a quick summary, etc.

## :computer: How to use
- After you clone the project, install the required Python libraries:
  <br>`pip install -r requirements.txt`
- Then, open `modules/constants.py` and type your OpenAI API key and the ID of the video you wish to use.
- Run `python main.py` and start asking the questions.

## :books: Project Structure  
```
|-- README             <- Project README
|-- docs               <- Documentation
|-- modules            <- Helper functions
|-- data               <- Data that will be used to "train" the LLM (The transcript of the YouTube video)
```

## [:question: Find the ID of a YouTube video](https://help.tcgplayer.com/hc/en-us/articles/115008106868-Finding-Your-YouTube-Video-ID)
