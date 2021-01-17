from pytube import YouTube
import os
from tkinter import *
from tkinter import filedialog

#global variables
res = None
stream = None
file_path = None
av_swtich = None
video = None


#see if the user wants to download audio or video

def av_select():
    global av_switch
    print('Would you like to download Video or Audio:')
    while True:
        av_switch = input('Please enter \'1\' for Video and \'2\' for Audio\n')
        if av_switch not in ('1', '2'):
            print('Pleae make a valid selection')
            continue
        else:
            break

#Download Audio Stream

def audio_download():
    global yt
    global file_path
    print('The Video has the following audio streams')
    print(*yt.streams.filter(only_audio=True), sep='\n')
    while True:
        itag = input('Please Enter the Itag of the stream you want to download:\n')
        try:
            yt.streams.get_by_itag(str(itag)).download(output_path=str(file_path), filename_prefix='Audio-')
            print('The audio stream has been downloaded')
            return True
        except:
            print('You have entered an invalid Itag')
            continue
        
#Define Download location 
def download_location():
    global file_path
    while True:
        file_path = input('Please enter the Folder to save the Video in\nPlease enter the Full Path')
        x = os.path.exists(path = str(file_path))
        if x == True:
            break
        else:
            print('The specified Folder does not exit')
            continue

#Select the video that the user wants to use
def video_select():
    resoultions = []
    yt = YouTube(ent_url.get())
    for i in yt.streams.filter(type = "video"): resoultions.append(i.resolution)
    ent_yt_title.config(state = NORMAL)
    ent_yt_title.insert(0, str(yt.title))
    ent_yt_title.config(state = DISABLED)
    print(str(resoultions))
    
    


def print_video_info():
    global video
    global yt
    res = []
    video = ent_url.get()
    yt = YouTube(video)
    print(yt.title)
    for i in yt.streams.filter(type = "video"): res.append(i.resolution)
    resolution = [] 
    [resolution.append(x) for x in res if x not in resolution] 
    resolution.sort()
    


    

#Select resoultion and display possible stings
def resoultion_select():
    global res
    global res_list
    while True:
        res = input('Please enter a Resoultion:\n')
        try:
            res_list = yt.streams.filter(resolution= str(res))
            return False
        except:
            print('You have entered an invalid resoultion')
            continue

#Select the stream to download based on the itag
def download_stream():
    global file_path
    global yt
    global res_list
    print('The Video has the following streams')
    print(*res_list, sep='\n')
    while True:
        itag = input('Please Enter the Itag of the stream you want to download:\n')
        try:
            yt.streams.get_by_itag(str(itag)).download(str(file_path))
            print('The video has been downloaded')
            return True
        except:
            print('You have entered an invalid Itag')
            continue

def main():
    global av_switch
    print('Welcome to the Youtube Video Downloader\n')
    download_location()
    video_select()
    av_select()
    if av_switch == '1':
        resoultion_select()
        download_stream()
    else:
        audio_download()



    


window = Tk()
window.minsize(width = 450, height = 500)


""" video Info gaterhing """

frm_url = Frame(master = window, height = 200, width = 400, )
frm_url.pack_propagate(0)
frm_url.pack()

lbl_url = Label(master = frm_url, text = "Please Enter Video URL")
lbl_url.pack(pady = 10)

ent_url = Entry(master = frm_url, width = 300, justify = 'center')
ent_url.pack(pady = 10)

btn_info = Button(master = frm_url, text = "Select Video", command = video_select)
btn_info.pack()

line0 = Frame( master = frm_url, height = 1, bg = "black")
line0.pack(fill = X, pady = 20, padx = 5)

lbl_yt_title = Label(master = frm_url, text = "Video Title")
lbl_yt_title.pack(pady = 5)

ent_yt_title = Entry(master = frm_url, text = "", width = 300, justify = 'center', state = DISABLED)
ent_yt_title.pack()

line1 = Frame( master = frm_url, height = 1, bg = "black")
line1.pack(fill = X, pady = 20, padx = 5)

"""Resoultion Selection"""
frm_res = Frame (master = window)
frm_res.grid()






window.mainloop()


