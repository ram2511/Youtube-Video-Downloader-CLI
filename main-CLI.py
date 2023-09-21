import pytube
import os
import subprocess


def videoDownload(videoURL):
    yt=pytube.YouTube(videoURL)
    yt.streams.get_highest_resolution().download()
    print("video download successfully")
    
def playListDownload(playListURL):
    pl=pytube.Playlist(playListURL)
    playListFolder(pl.title)
    print(pl.title,"Folder is created... ")
    os.chdir(pl.title)
    for i in pl:
        print(i)
        yt=pytube.YouTube(i)
        yt.streams.get_highest_resolution().download()
    print("PlayList Download successfully")
    
def playListFolder(folderName):
    if(os.path.exists(folderName)):
        playListFolder()    
    else:
        os.mkdir(folderName)

choice=True
rootDir=os.getcwd()
while choice:
    os.chdir(rootDir)
    print("------------YOUTUBE VIDEO DOWNLOADER------------")
    print("Choices;\n   [1]Video\n   [2]Playlist ")
    options=int(input())
    if(options==1):
        videoDownload(input("Video URL: "))
    elif(options==2):
         playListDownload(input("Playlist URL: "))       

    choice=input("Do you wnat download some contents ? [yes/no]").lower()=="yes"
