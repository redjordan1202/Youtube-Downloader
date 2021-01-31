from pytube import YouTube
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
from tkinter import messagebox

filepath = os.path.expandvars(R"C:\Users\$USERNAME\Videos")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainApplication:
    def __init__(self,master, *args, **kwargs):
        self.master = master
        self.filepath = os.path.expandvars(R"C:\Users\$USERNAME\Videos")

        """video Select"""
        self.frm_url = tk.Frame(master = self.master, height = 200, width = 450)
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

        self.lbl_yt_title = tk.Label(master = self.frm_url, text = "Video Title:")
        self.lbl_yt_title.pack(pady = 5)

        self.lbl_yt_title= tk.Label(master = self.frm_url, text = 'Please Select Video')
        self.lbl_yt_title.pack()
        
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

        """Download and download progress"""
        self.frm_download = tk.Frame(master = self.master)
        self.frm_download.pack(pady = 10)

        self.lbl_streams = tk.Label(master = self.frm_download, text = 'Available Streams')
        self.lbl_streams.grid(column = 0, row = 0, columnspan = 3, pady = (5,20))
        
        self.btn_download_video = tk.Button(master = self.frm_download, text = 'Download Video', command = self.start_download_video, state = tk.DISABLED)
        self.btn_download_video.grid(column = 0, row = 3, padx = 30)
        self.btn_download_audio = tk.Button(master = self.frm_download, text = 'Download Audio', command = self.start_download_audio, state = tk.DISABLED)
        self.btn_download_audio.grid(column = 2, row = 3, padx = 30)
        self.lbl_progress = tk.Label(master = self.frm_download, text = 'Download Status: Waitng for download')
        self.lbl_progress.grid(column = 0 , row= 4, columnspan = 3, pady = 10)
        self.progress = ttk.Progressbar(master= self.frm_download,orient=tk.HORIZONTAL, length=300, mode="determinate" )
        self.progress.grid(column = 0 , row= 5, columnspan = 3, pady = 10)
        
        self.butons = [self.rbtn_480p, self.rbtn_720p, self.rbtn_1080p, self.rbtn_1440p, self.rbtn_2160p, self.btn_select, self.btn_download, self.btn_download_video, self.btn_download_audio]

        """Functions"""
    def progress_check(self, chunck, file_handle, bytes_remaning):
        self.percent = (100*(self.file_size - bytes_remaning))/self.file_size
        if self.percent < 100:
            self.progress['value'] = self.percent
            self.lbl_progress.config(text = "Download Status: {:00.0f}% Downloaded".format(self.percent))
        else:
            self.progress['value'] = 100
            self.lbl_progress.config(text = "Download Status: Download Complete!")
            for x in self.butons:
                x.config(state = tk.NORMAL)
            
    def select_video(self):
        self.resoultions = []
        for resoultion in self.rbtn_resoultions:
            exec("self.rbtn_" + str(resoultion) +'.config(state = tk.DISABLED)')

        try:
            self.yt = YouTube(self.ent_url.get())
        except:
            self.lbl_yt_title.config(text = 'Please Enter a Valid Video URL')
            return

        for i in self.yt.streams.filter(type = "video"): self.resoultions.append(i.resolution)
        self.res_list = []
        [self.res_list.append(x) for x in self.resoultions if x not in self.res_list] 

        for i in self.res_list:
            if i not in self.rbtn_resoultions:
                self.res_list.remove(i)
        self.res_list.remove('144p')

        for resoultion in self.res_list:
            exec("self.rbtn_" + str(resoultion) +'.config(state = tk.NORMAL)')
        self.lbl_yt_title.config(text = str(self.yt.title))
        self.btn_download_video.config(state = tk.NORMAL)
        self.btn_download_audio.config(state = tk.NORMAL)

    def save_window(self):
        self.save_window = tk.Toplevel(self.master)
        self.save_window.geometry('400x150')
        self.icon = PhotoImage(file = resource_path("folder.png"))
        self.save_window.iconphoto(False, self.icon)
        self.save_window.geometry('400x120')
        self.save_window.resizable(False,False)
        self.save_window.title('Folder Select')

        self.save_window.transient(self.master)
        self.app1 = SaveDialouge(self.save_window)
        self.save_window.mainloop()

    def video_download(self):
        global filepath
        try:
            self.file_size = self.yt.streams.filter(resolution = (str(self.resoultion.get()))).first().filesize
        except:
            self.lbl_progress.config(text = "Download Status: Error, Please Ensure you have a valid URL")
            return

        for x in self.butons:
            x.config(state = tk.DISABLED)
        
        self.yt.streams.filter(resolution = (str(self.resoultion.get()))).first().download(str(filepath))


    def audio_download(self):
        global filepath
        self.file_size = self.yt.streams.filter(only_audio=True).first().filesize
        self.yt.streams.filter(only_audio=True).first().download( str(filepath), filename_prefix = 'Audio.')


    def start_download_video(self):
        global filepath
        threading.Thread(target=self.yt.register_on_progress_callback(self.progress_check)).start()
        threading.Thread(target=self.video_download).start()
        

    def start_download_audio(self):
        global filepath
        threading.Thread(target=self.yt.register_on_progress_callback(self.progress_check)).start()
        threading.Thread(target=self.audio_download).start()
        
        """Pop Up window for save location selection"""
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
        
    

    def set_default(self):
        self.path = os.path.expandvars(R"C:\Users\$USERNAME\Videos")
        self.ent_location.delete(0, tk.END)
        self.ent_location.insert(0,str(self.path))
    

    def confirm(self):
        global filepath
        self.path = self.ent_location.get()
        if os.path.isdir(self.path) == True:
            filepath = str(self.path)
        else:
            messagebox.showerror(title='Error', message='Please Select a Valid Save Location')
            return
        self.master.destroy()


def main(): 
    root = tk.Tk()
    icon = tk.PhotoImage(file = resource_path("icon.png"))
    root.title('Youtube Video Downloader')
    root.iconphoto(False, icon)

    root.geometry('400x460')
    app = MainApplication(root)
    root.mainloop()
    
main()
