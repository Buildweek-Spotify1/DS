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


Example:
` https://suggestords2.herokuapp.com/song?title=Hello&artist=Adele`

Returns:
`album	25
artist	Adele
id	4sPmO7WMQUAf45kwMOtONw
title	Hello `


* <https://suggestords2.herokuapp.com/suggestions?title=&artist=> (returns 6 most similar songs, along with data for graphing)

Example:
`https://suggestords2.herokuapp.com/suggestions?title=Hello&artist=Adele `

Returns:
`	
tracks	
0	
features	
acousticness	1.0264802142219576
danceability	0.9457493244647683
energy	1.0529816005320327
instrumentalness	0
key	0.999980000399992
liveness	0.9805269186712485
loudness	0.8664621240709445
mode	0
speechiness	0.982758620689655
tempo	0.9340168555152023
valence	1.1795226565202355
info	
album	miwa the Best
artist	miwa
id	3o9Gn0UhzcNZDPyGmBkSHQ
image	https://i.scdn.co/image/ab67616d00001e02a96850706ce324c3c64481e1
title	Unchained Love `

* <https://suggestords2.herokuapp.com/least?title=&artist=> (returns least similar song)]

Example:
`https://suggestords2.herokuapp.com/least?title=Hello&artist=Adele`


Returns:	
`album	Natural Water Sounds for Sleep and Relaxation Volume 1
artist	Tmsoft’s White Noise Sleep Sounds
id	4FICqRgVTZsHOnU9QNKCPD
image	https://i.scdn.co/image/ab67616d00001e029d882c85f44dee0c855077ff `

Url Parameters: title (song title) artist (artist)

Results will be returned as long as one of the parameters is entered, and is a valid artist name/song title

User input is sent to the spotify api in order to retrieve correct song info and audio features
