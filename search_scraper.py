import requests, json
from bs4 import BeautifulSoup
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

BASE_URL = "https://www.jiosaavn.com/search"
SONGS_URL = "/"
ALBUMS_URL = "/album/"
PLAYLISTS_URL = "/playlist/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# Base method
def search(keyword, category, count):
    if(category=="playlist"):
        return search_playlists(keyword, int(count))
    elif(category=="album"):
        return search_albums(keyword, int(count))
    else:
        return search_songs(keyword, int(count))


# Search for songs
def search_songs(keyword, num):
    global HEADERS, BASE_URL, SONGS_URL
    url = BASE_URL+SONGS_URL+keyword
    songs = {}
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        songs = scrape_songs(soup, num)
    except:
        return None
    return songs

#Scraping to get the list of songs in search result
def scrape_songs(soup, num):
    global HEADERS
    songs = {}
    try:
        songs_soup = soup.find('ol', {'class': 'track-list song-search no-index'})
        containers = songs_soup.select('li.song-wrap')
        count = len(containers)
        if(num<count):
            count = num
        for i in range(count):
            url  = containers[i].find('div', {'class': 'main'}).find('a')['href']
            res = requests.get(url, headers=HEADERS)
            item_soup = BeautifulSoup(res.content, 'html.parser')
            song = read_song_details(item_soup, url)
            songs[i] = song
    except:
        return None
    return songs

# Search for albums
def search_albums(keyword, num):
    global HEADERS, BASE_URL, ALBUMS_URL
    url = BASE_URL+ALBUMS_URL+keyword
    albums = {}
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        albums = scrape_albums(soup, num)
    except:
        return None
    return albums
    

# Scraping to get list of albums in search result
def scrape_albums(soup, num):
    global HEADERS
    albums = {}
    try:
        albums_soup = soup.find('ol', {'class': 'grid-list albums'})
        containers = albums_soup.select('li')
        count = len(containers)
        if(num<count):
            count = num
        for i in range(count):
            url  = containers[i].find('div', {'class': 'art album-art'}).find('a')['href']
            album = read_album(containers[i], url)
            albums[i] = album
    except:
        return None
    return albums

#Extract data from the song tiles
def read_album(tile, url):
    global HEADERS
    details = {}
    details['url'] = url
    res = requests.get(details['url'], headers=HEADERS)
    soup = BeautifulSoup(res.content, 'html.parser')
    f = open('temp.html', 'w')
    f.write(str(soup))
    details['thumbnail'] = soup.find('div', {'class': 'art solo-art'}).find('img')['src']
    details['title'] =  ' '.join(soup.find('h1', {'class': 'page-title'}).text.split())
    details['artist'] = ' '.join(soup.find('h2', {'class': 'page-subtitle'}).find('a').text.split())
    literals = soup.find('h2', {'class': 'page-subtitle'}).text.split()
    details['duration'] = literals[-1]
    details['songs'] = get_songs(soup)
    return details

# Search for albums
def search_playlists(keyword, num):
    global HEADERS, BASE_URL, PLAYLISTS_URL
    url = BASE_URL+PLAYLISTS_URL+keyword
    playlists = {}
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        playlists = scrape_playlists(soup, num)
    except:
        return None
    return playlists
    

# Scraping to get list of albums in search result
def scrape_playlists(soup, num):
    global HEADERS
    playlists = {}
    playlists_soup = soup.find('ul', {'class': 'playlist-list'})
    containers = playlists_soup.select('li.playlist-result')
    count = len(containers)
    if(num<count):
        count = num
    for i in range(count):
        url  = containers[i].find('div', {'class': 'playlist-meta'}).find('a')['href']
        thumbnail = containers[i].find('div', {'class': 'art solo-art'}).find('img')['src']
        playlist = read_playlist(containers[i], url, thumbnail)
        playlists[i] = playlist
    return playlists

# Extract data from the playlist tiles
def read_playlist(tile, url, thumbnail):
    global HEADERS
    details = {}
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.content, 'html.parser')
    details['thumbnail'] = thumbnail
    details['title'] =  ' '.join(soup.find('h1', {'class': 'page-title'}).text.split())
    literals = soup.find('h2', {'class': 'page-subtitle'}).text.split()
    details['duration'] = literals[-1]
    details['songs'] = get_songs(soup)
    return details

# Getting songs from a list of songs
def get_songs(soup):
    global HEADERS
    songs = {}
    try:
        count = 0
        for item in soup.select('li:not(.hide).song-wrap'):
            url=item.find('span', {'class': 'title'}).find('a')['href']
            res = requests.get(url, headers = HEADERS)
            item_soup = BeautifulSoup(res.content, 'html.parser')
            songs[count] = read_song_details(item_soup, url)
            count+=1
    except:
        return None
    return songs

# Getting song details
def read_song_details(soup, url):
    song = {}
    try:
        literals = soup.find('h2', {'class': 'page-subtitle'}).text.split()
        song['url'] = url
        song['thumbnail'] = soup.find('div', {'class': 'solo-art'}).find('img')['src']
        song['title'] = ' '.join(soup.find('h1', {'class': 'page-title'}).text.split())
        song['lyrics'] = read_song_lyrics(soup)
        song['album'] = ' '.join(literals[:literals.index('by')])
        song['duration'] = literals[-1]
        artists = literals[literals.index('by')+1:literals.index('·')]
        artists[-1] = artists[-1]+','
        i = 0
        a = ''
        song['artists'] = []
        while(i<len(artists)):
            a += ' '+artists[i]
            if(a[-1]==','):
                a = a[:-1]
                song['artists'].append(a.strip())
                a = ''
            i+=1
    except:
        return None
    return song

# Reading the lyrics of songs
def read_song_lyrics(soup):
    global HEADERS
    try:
        url = soup.find('div', {'class': 'page-group lyrics basic-copy top'}).find('a', {'class': 'btn light outline'})['href']
    except:
        return "N/A"
    try:
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.content, 'html.parser')
        lyrics = str(soup.find('p', {'class': 'lyrics'}))
        lyrics = lyrics[lyrics.index('>')+1:lyrics.index('</p>')]
        while('<br/>' in lyrics):
            lyrics = lyrics[:lyrics.index('<br/>')] + '\n' + lyrics[lyrics.index('<br/>')+5:]
    except:
        return None
    return lyrics    
