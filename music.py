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

