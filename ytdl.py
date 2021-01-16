from pytube import YouTube
import os
from tkinter import *
from tkinter import filedialog

#global variables
yt = None
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

def Main():
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
    print(str(resolution))
    
    

    
#Main()

window = Tk()
window.minsize(width = 450, height = 500)



#video info gathering
frm_url = Frame(master = window, height = 100, width = 400, )
frm_url.pack_propagate(0)
frm_url.pack()

lbl_url = Label(master = frm_url, text = "Please Enter Video URL")
lbl_url.pack(pady = 10)

ent_url = Entry(master = frm_url)
ent_url.pack(pady = 10)

btn_download = Button(master = frm_url, text = "Download")
btn_videoinfo = Button(master = frm_url,text = "View Video Info", command = print_video_info)
btn_download.pack(side = LEFT, padx = 50)
btn_videoinfo.pack(side = RIGHT, padx = 50)

line = Frame(height = 1, bg = "black")
line.pack(fill = X, pady = 20, padx = 5)

frm_res = Frame(master = window)
frm_res.pack()

lbl_res = Label(master = frm_res, text = "Please Select the Resoultion")
lbl_res.pack()

res = StringVar(window, "480p")
values ={'480p' : '480p',
'720p' : '720p',
'1080p' : '1080p',
'1440p' : '1440p',
'4k' : '4k',
}
for (text, value) in values.items():
    Radiobutton(master = frm_res, text = text, variable = res, value = value).pack(side = LEFT, padx = 20)










window.mainloop()


