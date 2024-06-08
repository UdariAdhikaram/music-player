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

