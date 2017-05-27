from pytube import YouTube
from pprint import pprint
yt = YouTube('https://www.youtube.com/watch?v=GxvgWUrJT3I&t=16s')
print(yt.get_videos())
print(yt.filename)
# video = yt.get('mp4', '720p')
# video.download('d:\\downloads\\')

