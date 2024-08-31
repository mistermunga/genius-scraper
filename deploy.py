import genius_revamped
import streamlit as st


def generate(song, artist):
    return genius_revamped.get_lyrics(song, artist)

def main():
    st.title("Lyrics Getter")

    html_temp = """  
          <div style="background-color: #FFFF00; padding: 16px">
          </div>  
          """

    st.markdown(html_temp, unsafe_allow_html=True)

    song_title = st.text_input("Song Title: ", value="")
    artist_name = st.text_input("Artist Name: ", value="")
    lyrics = ""

    if st.button("generate"):
        lyrics = generate(song_title, artist_name)

    st.write(lyrics)


if __name__ == "__main__":
    main()
    