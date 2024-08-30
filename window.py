import tkinter as tk
import genius_revamped


def on_submit():
    artist = artist_entry.get()
    song = song_entry.get()
    lyrics = get_info(artist, song)
    if lyrics:
        lyrics_text.delete(1.0, tk.END)  # Clear previous text
        lyrics_text.insert(tk.END, lyrics)
    else:
        lyrics_text.delete(1.0, tk.END)  # Clear previous text
        lyrics_text.insert(tk.END, "Lyrics not found or error occurred.")


def get_info(artist_name, song_name):
    artistID = genius_revamped.get_artist_id(artist_name)

    if not artistID:
        return "Artist not found."
    else:
        songs = genius_revamped.get_songs_by_artist(artistID)
        song_info = None

        for song in songs:
            if song['title'].lower() == song_name.lower():
                song_info = song
                break

        if song_info:
            try:
                lyrics = genius_revamped.lyrics_from_song_api_path(song_info['api_path'])
                return lyrics
            except Exception as e:
                return f"An error occurred: {e}"
        else:
            return "Song not found."


window = tk.Tk()
window.title("Lyrics Getter")

tk.Label(window, text="Song Name").grid(row=0, column=0)
song_entry = tk.Entry(window)
song_entry.grid(row=0, column=1)

tk.Label(window, text="Artist Name").grid(row=1, column=0)
artist_entry = tk.Entry(window)
artist_entry.grid(row=1, column=1)

submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2)

lyrics_text = tk.Text(window, wrap='word', height=15, width=50)
lyrics_text.grid(row=3, column=0, columnspan=2)

window.mainloop()
