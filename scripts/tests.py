import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

cl_id = '66dded11300a4c5a9d565000fa13d8c8'
cl_sec = '1b74966ace0a4560bd7164f323a1afa6'
username = 'antonstorozhilov'
redirect_uri = 'http://localhost'
#client_credentials_manager = SpotifyClientCredentials(client_id='66dded11300a4c5a9d565000fa13d8c8', client_secret='1b74966ace0a4560bd7164f323a1afa6')



scope = 'user-read-currently-playing'
# scope = 'user-read-playback-state'
# works as well

token = util.prompt_for_user_token(username, scope, client_id=cl_id, client_secret=cl_sec, redirect_uri=redirect_uri)
                                   #redirect_uri=redirect_uri)

spotify = spotipy.Spotify(auth=token)
current_track = spotify.current_user_playing_track()

print(current_track)
