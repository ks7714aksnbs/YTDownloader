from pytube import YouTube
from pydub import AudioSegment
import pandas as pd
import os


class MP3():
    def __init__(self, readfrom):
        self.readfrom = readfrom

    def extract_data(self):
        file = pd.read_excel(f'./Data/{self.readfrom}.xlsx')
        df = file.values
        return df

    print('\n\n')

    def download_mp3_without_metadata(self):
        header = '-' * 70
        for data in self.extract_data():
            link = data[0]
            youtube_object = YouTube(link).streams.filter(
                progressive=True, file_extension="mp4").order_by('resolution').desc().first()
            print(header)
            print(youtube_object.title)
            print(header)
            youtube_object = youtube_object.download('./Temp')

    def codec_conversion(self):
        file = os.listdir(f'./Temp')
        for name in file:
            filename = os.path.splitext(name)[0]
            mp3_file = AudioSegment.from_file(f'./Temp/{filename}.mp4', "mp4")
            output_path = f'./{self.readfrom}/{filename}.mp3'
            mp3_file.export(output_path, format="mp3", bitrate="320k")

    def clean_up(self):
        file = os.listdir(f'./Temp')
        for name in file:
            file_extension = os.path.splitext(name)[1]
            if file_extension == '.mp4':
                os.remove(f'./Temp/{name}')


def execute_mp3_without_metadata(file):
    mp3_object = MP3(file)
    mp3_object.download_mp3_without_metadata()
    mp3_object.codec_conversion()
    mp3_object.clean_up()
