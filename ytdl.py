from pytube import YouTube
import os

#global variables
yt = None
res = None
stream = None
file_path = None
#see if the user wants to download audio or video. This way they can get both





#Define Download location 
def download_location():
    global file_path
    while True:
        file_path = input('Please enter the Folder to save the Video in:\n')
        x = os.path.exists(path = str(file_path))
        if x == True:
            break
        else:
            print('The specified Folder does not exit')
            continue

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
    global file_path
    global yt
    while True:
        itag = input('Please Enter the Itag of the stream you want to download:\n')
        try:
            yt.streams.get_by_itag(str(itag)).download(str(file_path))
            print('The video has been downloaded')
            return True
        except:
            print('You have entered an invalid Itag')
            continue
            
def Main():
    download_location()
    video_select()
    resoultion_select()
    download_stream()
    exit()

Main()




""" To do list
Add a function to change between audio and video downloading
Possibly do batch downloading/playlist downloading audio and video
clean up the code and make a proper Main function that does more then just call all the other functions in order.


"""

#test video https://www.youtube.com/watch?v=mODI4-cRhPE
