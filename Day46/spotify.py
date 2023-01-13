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


# spotify2.get_auth_response()
# print(spotify2.get_cached_token())
print(spotify1.current_user()['id'])

