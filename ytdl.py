from pytube import YouTube

yt = None
res = None
stream = None
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
    global stream
    while True:
        res = input('Please enter a Resoultion:\n')
        try:
            stream = yt.streams.filter(resolution= str(res),audio_codec='mp4a.40.2').first()
            return False
        except:
            print('You have entered an invalid resoultion')
            continue




video_select()
resoultion_select()
stream.download()

""" To do list
Correct resoultion_select func I want to have it display the list 
of streams based on resltion and then have user select stream by itag based on the list
Implement a download func
Give users a choice of downloading audio stream or video so users can get both with the same program.
have program cycle back to the start unelss the user exits with a command """








#test video https://www.youtube.com/watch?v=mODI4-cRhPE

