# DS


## Spotify Song Suggester API

A simple back-end Flask API to suggest spotify songs in the Spotify Song Suggester app
based on a track_id chosen by the user or a list of favorite songs

The spotify song suggester API uses the Spotify Audio Features dataset, uploaded to Kaggle joined with webscraped genre.

A KNN model was integrated into the Flask app. 
The app handles the requests, returning the appropriate JSON data.

---

## Usage

#### Retrieve 30 songs suggested based on one track_id given

### `[GET] /song/<track_id>`


**Parameters:** None

- request:track_id

**Returns:** JSON array containing the full details of the top 30 suggestions for a track_id given.

Example:

` https://spotifydsapp.herokuapp.com/song/6VjBxj5OhlHqL4h5qwo6gL`

Returns:

    `[{"index":37134,"artist_name":"Moby","track_id":"3UigcTkkcvBLnq6GVCjE3i",
    "track_name":"Like a Motherless Child - Broken Places Remix","acousticness":0.00176,
    "danceability":0.573,"duration_ms":349747,"energy":0.858,"instrumentalness":0.301,
    "key":2,"liveness":0.208,"loudness":-6.335,"mode":1,"speechiness":0.0497,
    "tempo":101.984,"time_signature":4,"valence":0.241,"popularity":27,"genre":"electronic"}...`

---


#### Retrieve 30 songs suggested based on a list of favorited song track_ids

### `[GET] OR [POST] /favorites`


	To retrieve data from this endpoint the body of the request should contain 
	Json in the format of :
  
`{
	"1":"song_id_1"
	"2":" song_id_2",
	"3":" song_id_3"
}`

Here is an example with actual track ids.

`{
	"1":"2RM4jf1Xa9zPgMGRDiht8O",
	"2":"1tHDG53xJNGsItRA3vfVgs",
	"3":"6Wosx2euFPMT14UXiWudMy"
}`

**Parameters:** None

- request: JSON object with track_id's

**Returns:** JSON array containing the full details of the top 30 suggestions based on a list of favorited song track_ids.

Example:

`https://spotifydsapp.herokuapp.com/favorites`

Returns:

	`[{"index":85630,"artist_name":"Beautiful Eulogy","track_id":"5Uv8yxTZhMWYhufL4jcWyV",
	"track_name":"Doxology - Instrumental","acousticness":0.609,"danceability":0.447,
	"duration_ms":231297,"energy":0.396,"instrumentalness":0.897,"key":6,"liveness":0.145,
	"loudness":-9.031,"mode":0,"speechiness":0.0367,"tempo":192.041,"time_signature":4,
	"valence":0.0346,"popularity":21,"genre":"hip-hop"}`

---

#### Radar chart image based on one track_id given

### `[GET] /image/<track_id>`

**Parameters:** None

- request:track_id

**Returns:** Renders a radar chart image based on one track_id given.

Example:

`https://spotifydsapp.herokuapp.com/image/6VjBxj5OhlHqL4h5qwo6gL`

Returns:

    `<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAH
    gCAYAAAA10dzkAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD
    2EBqD+naQAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9u
    My4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAgAElEQVR
    4nOzdd1SUV/4G8GdmGIcyoKAGwYJKEcUOAoJGUowNsG3EbiyJRtPjJ
    tnklxizm03ZTdFolsTE2BNj1BUsaFBRULEQsaCUiFhRERmkw5TfHwi
    rhihl4M4783zO8WwOyMwjyxmeud/...`

---

### Testing

Flask API was tested in Postman.

---

## Deployment

Find the last version of the Flask API on:

[Home](spotifydsapp.herokuapp.com)

[Suggestions example based on one song](spotifydsapp.herokuapp.com/song/6VjBxj5OhlHqL4h5qwo6gL)

[Suggestions example based on a list of favorites](spotifydsapp.herokuapp.com/favorites)

[Radar chart image example based on one song](spotifydsapp.herokuapp.com/image/6VjBxj5OhlHqL4h5qwo6gL)