def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()
def pause_music():
    mixer.music.pause()
