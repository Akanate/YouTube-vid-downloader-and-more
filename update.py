import os
import requests

def start_install():
    print('Welcome to the updater I see you have come to update')
    choice = input('''
    1.Full update(This includes the installation of git terminal)
    2.Normal update(This updates your version using git terminal)
    Enter a choice: ''')
    if choice == '1':
        full()
    elif choice == '2':
        Normal()
    else:
        print('Enter a vaild choice')
        start_install()


def full():
    print('Starting installation')
    url = requests.get('https://github.com/git-for-windows/git/releases/download/v2.22.0.windows.1/Git-2.22.0-64-bit.exe')
    content = url.content
    f = open('git_terminal.exe','wb')
    f.write(content)
    f.close()
    os.system('git_terminal.exe')
    print('Installed github terminal beginning installation of update')
    cwd = os.getcwd()
    os.chdir(cwd)
    os.system('cd ..')
    os.system('del /x /q YouTube-vid-downloader-and-more')
    os.system('git clone https://github.com/WHYSOEASY/Youtube-vid-downloader-and-more.git')
    os.system('cd YouTube-vid-downloader-and-more')
    print('Update successful')
    quit()

def Normal():
    os.chdir(cwd)
    os.system('cd ..')
    os.system('del /x /q YouTube-vid-downloader-and-more')
    os.system('git clone https://github.com/WHYSOEASY/YouTube-vid-downloader-and-more.git')
    print('Update done')
    quit()



start_install()