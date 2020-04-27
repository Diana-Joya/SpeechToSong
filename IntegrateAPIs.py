import requests
import spotipy
import spotipy.oauth2 as oauth2


def authenticate_genius():
    '''         GENIUS API Request          '''
    access_token = 'YOUR GENIUS ACCESS TOKEN HERE'
    base_url = 'https://api.genius.com'

    return access_token, base_url


def genius_request(query, access_token, base_url):
    song_query = query.replace(' ', '-')

    print('Genius call')
    params = {'q': song_query}
    token = 'Bearer {}'.format(access_token)
    headers = {'Authorization': token}

    path = 'search/'
    request_uri = base_url + '/' + path
    print(request_uri + song_query)

    get_song = requests.get(request_uri, params=params, headers=headers)
    json = get_song.json()

    popularity = 0
    most_popular = False
    for hit in json['response']['hits']:
        if 'pageviews' in hit['result']['stats']:
            if hit['result']['stats']['pageviews'] > popularity:
                popularity = hit['result']['stats']['pageviews']
                top_result = hit
                most_popular = True

    if most_popular:
        full_title = top_result["result"]["full_title"]
        song_title = top_result["result"]["title"]
        song_id = top_result["result"]["id"]
        artist = top_result["result"]["primary_artist"]["name"]
    else:
        full_title = json["response"]["hits"][0]["result"]["full_title"]
        song_title = json["response"]["hits"][0]["result"]["title"]
        song_id = json["response"]["hits"][0]["result"]["id"]
        artist = json["response"]["hits"][0]["result"]["primary_artist"]["name"]

    print('Your search returned: ', full_title, "\nSong ID: ", song_id, "\nArtist: ", artist, "\nSong Title: ", song_title)
    return artist, song_title


def authenticate_spotify():
    '''         Spotify API Request          '''

    credentials = oauth2.SpotifyClientCredentials(
        client_id='YOUR SPOTIFY CLIENT ID HERE',
        client_secret='YOUR SPOTIFY CLIENT SECRET HERE')

    sp_token = credentials.get_access_token()

    return sp_token


def spotify_request(artist, song_title, token):
    print('\nSpotify call')
    print(song_title)
    sp = spotipy.Spotify(token)

    results = sp.search(q=artist, limit=50)
    print(results)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
        song_check = normalize_str(song_title)
        track_check = normalize_str(track['name'])
        if track_check == song_check or song_check in track_check:
            if "Alexander Hamilton - Instrumental" == track['name']:
                continue
            else:
                print('track    : ' + track['name'])
                if track['preview_url']:
                    print('audio    : ' + track['preview_url'])
                if track['album']:
                   print('cover art: ' + track['album']['images'][0]['url'])
                return track
    return None


def normalize_str(str):
    str = str.strip()
    str = str.replace('​', '', 1)
    str = str.replace('’', '')
    str = str.replace('\'', '')
    str = str.replace('-', '')
    return str
