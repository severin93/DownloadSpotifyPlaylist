from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


def loginToSpotify(mail, haslo, authorization_url):

    browser = webdriver.Chrome()
    browser.get(authorization_url)
    zaloguj_sie = browser.find_element_by_class_name('btn')
    zaloguj_sie.send_keys(Keys.ENTER)
    login = browser.find_element_by_id('login-username')
    password = browser.find_element_by_id('login-password')
    login.send_keys(mail)
    password.send_keys(haslo)
    zaloguj_sie_spotify = browser.find_element_by_class_name('btn-green')
    zaloguj_sie_spotify.send_keys(Keys.ENTER)
    time.sleep(1)
    authorization_response = browser.current_url

    return authorization_response

def connectToSpotifyApi(apiUrl, oauth):

    dictSpotify = {'Song' : [], 'Album' : [], 'Artist' : []}

    r = oauth.get(apiUrl)
    result = json.loads(r.text)
    for item in result['items']:

        songName = item['track']['name']
        dictSpotify['Song'].append(songName)

        albumName = item['track']['album']['name']
        dictSpotify['Album'].append(albumName)

        for artist in item['track']['artists']:
            artistNames = []
            artistName = artist['name']
            artistNames.append(artistName)

        dictSpotify['Artist'].append(' '.join(artistNames))

    return dictSpotify, result['next']

