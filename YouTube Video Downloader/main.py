from pytube import YouTube

url = "https://www.youtube.com/watch?v=1MBR39rTEs8"

video = YouTube(url)

print(video.title)

print(video.thumbnail_url)

print(video.views)

print(video.description)

video = video.streams.get_highest_resolution()

video.download()