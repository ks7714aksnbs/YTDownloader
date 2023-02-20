from pytube import YouTube   # Downloads the Audio in MP4 Format
from pydub import AudioSegment   # Converts the Audio in MP3 Format
import pandas as pd   # Used for classification of data in excel files
import numpy as np   # Used for sorting arrays from classified data
import os   # Used for interacting with files in the machine
import eyed3  # Used for embedding thumbnails to MP3 Files and any metadata
import urllib.request   # Used to download thumbnails from url
from PIL import Image   # Used to convert thumbnails from url to jpg
import shutil   # Used to move files from program folder to specified destination
# Used for generating a delay in request rate to avoid any potential request errors.


class MP3:
    def __init__(self, readfrom):
        self.readfrom = readfrom

    def extract_data(self):  # Extracts Data from Excel File
        file = pd.read_excel(f'./Data/{self.readfrom}.xlsx')
        df = file.values
        return df

    # This function just sorts the data for embedding metadata later on.
    def metadata_data_order(self):
        path = f'./Temp'
        files = []
        for item in os.listdir(path):
            files.append(item)
        files.sort()
        return files

    # The following function embeds metadata to the extracted MP3 File
    def codec_conversion(self, title):

        # The following lines are to convert the MP4 File to MP3 with possible metadata
        input_path = f'./Temp/{title}'
        mp3_file = AudioSegment.from_file(f'{input_path}.mp4', "mp4")
        output_path = f'./Metadata_Included/{title}.mp3'
        mp3_file.export(output_path, format="mp3", bitrate="320k")

        # The following embeds the remaining metadata to the MP3 File

    def embed_metadata(self, creator, title):
        output_path = f'./Metadata_Included/{title}.mp3'
        new_mp3_file = eyed3.load(output_path)
        new_mp3_file.initTag(version=(2, 3, 0))
        image_path = f'./Thumbnails/{title}.jpg'
        with open(image_path, mode='rb') as thumbnail:
            thumbnail_data = thumbnail.read()

        new_mp3_file.tag.artist = creator
        new_mp3_file.tag.title = title
        new_mp3_file.tag.album_artist = creator
        new_mp3_file.tag.images.set(3, thumbnail_data, "image/jpeg", u"cover")
        new_mp3_file.tag.save()

    def move(self, title):  # After the entire execution, this function moves all the files to a separate folder
        input_path = f'./Metadata_Included/{title}.mp3'
        output_path = f'./{self.readfrom}'
        shutil.move(input_path, output_path)

    def clean_up(self, title):  # Cleans Up the folders in the program files (python program files)
        input_path = f'./Temp/{title}.mp4'
        input_path2 = f'./Thumbnails/{title}.jpg'

        os.remove(input_path)
        os.remove(input_path2)


class ObjectInfo:
    def __init__(self, data):
        self.data = data

    # The following functions extract elements from the extracted data from excel file

    def titles(self):
        all_titles = []
        for item in self.data:
            all_titles.append(item[1])

        return all_titles

    def links(self):
        all_links = []
        for item in self.data:
            all_links.append(item[0])

        return all_links

    def creators(self):
        all_creators = []
        for item in self.data:
            all_creators.append(item[2])

        return all_creators

    # The following function arranges the extracted data into order w.r.t the titles

    def arrange_array(self):
        df2 = pd.DataFrame(self.data, columns=[
                           'Links (Necessary)', 'Titles (Optional)', 'Creators (Optional)', 'Thumbnail URLs (.jpg) (Optional)'])
        sorted_data = df2.sort_values('Titles (Optional)', ascending=True)

        return np.array(sorted_data)

    # The following function arranges metadata into a list
    def arranging_metadata(self, data_order):
        values = []
        for item in data_order:
            values.append(item)
        return values


class GetThumbnail:
    def __init__(self, title, link):
        self.title = title
        self.link = link

    # The following function downloads the thumbnails from either a specified link or default YouTube Link
    def download_thumbnail(self, value):

        if type(value) != float:  # Downloads The Thumbnail from specified link
            if 'https://www.youtube.com' in str(value):
                thumbnail_url = YouTube(value).thumbnail_url
                image_path = f'./Thumbnails/{self.title}.jpg'
                urllib.request.urlretrieve(thumbnail_url, image_path)
                image = Image.open(image_path)

            else:
                thumbnail_url = value
                image_path = f'./Thumbnails/{self.title}.jpg'
                urllib.request.urlretrieve(thumbnail_url, image_path)
                image = Image.open(image_path)
        else:                   # Downloads the default YouTube Link
            thumbnail_url = YouTube(self.link).thumbnail_url
            image_path = f'./Thumbnails/{self.title}.jpg'
            urllib.request.urlretrieve(thumbnail_url, image_path)
            image = Image.open(image_path)


def execute_mp3(file):

    check_list = []
    # Required Data For Execution
    mp3_object = MP3(file)
    mp3_object_dataframe = ObjectInfo(mp3_object.extract_data())
    mp3_object_array = mp3_object_dataframe.arrange_array()

    # Execution Begins

    for count, item in enumerate(mp3_object_array):

        link = item[0]
        title = item[1]
        creator = item[2]
    # FILE DOWNLOAD PROCEDURE STARTS HERE
        header = '-' * 70

        if count == 0:
            print(header)
            print(title)
            print(creator)
            print(header)
        else:
            print(title)
            print(creator)
            print(header)
        try:

            youtube_object = YouTube(link)
            youtube_object = youtube_object.streams.filter(
                only_audio=True, file_extension='mp4').order_by('abr').desc().first()
            youtube_object = youtube_object.download(
                f'./Temp', f'{title}.mp4')

        except KeyboardInterrupt:
            continue

    # FILE DOWNLOAD PROCEDURE ENDS HERE
    # Required data for embedding metadata

    metadata_order = mp3_object.metadata_data_order()
    metadata_values = mp3_object_dataframe.arranging_metadata(metadata_order)
    # Embedding Metadata
    for count, item in enumerate(mp3_object_array):
        # Extracting data for embedding
        link = item[0]
        title = item[1]
        creator = item[2]
        thumbnails = item[3]
        # Converting Codecs from MP4 to MP3
        try:
            mp3_object.codec_conversion(title)
            # Extracting required thumbnails for the MP3 Files
            thumbnail = GetThumbnail(title, link)
            thumbnail.download_thumbnail(thumbnails)
            # Embedding All Metadata and Thumbnails to the respective MP3 File
            mp3_object.embed_metadata(creator, title)
            mp3_object.move(title)
            mp3_object.clean_up(title)
        except:
            continue
