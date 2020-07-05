import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read,user-read-playback-state,user-modify-playback-state'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)


if token:
    sp = spotipy.Spotify(auth=token)
    sp.pause_playback()
else:
    print("Can't get token for", username)