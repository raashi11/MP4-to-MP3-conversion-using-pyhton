import tkinter as tk
import glob
import os


root = tk.Tk()

label = tk.Label(root, text="Choose the mp4 to get the audio from")
label.pack()

lst = tk.Listbox(root)
lst.pack()

def add_to_entry(event):
	n = lst.curselection()
	item = lst.get(n)
	v.set(item)

def get_audio():
	string = f"ffmpeg -i {entry.get()} -f mp3 -ab 192000 -vn audio.mp3"
	os.system(string)
	os.startfile("audio.mp3")


for f in glob.glob("*.mp4"):
	lst.insert(tk.END, f)
lst.bind("<Double-Button>", add_to_entry)

v = tk.StringVar()
entry = tk.Entry(root, textvariable=v)
entry.pack()

button = tk.Button(root, text="Get audio", command=get_audio)
button.pack()

root.mainloop()