from pytube import YouTube
from moviepy.editor import *
import os
from pydub import AudioSegment
import ffmpeg

mp4_file = r'./process/downloads/test.mp4'
mp3_file = r'./process/downloads/test.mp3'

def download_video():
    try:
        YouTube(url).streams.first().download("./process/downloads",filename="test")
        print("Download complete")

        print("Converting video to mp3")
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
        print("Convert complete")
        run_spleeter()

    except Exception as e:
        print("Unable to download from YouTube, please check that the URL is valid and try again.")


def run_spleeter():
    print("Running Spleeter")
    os.system("spleeter separate -i .\process\downloads\\test.mp3 -p spleeter:4stems -o output")
    print("Spleeter complete")
    combine_files()

def combine_files():
    print("Combining files")
    bass = AudioSegment.from_file("./output/test/bass.wav", format="wav")
    drums = AudioSegment.from_file("./output/test/drums.wav", format="wav")
    other = AudioSegment.from_file("./output/test/other.wav", format="wav")

    # Overlay drums over bass at position 0  (use louder instead of bass to use the louder version)
    combinedAudio = bass.overlay(drums, position=0).overlay(other, position = 0)

    print("Combining audio")
    # simple export
    file_handle = combinedAudio.export("./process/output/combined   /test/audio.mp3", format="mp3")

    print("Finish combining audio...")

    print("Merging video with audio...")

    os.system("ffmpeg -i ./process/downloads/test.mp4 -i ./process/output/combined/test/audio.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 ./process/output/final/output.mp4")

    print("Merging video with audio complete...")


# Get input from user
url = input("Please enter YouTube URL:")
download_video()
