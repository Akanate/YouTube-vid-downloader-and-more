import os
import requests
import shutil
import time
def choice():
    choose = input("Do you have git hub terminal: ")
    if choose == "yes":
        git_install()
    elif choose == "no":
        windows_updater()
    else:
        print("Invalid option")
        choice()

def git_install():
    print("Starting update")
    cwd = os.getcwd()
    os.chdir(cwd)
    os.system("rmdir /q /s instaInstaller")
    os.system("git clone https://github.com/WHYSOEASY/instaInstaller.git")
    print("Done")
    exit()

def windows_updater():
    time.sleep(1)
    print("Getting url")
    url = "https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe"
    requested = requests.get(url)
    contents = requested.content
    time.sleep(1)
    print("Downloading git into file")
    cwd = os.getcwd()
    os.chdir(cwd)
    f = open("git.exe","wb")
    f.write(contents)
    f.close()
    print("Put contents into file")
    os.system("git.exe")
    print("Downloaded")
    print("Getting update")
    os.chdir(cwd)
    os.system("git clone https://github.com/WHYSOEASY/instaInstaller.git")
    print("Updated")
    os.system("del git.exe")
    exit()
    
    
choice()
