from pytube import YouTube, Playlist
import pandas as pd


def extract_data():
    file = pd.read_excel('./Data/Videos.xlsx').sort_values('Title')
    df = file.values
    return df


def execute_mp4():
    header = '-' * 70
    count = 0

    for count, item in enumerate(extract_data()):

        link = item[0]
        title = item[1]

        print(header)
        print(title)
        print(header)

        youtube_object = YouTube(link).streams.filter(
            progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        youtube_object = youtube_object.download(f'./Videos')
