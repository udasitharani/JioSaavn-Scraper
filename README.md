# JioSaavn-Scraper
This is the source code of a bot that can fetch songs, playlists and albums data from JioSaavn. 
It has two parts- home_scraper.py and search_scraper.py

*home_scraper.py* fetches recommended songs, albums and playlists data from the home page in english as well as hindi languages.



init_soup_english() - initializes the bot for fetching english song data


init_soup_hindi() - initializes the bot for fetching hindi song data


get_top_songs(num) - fetches the songs data from top songs section
    num-****required, int***
      the number of data items to be returned
    Returns a list of song data.


get_new_releases(num) - fetches the albums data from new releases section
    num-****required, int***
      the number of data items to be returned
    Returns a list of albums data.


get_featured_playlists(num) - fetches the playlists data from featured playlists section
    num-****required, int***
      the number of data items to be returned
    Returns a list of playlists data.


Remaining functions are internal functions that are used by the functions mentioned above.





*search_scraper.py* fetches search results in the all formats - songs, albums, playlists.


search_songs(keyword, num) - fetches the search results matching songs data
    *keyword*-****required, string***
      the search term
    num-****required, int***
      the number of data items to be returned
    Returns a list of songs data items.


search_albums(keyword, num) - fetches the search results matching albums data
    *keyword*-****required, string***
      the search term
    num-****required, int***
      the number of data items to be returned
    Returns a list of albums data items.


search_playlists(keyword, num) - fetches the search results matching playlists data
    *keyword*-****required, string***
      the search term
    num-****required, int***
      the number of data items to be returned
    Returns a list of playlists data items.


Remaining functions are internal functions that are used by the functions mentioned above.
