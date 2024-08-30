import tkinter as tk
import genius_revamped


def on_submit():
    artist = artist_entry.get()
    song = song_entry.get()
    lyrics = genius_revamped.get_lyrics(song, artist)

    lyrics_text.delete(1.0, tk.END)  # Clear previous text
    if lyrics:
        lyrics_text.insert(tk.END, lyrics)
    else:
        lyrics_text.insert(tk.END, "Lyrics not found or error occurred.")


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
