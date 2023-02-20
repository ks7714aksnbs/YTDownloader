import mp3_interface_metadata
import mp3_interface_without_metadata
import mp4_interface
import playlist_interface

header = '''

█▄█ ▀█▀ █▀▄ █▀█ █ █ █ █▄ █ █   █▀█ ▄▀█ █▀▄ █▀▀ █▀█
 █   █  █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄

-----------------------------------------------------

'''

print(header)

input_text = '''
-------------------------------------------------------

1. Music - MP3 [With Metadata] [For this option, you need to manually add metadata in the "Music.xlsx" file]

2. Music - MP3 [Without Metadata]

3. Podcasts - MP3 [With Metadata] [For this option, you need to manually add metadata in the "Podcasts.xlsx" file]

4. Podcasts - MP3 [Without Metadata]

5. Videos - MP4 

6. YouTube Playlists

-------------------------------------------------------


Select the type of file you want to download : '''
# user_input = int(input(input_text))


def main():
    while True:
        try:
            user_input = int(input(input_text))
            print('\n')
            break
        except ValueError:
            print('\n\n------Please enter the corresponding number of the type of file you want to download------\n\n')
            continue

    while user_input not in [1, 2, 3, 4, 5, 6]:
        try:
            print('\n\n------Please enter the corresponding number of the type of file you want to download------\n\n')
            user_input = int(input(input_text))
            print('\n')
        except ValueError:
            print('\n\n------Please enter the corresponding number of the type of file you want to download------\n\n')
            user_input = int(input(input_text))
            print('\n')

    print('\n')

    if user_input == 1:
        mp3_interface_metadata.execute_mp3('Music')
    if user_input == 2:
        mp3_interface_without_metadata.execute_mp3_without_metadata('Music')
    if user_input == 3:
        mp3_interface_metadata.execute_mp3('Podcasts')
    if user_input == 4:
        mp3_interface_without_metadata.execute_mp3_without_metadata('Podcasts')
    if user_input == 5:
        mp4_interface.execute_mp4()
    if user_input == 6:
        playlist_interface.execute()


if __name__ == '__main__':
    main()
