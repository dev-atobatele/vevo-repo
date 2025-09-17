from moviepy import *

# Load image / gif / video and audio
video = VideoFileClip(r"C:\path_to_image_or_video.mp4")
audio = AudioFileClip(r"C:\path_to_audio.mp3")

# Calculate how many times to repeat the video
num_loops = int(audio.duration // video.duration) + 1

# Repeat the video
video_loops = [video] * num_loops
looped_video = concatenate_videoclips(video_loops)

# Trim to match audio duration
final_clip = looped_video.subclipped(0, audio.duration).with_audio(audio)

# Export the final video to the current directory, or add the full path for another one
final_clip.write_videofile("output_video.mp4")



# To ensure audio quality, add audio_bitrate='' or audio_codec='', eg. final_clip.write_videofile("video_name.mp4", audio_bitrate="320k", audio_codec="mp3").

# audio_bitrate = "320k" or lower for mp3 codec. The default value is 128k for mp3s. The other codecs listed determine the bitrate.

# audio_codec = "flac" (16-bit only), "pcm_s16le" (16-bit WAV), "pcm_s24le" (24-bit WAV), "pcm_s32le" (32-bit WAV). The default codec is "mp3".

# To ensure image / video quality, you can export the video as an .mov or .mkv file.