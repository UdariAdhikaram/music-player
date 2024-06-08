from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from pygame import mixer

# Color codes
co1 = "#ffffff"
co2 = "#3C1DC6"
co3 = "#333333"
co4 = "#CFC7F8"
co5 = "#000000"

# Initialize pygame mixer
mixer.init()

# Create the main window
window = Tk()
window.title("")
window.geometry("800x600")
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

# Global lists
songs = []
favorite_songs = []

# Event functions
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = (index + 1) % len(songs)
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = (index - 1) % len(songs)
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def add_music():
    files = filedialog.askopenfilenames(initialdir='/', title='Select Music Files', filetypes=(('MP3 Files', '*.mp3'), ('All Files', '*.*')))
    for file in files:
        songs.append(file)
        listbox.insert(END, os.path.basename(file))

def delete_music():
    selected_song = listbox.curselection()
    if selected_song:
        song = listbox.get(selected_song)
        listbox.delete(selected_song)
        songs.remove(song)
        if song in favorite_songs:
            favorite_songs.remove(song)
        if running_song['text'] == song:
            stop_music()
            running_song['text'] = "Choose a Song"

def add_favorite():
    selected_song = listbox.curselection()
    if selected_song:
        song = listbox.get(selected_song)
        if song not in favorite_songs:
            favorite_songs.append(song)

# Frames
left_frame = Frame(window, width=400, height=400, bg=co1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=400, height=200, bg=co3)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=800, height=400, bg=co4)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

# Right frame with listbox and scrollbar
listbox = Listbox(right_frame, selectmode=SINGLE, font=("Arial 12 bold"), width=42, height=18, bg=co3, fg=co1)
listbox.grid(row=0, column=0)

scrollbar = Scrollbar(right_frame)
scrollbar.grid(row=0, column=1, sticky='ns')

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Images and buttons
img_1 = Image.open('icons/5.jpg')
img_1 = img_1.resize((380, 380))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=400, image=img_1, bg=co1)
app_image.place(x=10, y=10)

img_3 = Image.open('icons/back.png')
img_3 = img_3.resize((40, 40))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, width=50, height=50, image=img_3, bg=co1, font=("Ivy 10"), command=prev_music)
prev_button.place(x=50, y=75)

img_2 = Image.open('icons/play.png')
img_2 = img_2.resize((40, 40))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, width=50, height=50, image=img_2, bg=co1, font=("Ivy 10"), command=play_music)
play_button.place(x=120, y=75)

img_4 = Image.open('icons/forward.png')
img_4 = img_4.resize((40, 40))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, width=50, height=50, image=img_4, bg=co1, font=("Ivy 10"), command=next_music)
next_button.place(x=190, y=75)

img_5 = Image.open('icons/pause.png')
img_5 = img_5.resize((40, 40))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, width=50, height=50, image=img_5, bg=co1, font=("Ivy 10"), command=pause_music)
pause_button.place(x=260, y=75)

img_6 = Image.open('icons/resume.png')
img_6 = img_6.resize((40, 40))
img_6 = ImageTk.PhotoImage(img_6)
resume_button = Button(down_frame, width=50, height=50, image=img_6, bg=co1, font=("Ivy 10"), command=resume_music)
resume_button.place(x=330, y=75)

img_7 = Image.open('icons/stop.png')
img_7 = img_7.resize((40, 40))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, width=50, height=50, image=img_7, bg=co1, font=("Ivy 10"), command=stop_music)
stop_button.place(x=400, y=75)

# Add music button
img_8 = Image.open('icons/addsong.png')
img_8 = img_8.resize((40, 40))
img_8 = ImageTk.PhotoImage(img_8)
add_music_button = Button(down_frame, image=img_8, width=50, height=50, bg=co1, font=("Ivy 10"), command=add_music)
add_music_button.place(x=470, y=75)

# Delete music button
img_9 = Image.open('icons/deletesong.png')
img_9 = img_9.resize((40, 40))
img_9 = ImageTk.PhotoImage(img_9)
delete_music_button = Button(down_frame, image=img_9, width=50, height=50, bg=co1, font=("Ivy 10"), command=delete_music)
delete_music_button.place(x=540, y=75)

# Add to favorite button
img_10 = Image.open('icons/favorite.png')
img_10 = img_10.resize((40, 40))
img_10 = ImageTk.PhotoImage(img_10)
favorite_button = Button(down_frame, image=img_10, width=50, height=50, bg=co1, font=("Ivy 10"), command=add_favorite)
favorite_button.place(x=610, y=75)

#line = Label(left_frame, width=200, height=1, padx=10, bg=co3)
#line.place(x=0, y=1)

#line = Label(left_frame, width=200, height=1, padx=10, bg=co1)
#line.place(x=0, y=3)

# Running song label
running_song = Label(down_frame, text="Choose a Song", font=("Ivy 16"), width=100, height=1, padx=10, bg=co1, fg=co5, anchor=NW)
running_song.place(x=0, y=1)

# Change directory to music folder and populate the listbox
os.chdir(r'E:\Research\research\musicsong')
songs = os.listdir()

def show():
    for song in songs:
        listbox.insert(END, song)

show()

# Start the main loop
window.mainloop()
