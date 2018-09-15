import operator

from requests_oauthlib import OAuth2Session
from api_functions import get_result_from_api_call
import pandas as pd
import pprint

client_id = '6080247b2e944437bb50ae10c713ef74'
client_secret = '4cc6643a79ac4422adbdfb2026fdbb02'
redirect_uri = 'https://localhost:8080/callback/'
scope = ['user-library-read']

all_songs = []

def connect_to_spotify_api():
    global oauth
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize')
    print('Please go to: {} and authorize access:'.format(authorization_url))
    authorization_response = input("Enter full callback URL")
    token = oauth.fetch_token(token_url='https://accounts.spotify.com/api/token',
                              authorization_response=authorization_response,
                              client_secret=client_secret)


def get_songs():
    apiCallUrl = 'https://api.spotify.com/v1/me/tracks?limit=50'
    while apiCallUrl is not None:
        result, apiCallUrl = get_result_from_api_call(apiCallUrl, oauth)
        for song, album, artist in zip(result['Song'], result['Album'], result['Artist']):
            all_songs.append(dict(song=song, album=album, artist=artist))
    pprint.pprint(all_songs)




if __name__ == '__main__':
    connect_to_spotify_api()
    get_songs()
    df = pd.DataFrame(all_songs)
    df.to_csv(path_or_buf='./songs.csv')

