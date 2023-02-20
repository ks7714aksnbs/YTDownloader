import re
from pytube import Playlist
from pytube import YouTube
from pydub import AudioSegment
import os


def playlist_link(playlist_link):
    playlist_object = Playlist(playlist_link)
    playlist_object._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    return playlist_object.video_urls


def download_mp3():
    header = '-' * 70

    print(header)
    playlist_link_input = str(input('Please enter playlist link : '))
    print(header)
    print('\n\n')
    while 'youtube.com/playlist' not in playlist_link_input:
        print('-----Please enter a valid playlist link-----\n\n')
        print(header)
        playlist_link_input = str(input('Please enter playlist link : '))
        print(header)
        print('\n\n')

    for link in playlist_link(playlist_link_input):
        youtube_object = YouTube(link).streams.filter(
            progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        print(header)
        print(youtube_object.title)
        print(header)
        youtube_object = youtube_object.download(f'./Temp')


def codec_conversion_mp3(input):
    file = os.listdir(f'./Temp')
    for name in file:
        filename = os.path.splitext(name)[0]
        mp3_file = AudioSegment.from_file(f'./Temp/{filename}.mp4', "mp4")
        output_path = f'./{input}/{filename}.mp3'
        mp3_file.export(output_path, format="mp3", bitrate="320k")


def clean_up_mp3():
    file = os.listdir(f'./Temp')
    for name in file:
        file_extension = os.path.splitext(name)[1]
        if file_extension == '.mp4':
            os.remove(f'./Temp/{name}')


def download_mp4():

    header = '-' * 70

    playlist_link_input = str(input('Please enter playlist link : '))
    print('\n\n')
    while 'youtube.com/playlist' not in playlist_link_input:
        print('-----Please enter a valid playlist link-----\n\n')
        print(header)
        playlist_link_input = str(input('Please enter playlist link : '))
        print(header)
        print('\n')

    for link in playlist_link(playlist_link_input):
        youtube_object = YouTube(link).streams.filter(
            progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        print(header)
        print(youtube_object.title)
        print(header)
        youtube_object = youtube_object.download(f'./Videos')


file_type_input_text = '''
1. Music

2. Podcasts

3. Videos

4. Go Back

Select the type of file you want to download : '''

lc = 'https://www.youtube.com/playlist?list=PL2DmEqSeFJKpMmAh8z996A9OVhcAhEO6u'


def execute():
    header = '-' * 70
    while True:
        try:

            print(header)
            file_type_input = int(input(file_type_input_text))
            print(header)
            print('\n')
            break
        except ValueError:
            print('\n\n------Please enter the corresponding number of the type of file you want to download------\n\n')
            continue

    while file_type_input not in [1, 2, 3, 4]:
        try:
            print('\n\n------Please enter the corresponding number of the type of file you want to download------\n\n')
            print(header)
            file_type_input = int(input(file_type_input_text))
            print(header)
            print('\n')
        except ValueError:
            print('\n\n------Please enter the corresponding number of the type of file you want to download------\n\n')
            print(header)
            file_type_input = int(input(file_type_input_text))
            print(header)
            print('\n')

    print('\n')

    if file_type_input == 1:
        download_mp3()
        codec_conversion_mp3('Music')
        clean_up_mp3()

    if file_type_input == 2:
        download_mp3()
        codec_conversion_mp3('Podcasts')
        clean_up_mp3()

    if file_type_input == 3:
        download_mp4()

    if file_type_input == 4:
        exit()
