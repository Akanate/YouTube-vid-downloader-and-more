import pytube
from pytube import Playlist
import requests
import os
import shutil


def main():
    print('Welcome to downloader')
    choice = input('''
    1.Youtube Downloader
    2.Image downloader
    3.Desktop image getter
    4.Source code copier
    Enter your choice: ''')
    if choice == '1':
        youtube_choice()
    elif choice == '2':
        image()
    elif choice == '3':
        spotlight()
    elif choice == '4':
        source()
    else:
        print('Enter a valid choice')
        main()

def youtube_choice():
    choices = input('''
    1.Download a single video
    2.Download a playlist
    3.Go back
    Enter a choice: ''')
    if choices == '1':
        download()
    elif choices == '2':
        playlist()
    elif choices == '3':
        main()
    else:
        print('Enter a valid choice')
        youtube_choice()

def download():
    link = input('Enter the video you want to download: ')
    yt = pytube.YouTube(link)
    videos = yt.streams.all()

    s = 1
    for v in videos:
        print(str(s)+". "+str(v))
        s+=1
    n = int(input('Enter the number of videos: '))
    vid = videos[n-1]

    dest = input('Enter the destination file: ')
    vid.download(dest)

    print("Download succesful")
    main()

def playlist():
    try:
        global folder
        destination = input('Enter the link of the playlist you want to install: ')
        folder = input('Enter the folder you want to save it in: ')
        linked = Playlist(destination)
        linked.download_all(folder)
        print('Downloaded your videos too',folder)
        your_choice = input('Do you want to zip this folder: ')
        if your_choice == 'yes' or your_choice == 'Yes':
            compress()
        elif your_choice == 'no' or your_choice == 'No':
            main()
        else:
            print('You typed wrong sending you back to main menu')
            main()
    except:
        print('We have managed to download some videos or maybe non at all but have encountered an error try a different playlist')
        main()
    main()



def image():
    global folder
    new_image = input('Enter the image you want to download: ')
    requested = requests.get(new_image)
    contents = requested.content
    file = input('Enter the file where you want to put it make sure it is a .jpg: ')
    f = open(file,'wb')
    f.write(contents)
    f.close()
    print('Done')
    main()



def spotlight():
    global folder
    print('Making a batch file which will execute and get all the spotlight folders and save them to a location of your choice')
    temporary = input('Enter where the batch file should be stored make sure to put .bat: ')
    file = input('Where do you want to save your images too: ')
    g = open(temporary,'a')
    g.write('''
    @echo 
    set Path=C:/Windows/System32
    set file='''+file+'''
    mkdir %file% >> nul
    set dst=%file%
    robocopy "%USERPROFILE%/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets" "%file%" 
    cd %file%
    rename *. *.png
    ''')
    g.close()
    os.system(temporary)
    print('Done')
    main()

def source():
    global folder
    print('This will get the source code of any website')
    linked = input('Enter the link of the website you want the source off: ')
    file = input('Enter where you want this source code to be stored make sure to put .html: ')
    r = requests.get(linked)
    contents = r.content
    d = open(file,'wb')
    d.write(contents)
    d.close()
    print('Done')
    main()


main()




        