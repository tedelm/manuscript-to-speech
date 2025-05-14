pip3 install pydub
pip3 install gtts
pip3 install edge-tts


#Download and install ffmpeg:
# powershell: winget install ffmpeg
#Go to the official ffmpeg download page. https://ffmpeg.org/download.html / https://www.gyan.dev/ffmpeg/builds/

#For Windows, you can use a pre-built binary from gyan.dev.
#Download the "release full" zip file, extract it, and note the path to the bin folder (it contains ffmpeg.exe).
#Add ffmpeg to your system PATH:
#Open the Start menu, search for "Environment Variables", and open "Edit the system environment variables".
#Click "Environment Variables".
#Under "System variables", find and select the "Path" variable, then click "Edit".
#Click "New" and add the path to the bin folder you extracted (e.g., C:\ffmpeg\bin).
#Click OK to close all dialogs.
#Restart your terminal or IDE to ensure the new PATH is recognized.
#Verify installation:
#Open a new terminal and run:
 ffmpeg -version
 