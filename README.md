# DS


## Spotify Song Suggester API

A simple back-end Flask API to suggest spotify songs in the Spotify Song Suggester app
based on a track_id chosen by the user or a list of favorite songs

The spotify song suggester API uses the Spotify Audio Features dataset, uploaded to Kaggle joined with webscraped genre.

A KNN model was integrated into the Flask app. 
The app handles the requests, returning the appropriate JSON data.


# API

The DS api for this project has 3 endpoints 

* <https://suggestords2.herokuapp.com/song?title=&artist=> (returns information about the song)
* <https://suggestords2.herokuapp.com/suggestions?title=&artist=> (returns 6 most similar songs, along with data for graphing)
* <https://suggestords2.herokuapp.com/least?title=&artist=> (returns least similar song)

Url Parameters: title (song title) artist (artist)

Results will be returned as long as one of the parameters is entered, and is a valid artist name/song title

User input is sent to the spotify api in order to retrieve correct song info and audio features