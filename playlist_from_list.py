import argparse
import datetime
import logging
import os
import re

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

logger = logging.getLogger("examples.add_tracks_to_playlist")
logging.basicConfig(level="DEBUG")
scope = "playlist-modify-public"

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_args():
    parser = argparse.ArgumentParser(description="Adds track to user playlist")
    parser.add_argument(
        "-f", "--file", help="File with list of searches", default='tonedeaf.txt'
    )
    parser.add_argument(
        "-p", "--playlist", help="playlist name to create", default='debug_create_' + str(datetime.datetime.now())
    )
    return parser.parse_args()


def main():
    args = get_args()

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            scope=scope,
            open_browser=False,
            redirect_uri="http://localhost:8000",
        )
    )
    items = []
    with open(args.file, "rb") as f:
        lines = f.readlines()
        for line in lines:
            result = sp.search(re.sub(r'[^A-Za-z0-9 ]+', ' ', line.decode('utf-8')))
            items += [track['id'] for track in result['tracks']['items']]
   
    playlist = sp.user_playlist_create(sp.current_user()['id'], args.playlist)
    for chunk in chunks(items, 100):
        sp.playlist_add_items(playlist['id'], chunk)


if __name__ == "__main__":
    main()
