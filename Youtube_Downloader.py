import os
from pytube import Playlist

# Convert string in alphanumeric format
def make_alpha_numeric(string):
    return ''.join(char for char in string if char.isalnum())

# Main function to download video tutorial
def downLoadPlayList(link):
    yt_playlist = Playlist(link)

    folderName = make_alpha_numeric(yt_playlist.title)
    os.mkdir(folderName)

    totalVideoCount = len(yt_playlist.videos)
    print("Total videos in playlist: ", totalVideoCount)

    for index, video in enumerate(yt_playlist.videos, start=1):
        print("Downloading:", video.title)
        video_size = video.streams.get_highest_resolution().filesize
        video.streams.get_highest_resolution().download(output_path=folderName)
    return totalVideoCount - index

link = input("Enter YouTube Playlist URL:")
if downLoadPlayList(link) == 0:
    print("All videos downloaded successfully!")
else:
    print("Something went wrong")
