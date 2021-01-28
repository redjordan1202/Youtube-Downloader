from pytube import YouTube
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

filepath = os.path.expandvars(R"C:\Users\$USERNAME\Videos")




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




    


class MainApplication:
    def __init__(self,master, *args, **kwargs):
        self.master = master
        """video Select"""
        self.frm_url = tk.Frame(master = self.master, height = 260, width = 450, highlightbackground = 'black', highlightthickness = 1)
        self.frm_url.pack_propagate(0)
        self.frm_url.pack(pady = 5)

        self.lbl_url = tk.Label(master = self.frm_url, text = "Please Enter Video URL")
        self.lbl_url.pack(pady = 10)

        self.ent_url = tk.Entry(master = self.frm_url, width = 50, justify = 'center')
        self.ent_url.pack(pady = 10,)

        self.btn_select = tk.Button(master = self.frm_url, text = "Select Video", command = self.select_video)
        self.btn_select.pack()

        self.btn_download = tk.Button(master = self.frm_url, text = "Select Download Folder", command = self.save_window)
        self.btn_download.pack()

        self.line0 = tk.Frame( master = self.frm_url, height = 1, bg = "black")
        self.line0.pack(fill = tk.X, pady = 20, padx = 5)

        self.lbl_yt_title = tk.Label(master = self.frm_url, text = "Video Title")
        self.lbl_yt_title.pack(pady = 5)

        self.ent_yt_title = tk.Entry(master = self.frm_url, text = "", width = 50, justify = 'center', state = tk.DISABLED)
        self.ent_yt_title.pack()

        """Resoultion Selection"""
        self.frm_res = tk.Frame(master = self.master)
        self.frm_res.pack()

        self.lbl_res = tk.Label(master = self.frm_res, text = 'Please Select Resoultion')
        self.lbl_res.grid(column = 1, row = 0, columnspan = 5, pady = 5)

        self.resoultion = tk.StringVar(self.master, '480p')
        self.rbtn_resoultions = ['480p','720p','1080p','1440p','2160p']
        self.rbtn_480p = tk.Radiobutton(master = self.frm_res, text = '480p', value = '480p', variable = self.resoultion, state = tk.DISABLED)
        self.rbtn_720p = tk.Radiobutton(master = self.frm_res, text = '720p', value = '720p', variable = self.resoultion, state = tk.DISABLED)
        self.rbtn_1080p = tk.Radiobutton(master = self.frm_res, text = '1080p', value = '1080p', variable = self.resoultion, state = tk.DISABLED)
        self.rbtn_1440p = tk.Radiobutton(master = self.frm_res, text = '1440p', value = '1440p', variable = self.resoultion, state = tk.DISABLED)
        self.rbtn_2160p = tk.Radiobutton(master = self.frm_res, text = '4K', value = '2160p', variable = self.resoultion, state = tk.DISABLED)

        self.rbtn_480p.grid(column = 1, row = 1)
        self.rbtn_720p.grid(column = 2, row = 1)
        self.rbtn_1080p.grid(column = 3, row = 1)
        self.rbtn_1440p.grid(column = 4, row = 1)
        self.rbtn_2160p.grid(column = 5, row = 1)

        self.frm_download = tk.Frame(master = self.master)
        self.frm_download.pack(pady = 10)

        self.lbl_streams = tk.Label(master = self.frm_download, text = 'Available Streams')
        self.lbl_streams.grid(column = 0, row = 0, columnspan = 3, pady = (5,20))
        
        self.btn_download_video = tk.Button(master = self.frm_download, text = 'Download Video', command = self.download_video)
        self.btn_download_video.grid(column = 0, row = 3, padx = 30)
        self.btn_download_audio = tk.Button(master = self.frm_download, text = 'Download Audio')
        self.btn_download_audio.grid(column = 2, row = 3, padx = 30)
        self.progress = ttk.Progressbar(master= self.frm_download,orient=tk.HORIZONTAL, length=300, mode="determinate" )
        self.progress.grid(column = 0 , row= 4, columnspan = 3, pady = 10)
        


    def progress_check(self, chunck, file_handle, bytes_remaning):
        self.percent = (100*(self.file_size - bytes_remaning))/self.file_size
        if self.percent 




    def select_video(self):
        self.resoultions = []
        for resoultion in self.rbtn_resoultions:
            exec("self.rbtn_" + str(resoultion) +'.config(state = tk.DISABLED)')

        try:
            self.yt = YouTube(self.ent_url.get(), on_progress_callback=self.progress_check)
        except:
            self.ent_yt_title.config(state = tk.NORMAL)
            self.ent_yt_title.delete(0, tk.END)
            self.ent_yt_title.insert(0, "Please Enter a Valid URL")
            self.ent_yt_title.config(state = tk.DISABLED)
            return

        

        for i in self.yt.streams.filter(type = "video"): self.resoultions.append(i.resolution)
        self.res_list = []
        [self.res_list.append(x) for x in self.resoultions if x not in self.res_list] 
        print(self.res_list)

        for i in self.res_list:
            if i not in self.rbtn_resoultions:
                self.res_list.remove(i)
        self.res_list.remove('144p')
        print(self.res_list)

        for resoultion in self.res_list:
            exec("self.rbtn_" + str(resoultion) +'.config(state = tk.NORMAL)')
        self.ent_yt_title.config(state = tk.NORMAL)
        self.ent_yt_title.delete(0, tk.END)
        self.ent_yt_title.insert(0, str(self.yt.title))
        self.ent_yt_title.config(state = tk.DISABLED)
        print(self.res_list)
        
    def save_window(self):
        self.save_window = tk.Toplevel(self.master)
        self.save_window.geometry('400x150')
        self.save_window.transient(self.master)
        self.app1 = SaveDialouge(self.save_window)
        self.save_window.mainloop()

    def download_video(self):
        global filepath
        self.file_size = self.yt.streams.filter(resolution = (str(self.resoultion.get()))).first().filesize
        self.yt.streams.filter(resolution = (str(self.resoultion.get()))).first().download()
        
        

        
        



class SaveDialouge:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.frm_save = tk.Frame(master = self.master)
        self.frm_save.pack()
        self.path = os.path.expandvars(R"C:\Users\$USERNAME\Videos")

        self.lbl_location = tk.Label (master = self.frm_save, text = 'Please select a Download Folder')
        self.lbl_location.grid(column = 1, row = 0, columnspan = 2, pady = 10)

        self.ent_location = tk.Entry (master = self.frm_save, width = 45,)
        self.ent_location.insert(0,str(self.path))
        self.ent_location.grid(column = 0, row = 1, columnspan = 2)
        

        self.btn_browse = tk.Button(master = self.frm_save,text = 'Browse...', width = 15, command = self.browse_folder)
        self.btn_browse.grid(column = 3, row = 1,)

        self.btn_confirm = tk.Button(master = self.frm_save, text = 'Confirm', width = 15, command = self.confirm)
        self.btn_confirm.grid(column = 3, row = 2, pady = 10)

        self.btn_default = tk.Button(master = self.frm_save, text = 'Set to Default', width = 15, command = self.set_default)
        self.btn_default.grid(column = 1, row = 2, pady = 10)

    def browse_folder(self):
        self.path = filedialog.askdirectory()
        self.ent_location.delete(0, tk.END)
        self.ent_location.insert(0,str(self.path))
        print(self.path)
    
    def set_default(self):
        self.path = os.path.expandvars(R"C:\Users\$USERNAME\Videos")
        self.ent_location.delete(0, tk.END)
        self.ent_location.insert(0,str(self.path))
    
    def confirm(self):
        global filepath
        filepath = str(self.path)
        print(filepath)
        self.master.destroy()



    
        

        
            






def main(): 
    root = tk.Tk()
    root.geometry('450x800')
    app = MainApplication(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()

