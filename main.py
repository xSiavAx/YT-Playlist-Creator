from ytmusicapi import YTMusic
from datetime import datetime

def main():
    print('Initializing...')
    playlist_name = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    ytmusic = YTMusic('headers_auth.json')

    print('Retrieving songs...')
    songs = ytmusic.get_library_songs(limit=10000)

    song_ids = list(map(lambda x: x['videoId'], songs))

    print('Creating playlist...')
    playlist = ytmusic.create_playlist(playlist_name, 'Automatically created playlist')

    print('Adding songs to playlist...')
    ytmusic.add_playlist_items(playlist, song_ids)
    print('Done.')


if __name__ == '__main__':
    main()
