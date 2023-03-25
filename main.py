from pytube import YouTube
import os
import moviepy.editor as mp

def download_video_mp3(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_path=output_path, filename='temp.mp4')

    clip = mp.AudioFileClip(f"{output_path}/temp.mp4")
    clip.write_audiofile(f"{output_path}/{yt.title}.mp3")

    os.remove(f"{output_path}/temp.mp4")



yt_url = input("Digite a URL do audio que quer baixar: ")

download_video_mp3(yt_url, './downloads')
