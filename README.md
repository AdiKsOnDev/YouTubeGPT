# :movie_camera: YouTube Video analyzing AI

This is a simple Python script for using OpenAI API on a transcript from a YouTube video.
Feel free to use this to ask questions about any video, ask for a quick summary, etc.

## :computer: How to use

- After you clone the project, install the required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```
- Then, open `modules/constants.py` and paste your OpenAI API key.
- Run `python main.py`, paste the URL of a video as an input and start asking questions.
- Write 'Quit' to stop the script

## :exclamation: Limitations

- You will not be able to ask questions about a video that has no transcript.
- Occasionally, script gives inaccurate responses.
- Sometimes script cannot answer very detailed queries, especially for a short video.

## :books: Project Structure  

```
|-- README             <- Project README
|-- docs               <- Documentation
|-- modules            <- Helper functions
|-- data               <- Data that will be used to "train" the LLM (The transcript of the YouTube video)
```
