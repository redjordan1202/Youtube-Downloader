from pytube import YouTube
import os

#global variables
yt = None
res = None
stream = None
#see if the user wants to download audio or video. This way they can get both





#Define Download location 
def download_location():
    







#Select the video that the user wants to use
def video_select():
    global yt
    while True:
        video = input('Please enter the video URL:\n')
        try:
            yt = YouTube(video)
            print('The title of the video you selected is: ' + yt.title)
            return False
        except:
            print('The URL is not Valid\n')
            continue

#Select resoultion and display possible stings
def resoultion_select():
    global res
    global res_list
    while True:
        res = input('Please enter a Resoultion:\n')
        try:
            res_list = yt.streams.filter(resolution= str(res)).all()
            print(*res_list, sep='\n')
            return False
        except:
            print('You have entered an invalid resoultion')
            continue

#Select the stream to download based on the itag
def download_stream():
    global yt
    while True:
        itag = input('Please Enter the Itag of the stream you want to download:\n')
        try:
            yt.streams.get_by_itag(str(itag)).download()
            print('The video has been downloaded')
            return True
        except:
            print('You have entered an invalid Itag')
            continue
            
            

#C:\Users\redjo\Videos\Youtube Downloads

#download function for both video and audio May split if its needed




#Someway to cycle to program back to the top so that user can download more then 1 video.

#might add a multi downloader to download more then 1 video at a time

#download location selector


video_select()
resoultion_select()
download_stream()

""" To do list
Correct resoultion_select func I want to have it display the list 
of streams based on resltion and then have user select stream by itag based on the list
Implement a download func
Give users a choice of downloading audio stream or video so users can get both with the same program.
have program cycle back to the start unelss the user exits with a command """








#test video https://www.youtube.com/watch?v=mODI4-cRhPE

"""   """