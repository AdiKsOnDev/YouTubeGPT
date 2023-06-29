from youtube_transcript_api import YouTubeTranscriptApi

import modules.constants as constants

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open("data/transcript.txt", "w") as file:
        for subtitle in transcript:
            file.write(subtitle.get("text") + "\n")
    

if __name__ == "__main__":
    get_transcript(constants.VIDEO_ID)