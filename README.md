# YTDownloader

YTDownloader (Definitely open to a more creative name ideas for the program)
This program lets you download media from YouTube without going through a dozen ads on some shady website that will embed some highly innacurate metadata.

Discalimer : I do not promote the use of downloaded media unless absolutely necessary, It is highly recommended that you watch content directly from YouTube and support creators.


# Features of the program

1. Downloads MP3 & MP4 Files.
2. Supports Bulk Downloads From Lists.
3. Download youtube playlists without individually going through each video.
4. You can embed metadata on your own to insure accuracy.
5. Option to override default album_art and embed preferred or custom album_art.
6. Files are downloaded pre-organised in folders with respect to the user's preference.

# How to use the program

Currently the program supports windows environment only, however with a few turn arounds in the activation of virtual environment through zsh or bash, you can get it up and running on a mac or linux too.

1. First download the program on your system, you could do this from the github gui or git clone shone as follows :

```       
git clone git@github.com:ks7714aksnbs/YTDownloader.git
```   
Or,                       
                          
```
git clone https://github.com/ks7714aksnbs/YTDownloader.git       
```

2. Once the download is completed, open powershell and type (Not necessary if you have python installed already):

```
winget install  Python.Python.3.11
```

3. Once the download is completed, open powershell or command prompt and type (This step is necessary to avoid any ffmpeg related errors) :

```
cd <path_to_file>
```

```
.\Scripts\Activate.ps1                        #For powershell
pip install -r requirements.txt
```
```
.\Scripts\activate.bat                        #For command prompt
pip install -r requirements.txt
```


3. Minimise the terminal and paste all the links in the music.xlsx,podcasts.xlsx or video.xlsx based on your preference in the Data Folder. 

4. You could also add metadata if you choose to do so, just make sure you don't leave the title field blank.

5. Once you've added all the links to your preferred files then head back to the terminal and type:

```
python main.py
```

6. Choose your preferred options and your files will be downloaded in the corresponding folders under "YTDownloader"

# NOTE : If you have embedded metadata then choose the options that say "[With Metadata]" and if you haven't embedded any metadata then choose the options that say "[Without Metadata]".



# Further Improvements
This program is in its initial stage and at this point the code isn't something that I would call highly efficient, Not only is that something that has to be worked on but it hasn't been properly optimised for error and exception handling yet.
However the program serves as a very productive utility if you need an All in One tool to download medi from YouTube without any problems.

The following are some improvements that you can expect in the future :

1. A better and more functional UI
2. Automatic metadata search and embedding
3. User Specified location to save media
4. An interactive and fully functional GUI
5. A better multi-platform support.

Please note, I'm a student and my code might not be the best in terms of efficiency, therefore any critiques and contribution to the program through better code and functionality implementations to better ideas are much appreciated :)

Thank you for using the program :)


