import sys
import spotipy
import spotipy.util as util
import pickle

# name = "joe"
# print(name)

# pickle.dump(name, open("name.dat", "wb"))

name = "bob"
print(name)

name = pickle.load(open("name.dat", "rb"))
print(name)