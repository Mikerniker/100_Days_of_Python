import spotipy
from main import all_songs, year_to_travel

CLIENT_ID = "ADD_CLIENT_ID"
CLIENT_SECRET = "ADD_CLIENT_SECRET"
REDIRECT_URI = "http://example.com"
ACCESS_TOKEN = "ADD_ACCESS_TOKEN"


spotify1 = spotipy.client.Spotify(auth=ACCESS_TOKEN,
                                  requests_session=True)

spotify2 = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,
                                       client_secret=CLIENT_SECRET,
                                       redirect_uri=REDIRECT_URI,
                                       scope="playlist-modify-private",
                                       requests_session=True,
                                       cache_path="token.txt")

#STEP2: Authentication with Spotify

# spotify2.get_auth_response()
# print(spotify2.get_cached_token())
spotify2.refresh_access_token("ADD_REFRESH_TOKEN")
print(spotify1.current_user()['id'])

#STEP 3: Search Spotify for Songs

playlist = []
for song in all_songs:
    song_tracks = spotify1.search(f"track: {song} year: {year_to_travel}", limit=1, type='track')
    try:
        song_uri = song_tracks['tracks']['items'][0]['uri']
        playlist.append(song_uri)
    except IndexError:
        print("The song is not available")
        continue
print(playlist)

#STEP 4: Create a playlist and add to it

playlist_id = spotify1.user_playlist_create(user=user_id,
                              name=f"{year_to_travel} Billboard 100",
                              public=False,
                              description="music memory lane")['id']

print(spotify1.playlist_add_items(playlist_id=playlist_id, items=playlist))