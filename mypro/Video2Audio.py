import imageio
imageio.plugins.ffmpeg.download()
import moviepy.editor
video = moviepy.editor.VideoFileClip(r"D:\Alan Walker - Faded(1080P_HD).mp4")
audio = video.audio
audio.write_audiofile(r"E:\Faded_myConvert.mp3")
print ('converted successfully')