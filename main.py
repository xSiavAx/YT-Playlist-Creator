from ytmusicapi import YTMusic
from datetime import datetime

def main():
	playlist_name = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

	ytmusic = YTMusic('headers_auth.json')

	songs = ytmusic.get_library_songs(limit=10000)

	song_ids = list(map(lambda x: x['videoId'], songs))

	playlist = ytmusic.create_playlist(playlist_name, "Automatically created playlist")

	ytmusic.add_playlist_items(playlist, song_ids)


if __name__ == "__main__":
    main()