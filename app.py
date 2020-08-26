from flask import Flask, request, render_template, jsonify
from sklearn.neighbors import NearestNeighbors
import spotipy
from spotipy import oauth2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from bottle import request, run, route
import io


PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID='8da7b70800a34cecbb89a72541dead74'
SPOTIPY_CLIENT_SECRET='471d09ad2d0b4de5831d99f5063c09c8'
SPOTIPY_REDIRECT_URI='http://localhost:8080'
CACHE = '.spotipyoauthcache'

#sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE)

df = pd.read_csv("https://raw.githubusercontent.com/Buildweek-Spotify1/DS/master/MusicWithGenresFiltered.csv")
def process_input(song_id, return_json = True):
    c = ["duration_ms", "index", "genre", "artist_name", "track_id", "track_name", "key", "mode"] # Columns to Omit
    song = df[df["track_id"] == song_id].iloc[0] # Get Song
    df_selected = df.copy()
    if not pd.isnull(song["genre"]): # If genre, set subset to only genre
        df_selected = df[df["genre"] == song["genre"]]
    nn = NearestNeighbors(n_neighbors=31, algorithm="kd_tree") # Nearest Neighbor Model
    nn.fit(df_selected.drop(columns=c))
    song = song.drop(index=c)
    song = np.array(song).reshape(1, -1)
    if return_json is False:
        return df_selected.iloc[nn.kneighbors(song)[1][0][1:]] # Return results as df
    return df_selected.iloc[nn.kneighbors(song)[1][0][1:]].to_json(orient="records") # Return results as json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
#@route('/')
#def index():

#    access_token = ""

 #   token_info = sp_oauth.get_access_token()

  #  if token_info:
   #     print('Found cached token!')
    #    access_token = token_info['access_token']
   # else:
    #    url = request.url
     #   code = sp_oauth.parse_response_code(url)
      #  if code:
       #     print("Found Spotify auth code in request URl Trying to get valid access token...")
        #    token_info = sp_oauth.get_access_token(code)
        #    access_token = token_info['access_token']
    
   # if access_token:
    #    print("Access Token available trying to get user information")
    #    sp = spotipy.Spotify(access_token)
    #    results = sp.current_user()
    #    return results
   # else:
    #    return htmlForLoginButton()

#def htmlForLoginButton():
#    auth_url = getSPOauthURI()
#    htmlForLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
#    return htmlForLoginButton

# def getSPOauthURI():
#    auth_url = sp_oauth.get_authorize_url()
#    return auth_url

@app.route('/song/<song_id>', methods = ['GET'])
def song(song_id):
    
    """Route for recommendations based on song selected."""
    return  process_input(song_id) #jsonify(recomendations)

@app.route('/favorites',methods = ['GET', 'POST'])
def favorites():
    my_dict = request.get_json(force=True)
    track_list = pd.DataFrame()
    for i in my_dict.values():
        track_list = track_list.append(process_input(i,False))
    track_list.drop_duplicates()
    return track_list.sample(30).to_json(orient="records")

@app.route('/image/<song_id>', methods = ['GET'])
def radar_map(song_id):
    """Route for returning radar graph."""
    c = ["acousticness", "danceability", "energy", "valence"] # Columns to Show
    N = len(c)
    values=df[df["track_id"] == song_id].iloc[0][c].tolist()
    values += values[:1]
    print(values)
    angles = [n / float(N) * 2 * 3.141 for n in range(N)]
    angles += angles[:1]
    print(angles)
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], c, color='grey', size=8)
    plt.yticks([], [], color="grey", size=7)
    ax.set_rlabel_position(0)
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    pic_bytes = io.BytesIO()
    plt.savefig(pic_bytes, format="png")
    pic_bytes.seek(0)
    data = base64.b64encode(pic_bytes.read()).decode("ascii")
    plt.clf()
    return "<img src='data:image/png;base64,{}'>".format(data)

if __name__ == "main":
    app.run()