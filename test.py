from __future__ import unicode_literals
import youtube_dl

with youtube_dl.YoutubeDL() as downloader:
            meta = downloader.extract_info("https://www.youtube.com/watch?v=Ym1fmIkjJEM&ab_channel=MoatazMashal", download=False) 
            print(meta)
            file=open('meta.txt', 'a')
           