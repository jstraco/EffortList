import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read,user-read-playback-state,user-modify-playback-state'

if len(sys.argv) > 2:
    username = sys.argv[1]
    volume = sys.argv[2]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)


if token:
    sp = spotipy.Spotify(auth=token)
    sp.volume(int(sys.argv[2]))
else:
    print("Can't get token for", username)