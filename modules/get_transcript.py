from youtube_transcript_api import YouTubeTranscriptApi

try:
    import modules.constants
except Exception:
    import constants

""" Function will get the transcript of a video and write it down
    in "transcript.txt"

    Arguments:
        video_id --> String containing the ID for a YouTube video
    
    No return type
"""
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open("data/transcript.txt", "w") as file:
        for subtitle in transcript:
            file.write(subtitle.get("text") + "\n")
    

if __name__ == "__main__":
    get_transcript(constants.VIDEO_ID)