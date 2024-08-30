"""file-name = genius_revamped.py"""

import requests
import constants
from bs4 import BeautifulSoup

base_url = 'http://api.genius.com'
headers = {'Authorization': f"Bearer {constants.my_token}"}

artist_name = "Boy Harsher"
song_title = "Pain"


def lyrics_from_song_api_path(song_api_path):
    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)
    response.raise_for_status()
    json_data = response.json()
    path = json_data['response']['song']['path']

    # Regular HTML scraping
    page_url = 'http://genius.com' + path
    page = requests.get(page_url)
    page.raise_for_status()
    html = BeautifulSoup(page.text, 'html.parser')

    lyrics = None

    for div in html.find_all("div", class_=lambda x: x and "Lyrics__Container" in x):
        lyrics = div.get_text(separator='\n').encode('ascii', 'ignore').decode()
        if lyrics:
            break

    if not lyrics:
        raise ValueError("Lyrics not found on the page.")

    return lyrics


def get_artist_id(artist_name):
    search_url = f"{base_url}/search"
    params = {'q': artist_name}
    response = requests.get(search_url, params=params, headers=headers)
    response.raise_for_status()
    json_data = response.json()

    for hit in json_data['response']['hits']:
        if hit['result']['primary_artist']['name'].lower() == artist_name.lower():
            return hit['result']['primary_artist']['id']

    return None


def get_songs_by_artist(artist_id):
    artist_songs_url = f"{base_url}/artists/{artist_id}/songs"
    params = {'per_page': 50}  # Adjust 'per_page' to retrieve more songs if needed
    response = requests.get(artist_songs_url, params=params, headers=headers)
    response.raise_for_status()
    json_data = response.json()

    return json_data['response']['songs']


if __name__ == '__main__':
    artist_id = get_artist_id(artist_name)

    if not artist_id:
        print(f"Artist '{artist_name}' not found.")
    else:
        songs = get_songs_by_artist(artist_id)
        song_info = None

        for song in songs:
            if song['title'].lower() == song_title.lower():
                song_info = song
                break

        if song_info:
            print(f"\nSelected song: {song_info['full_title']}")
            try:
                lyrics = lyrics_from_song_api_path(song_info['api_path'])
                print(f"\nLyrics:\n{lyrics}")
            except ValueError as e:
                print(str(e))
        else:
            print(f"Song '{song_title}' by '{artist_name}' not found.")
