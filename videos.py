from __future__ import unicode_literals
import youtube_dl
import PySimpleGUI as sg



def video_download_stream(url=[],type="mp4"):
    for url in url:
        with youtube_dl.YoutubeDL() as downloader:
            meta = downloader.download(url)
           
    



    





       