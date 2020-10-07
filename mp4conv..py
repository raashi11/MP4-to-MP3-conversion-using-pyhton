import moviepy.editor as mpe
file = mpe.VideoFileClip("video.mp4")
file.audio.write_audiofile("video.mp3")
