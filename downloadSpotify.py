from requests_oauthlib import OAuth2Session
from spotifyApiFunctions import loginToSpotify, connectToSpotifyApi
import pandas as pd

client_id = '6080247b2e944437bb50ae10c713ef74'
client_secret = '4cc6643a79ac4422adbdfb2026fdbb02'
redirect_uri = 'https://localhost:8080/callback/'
scope=['user-library-read']
mySpotifyMail = ''
mySpotifyPassword = ''
apiCallUrl = 'https://api.spotify.com/v1/me/tracks?limit=50'

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize')
authorization_response = loginToSpotify(mySpotifyMail, mySpotifyPassword, authorization_url)
token = oauth.fetch_token('https://accounts.spotify.com/api/token', authorization_response=authorization_response,
                              client_secret=client_secret)

writer = pd.ExcelWriter('spotify_data.xlsx', engine='xlsxwriter')

totalDictSpotify = {'Song' : [], 'Album' : [], 'Artist' : []}

while apiCallUrl is not None:

    result, apiCallUrl = connectToSpotifyApi(apiCallUrl, oauth)

    for item in result['Song']:
        totalDictSpotify['Song'].append(item)
    for item in result['Album']:
        totalDictSpotify['Album'].append(item)
    for item in result['Artist']:
        totalDictSpotify['Artist'].append(item)

df = pd.DataFrame(totalDictSpotify)
df.to_excel(writer)
writer.save()





