import pandas as pd
import numpy as np

from downloadingMP3 import downloadSongs

file = pd.read_excel('spotify_data.xlsx')

artist_names = file['Artist']

song_names = file['Song']

totalList = []

for song, artist in zip(song_names, artist_names):
    totalList.append(song + ' ' + artist)

downloadSongs(totalList)


