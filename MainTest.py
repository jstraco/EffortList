import sys
import spotipy
import spotipy.util as util
from time import sleep

userID = "aaa766fda37f45d79aa39e91b383773d"
userSecret = "6ece276dd4f84473b4f806234c3cc849"
redirectURL = "http://localhost:7777/callback"
scope = 'user-library-read,user-read-playback-state,user-modify-playback-state'
temp = 1
# Test for valid input
"""
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()
"""
username = "jstraco"
# Creates token of permitions
token = util.prompt_for_user_token(username, scope, userID, userSecret, redirectURL)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
    sys.exit()

# Main Loop
done = False
isPlaying = False
while not done:
    sleep(1)
    if isPlaying:
        print("Playback has started")
        currentSong = sp.current_playback()['item']['name']
        print(currentSong)
        while isPlaying:
            if sp.current_playback()['item']['name'] != currentSong:
                currentSong = sp.current_playback()['item']['name']
                print(currentSong)
            isPlaying = sp.current_playback()['is_playing']
            if not isPlaying:
                print("                 Playback has stoped")

    isPlaying = sp.current_playback()['is_playing']
#e