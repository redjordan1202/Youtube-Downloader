# Youtube-Downloader
Python based GUI Youtube video downloader.
Supports downloading Videos and Audio up to 4k resolutions.

Background:
This is my first major project using Python. It stemmed from looking at a list of common beginner projects. I originally created a command line version of this program that had the same functionality. But it was a little clunky to use and command line programs never seem as impressive to me. So I looked into creating a project with a GUI and found Tkinter. Using Tkinter together with PyTube I was able to create what I think is a pretty solid first Python GUI program. 

How to use:
-Enter a YouTube Video URL in the space provided
-Click the Select Video button to pull video info including title and available resolutions
-Select a download location
    -If you do not select a download location the file will be saved to your Videos folder of the current user
-Select a resolution. Note the resolution you select will not affect audio quality.
-Click on either the Video or Audio download button. Your download will start and the progress bar will update with the current progress.

Known Issues:
Pytube, the library used to download youtube videos, is currently bugged. Most likely due to a recent change at how Youtube handles request to their server. 
I am currently working on a rewrite of this project using a different library to handle video downloads. ETA for completion on that is unknown.
