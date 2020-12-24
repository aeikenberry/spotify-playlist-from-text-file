# Spotify Playlists from text file

## Example

`python playlist_from_list.py -f path-to-file.txt -p "My sick playlist"`

## Instructions
1. Setup a Spotify app (https://developer.spotify.com/).
2. Get your ID/Secret.
3. Create a redirect_uri: `http://localhost:8000`
4. set you env vars:
`SPOTIFY_CLIENT_ID`
`SPOTIFY_CLIENT_SECRET`
5. Run the script
6. Follow the instructions to do Oauth in the browser on first run.
7. Paste the full url you're redirected to.
8. It will cache your auth in a `.cache` file
