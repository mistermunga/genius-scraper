import genius_revamped
import os
import constants

invalid_characters = [ "<", ">", ":", r'"', "/", '\\', "|", "?", "*", " "]


def cleanup(text: str) -> str:
    text = r"{}".format(text)
    for char in text:
        if char in invalid_characters:
            text = text.replace(char, "_")

    return text


def write_lyrics_to_file(song, artist):
    lyrics = genius_revamped.get_lyrics(song, artist)

    if not lyrics:
        print('No lyrics found')
        return False

    filename = f"{cleanup(song)}-{cleanup(artist)}.txt"
    fullpath = os.path.join(constants.resources_path, filename)

    with open(fullpath, 'w') as f:
        f.write(lyrics)
    print(f"Lyrics saved to {fullpath}")
    return True


def main():
    song_name = input("Song Name: ")
    artist_name = input("Artist: ")
    write_lyrics_to_file(song_name, artist_name)


if __name__ == '__main__':
    main()
