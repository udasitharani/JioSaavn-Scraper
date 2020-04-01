# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

BASE_URL = "https://www.jiosaavn.com"
HOME_URL = "/"
ENGLISH_HOME_URL = "english/"
HINDI_HOME_URL = "hindi/"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
home_soup=None
new_releases_soup = None
featured_playlists_soup = None
top_songs_soup = None

def fetch(category, count, language):
    try:
        if(language=="english"):
            init_soup_english()
        else:
            init_soup_hindi()
        if(category=="playlists"):
            return get_featured_playlists(int(count))
        elif(category=='albums'):
            return get_new_releases(int(count))
        else:
            return get_top_songs(int(count))
    except:
        return None

def init_soup_hindi():
    global header, home_soup, new_releases_soup, featured_playlists_soup, top_songs_soup, BASE_URL, HOME_URL, HINDI_HOME_URL
    try:
        response = requests.get(BASE_URL + HOME_URL + HINDI_HOME_URL, headers=header)
        home_soup = BeautifulSoup(response.content, "html.parser")
        new_releases_soup = home_soup.find('section', {'id': 'new-releases'})
        featured_playlists_soup = home_soup.find('section', {'id': 'featured'}).find('div', {'id': 'featured-playlists'})
        top_songs_soup = home_soup.find('section', {'id': 'top-15'})
    except:
        return None

def init_soup_english():
    global header, home_soup, new_releases_soup, featured_playlists_soup, top_songs_soup, BASE_URL, HOME_URL, ENGLISH_HOME_URL
    try:
        response = requests.get(BASE_URL + HOME_URL + ENGLISH_HOME_URL, headers=header)
        home_soup = BeautifulSoup(response.content, "html.parser")
        new_releases_soup = home_soup.find('section', {'id': 'new-releases'})
        featured_playlists_soup = home_soup.find('section', {'id': 'featured'}).find('div', {'id': 'featured-playlists'})
        top_songs_soup = home_soup.find('section', {'id': 'top-15'})
    except:
        return None

# Get Weekly Top Songs
def get_top_songs(num):
    global top_songs_soup, header
    songs = {}
    try:
        songs_soup = top_songs_soup.find('ol', {'class': 'chart-list highlight-first'})
        containers = songs_soup.select('li')
        count = len(containers)
        if(num<count):
            count = num
        for i in range(count):
            url  = containers[i].find('a')['href']
            res = requests.get(url, headers=header)
            item_soup = BeautifulSoup(res.content, 'html.parser')
            songs[i] = read_song_details(item_soup, url)
    except:
        return None
    return songs

# Get new albums 
def get_new_releases(num):
    global new_releases_soup
    releases = {}
    try:
        containers = new_releases_soup.select('div.album-item')
        count = len(containers)
        if(num<count):
            count = num
        for i in range(count):
            url  = containers[i].find('a')['href']
            releases[i] = read_album(containers[i], url)
    except:
        return None
    return releases

#Extract data from the song tiles
def read_album(tile, url):
    global header
    details = {}
    try:
        details['url'] = url
        res = requests.get(details['url'], headers=header)
        soup = BeautifulSoup(res.content, 'html.parser')
        details['thumbnail'] = soup.find('div', {'class': 'art solo-art'}).find('img')['src']
        details['title'] =  ' '.join(soup.find('h1', {'class': 'page-title'}).text.split())
        details['artist'] = ' '.join(soup.find('h2', {'class': 'page-subtitle'}).find('a').text.split())
        literals = soup.find('h2', {'class': 'page-subtitle'}).text.split()
        details['duration'] = literals[-1]
        details['songs'] = get_songs(soup)
    except:
        return None
    return details

# Get featured releases
def get_featured_playlists(num):
    global featured_playlists_soup
    playlists = {}
    try:
        containers = featured_playlists_soup.select('div.album-item')
        count = len(containers)
        if(num<count):
            count = num
        for i in range(count):
            url = containers[i].find('a')['href']
            thumbnail = containers[i].find('div', {'class': 'album art'}).find('img')['src']
            playlists[i] = read_playlist(containers[i], url, thumbnail)
    except:
        return None
    return playlists
    

# Extract data from the playlist tiles
def read_playlist(tile, url, thumbnail):
    global header
    details = {}
    try:
        res = requests.get(url, headers=header)
        soup = BeautifulSoup(res.content, 'html.parser')
        f = open('temp.html', 'w')
        f.write(str(soup))
        details['thumbnail'] = thumbnail
        details['title'] =  ' '.join(soup.find('h1', {'class': 'page-title'}).text.split())
        literals = soup.find('h2', {'class': 'page-subtitle'}).text.split()
        details['duration'] = literals[-1]
        details['songs'] = get_songs(soup)
    except:
        return None    
    return details

        
def get_songs(soup):
    global header
    songs = {}
    try:
        count = 0
        for item in soup.select('li:not(.hide).song-wrap'):
            url=item.find('span', {'class': 'title'}).find('a')['href']
            res = requests.get(url, headers = header)
            item_soup = BeautifulSoup(res.content, 'html.parser')        
            songs[count] = read_song_details(item_soup, url)
            count += 1
    except:
        return None
    return songs

def read_song_details(soup, url):
    song = {}
    try:
        song['url'] = url
        song['thumbnail'] = soup.find('div', {'class': 'solo-art'}).find('img')['src']
        song['title'] = ' '.join(soup.find('h1', {'class': 'page-title'}).text.split())
        song['lyrics'] = read_song_lyrics(soup)
        literals = soup.find('h2', {'class': 'page-subtitle'}).text.split()
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
    global header
    try:
        url = soup.find('div', {'class': 'page-group lyrics basic-copy top'}).find('a', {'class': 'btn light outline'})['href']
    except:
        return "N/A"
    try:
        res = requests.get(url, headers=header)
        soup = BeautifulSoup(res.content, 'html.parser')
        lyrics = str(soup.find('p', {'class': 'lyrics'}))
        lyrics = lyrics[lyrics.index('>')+1:lyrics.index('</p>')]
        while('<br/>' in lyrics):
            lyrics = lyrics[:lyrics.index('<br/>')] + '\n' + lyrics[lyrics.index('<br/>')+5:]
    except:
        return None
    return lyrics