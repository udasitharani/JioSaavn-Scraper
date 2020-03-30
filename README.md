# JioSaavn-Scraper
This is the source code of a bot that can fetch songs, playlists and albums data from JioSaavn. 
It has two parts- home_scraper.py and search_scraper.py

*home_scraper.py* fetches recommended songs, albums and playlists data from the home page in english as well as hindi languages.
<br/><br/><br/>


init_soup_english() - initializes the bot for fetching english song data
<br/><br/>

init_soup_hindi() - initializes the bot for fetching hindi song data
<br/><br/>

get_top_songs(num) - fetches the songs data from top songs section<br/>
    num-****required, int***<br/>
      the number of data items to be returned<br/>
    Returns a list of song data.<br/>
<br/>

get_new_releases(num) - fetches the albums data from new releases section<br/>
    num-****required, int***<br/>
      the number of data items to be returned<br/>
    Returns a list of albums data.<br/>
<br/>

get_featured_playlists(num) - fetches the playlists data from featured playlists section<br/>
    num-****required, int***<br/>
      the number of data items to be returned<br/>
    Returns a list of playlists data.<br/>
<br/>

Remaining functions are internal functions that are used by the functions mentioned above.<br/>
<br/><br/>



*search_scraper.py* fetches search results in the all formats - songs, albums, playlists.<br/>
<br/>

search_songs(keyword, num) - fetches the search results matching songs data<br/>
    *keyword*-****required, string***<br/>
      the search term<br/>
    num-****required, int***<br/>
      the number of data items to be returned<br/>
    Returns a list of songs data items.<br/>
<br/>

search_albums(keyword, num) - fetches the search results matching albums data<br/>
    *keyword*-****required, string***<br/>
      the search term<br/>
    num-****required, int***<br/>
      the number of data items to be returned<br/>
    Returns a list of albums data items.<br/>
<br/>

search_playlists(keyword, num) - fetches the search results matching playlists data<br/>
    *keyword*-****required, string***<br/>
      the search term<br/>
    num-****required, int***<br/>
      the number of data items to be returned<br/>
    Returns a list of playlists data items.<br/>
<br/>

Remaining functions are internal functions that are used by the functions mentioned above.
