from pytube import YouTube

url = input("")    #Enter the url of the video you want to download

video = YouTube(url)

print(video.title)    #prints the title of the youtube video

print(video.thumbnail_url)    #prints the link of the youtube thumbnail image

print(video.views)    #prints the views of the video

print(video.description)    #prints the description of the video

video = video.streams.get_highest_resolution()

video.download()    #downloads the video in your current directory
