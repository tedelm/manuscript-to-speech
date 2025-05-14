import subprocess
import os
import glob

# Ensure the audio directory exists
os.makedirs("audio", exist_ok=True)

# Get all mp3 files and sort them by their numerical order
audio_files = sorted(glob.glob("audio/dialog_*.mp3"))

if not audio_files:
    print("No audio files found in the audio directory!")
    exit(1)

# Create the concat string for ffmpeg
concat_string = "|".join(audio_files)
combined_path = "audio/combined.mp3"

# Combine the audio files using ffmpeg
subprocess.run([
    "ffmpeg",
    "-i", f"concat:{concat_string}",
    "-c", "copy",
    combined_path
], check=True)

print(f"Combined audio file created at: {combined_path}")