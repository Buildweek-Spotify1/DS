{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "wS95uiRMsb4D"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import json\n",
    "import pickle\n",
    "import os\n",
    "\n",
    "from sklearn.neighbors import NearestNeighbors\n",
    "from sklearn.base import BaseEstimator, TransformerMixin\n",
    "\n",
    "from flask import Blueprint, request, jsonify, render_template, Flask\n",
    "from flask_cors import CORS, cross_origin\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "class My_encoder(BaseEstimator, TransformerMixin):\n",
    "   \n",
    "    def __init__(self,drop = 'first',sparse=False):\n",
    "        self.encoder = OneHotEncoder(drop = drop,sparse = sparse)\n",
    "        self.features_to_encode = []\n",
    "        self.columns = []\n",
    "    \n",
    "    def fit(self,X_train,features_to_encode):\n",
    "        \n",
    "        data = X_train.copy()\n",
    "        self.features_to_encode = features_to_encode\n",
    "        data_to_encode = data[self.features_to_encode]\n",
    "        self.columns = pd.get_dummies(data_to_encode,drop_first = True).columns\n",
    "        self.encoder.fit(data_to_encode)\n",
    "        return self.encoder\n",
    "    \n",
    "    def transform(self,X_test):\n",
    "        \n",
    "        data = X_test.copy()\n",
    "        data.reset_index(drop = True,inplace =True)\n",
    "        data_to_encode = data[self.features_to_encode]\n",
    "        data_left = data.drop(self.features_to_encode,axis = 1)\n",
    "        \n",
    "        data_encoded = pd.DataFrame(self.encoder.transform(data_to_encode),columns = self.columns)\n",
    "        \n",
    "        return pd.concat([data_left,data_encoded],axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def safe_paths():\n",
    "    '''\n",
    "    Function helper to define path of pickled model and preprocessed dataframes.\n",
    "    '''\n",
    "    \n",
    "    model_path = os.path.join('model_pickle.pkl')\n",
    "    train_path = os.path.join('df_encoded_for_train.pkl')\n",
    "    ref_path = os.path.join('df_encoded_for_ref.pkl')\n",
    "    \n",
    "    return (model_path, train_path, ref_path)\n",
    "\n",
    "\n",
    "\n",
    "def load_models():\n",
    "    '''\n",
    "    Helper function to load pickled model and preprocessed dataframes\n",
    "    '''\n",
    "    model_path, train_path, ref_path = safe_paths()\n",
    "    \n",
    "    pickled_model = pickle.load(open(model_path, 'rb'))\n",
    "    pickled_train = pickle.load(open(train_path, 'rb'))\n",
    "    pickled_ref = pickle.load(open(ref_path, 'rb'))\n",
    "        \n",
    "    return (pickled_model, pickled_train, pickled_ref)  \n",
    "\n",
    "\n",
    "\n",
    "############################################################\n",
    "'Saving loaded pickled files in global memory'\n",
    "\n",
    "PICKLED_MODEL, PICKLED_TRAIN, PICKLED_REF = load_models()\n",
    "#############################################################\n",
    "\n",
    "\n",
    "def recommend_track_id(track_id = '2YegxR5As7BeQuVp2U6pek'):\n",
    "    '''\n",
    "    Helper function that takes in atrack_id and recommends 14 track_ids of similar songs\n",
    "    '''\n",
    "    \n",
    "    song_num = PICKLED_REF[PICKLED_REF['track_id']==track_id].song_num.to_numpy()[0]\n",
    "    distance, neighbors = PICKLED_MODEL.kneighbors(np.array([PICKLED_TRAIN.values[song_num]]))\n",
    "    \n",
    "    song_list = []\n",
    "    for item in neighbors[0][1:]: # this way excludes itself\n",
    "        row = PICKLED_REF.iloc[item]\n",
    "        song_list.append((row.track_id))  # print list of track id\n",
    "      \n",
    "    return song_list\n",
    "\n",
    "\n",
    "def recommend_json(track_id='2YegxR5As7BeQuVp2U6pek'):\n",
    "    '''\n",
    "    Helper function the returns track_ids in json format.\n",
    "    '''\n",
    "    \n",
    "    rec_list = recommend_track_id(track_id)\n",
    "    rec_df = pd.DataFrame(rec_list, columns=['rec_track_id'])\n",
    "    rec_json = rec_df.to_json()\n",
    "    \n",
    "    return rec_json\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['0DJev1kGOCzaY8Ae3oQwH0',\n",
       " '3t7wojJJqpSNCASv5wOe5I',\n",
       " '3e0qSxu1fNPzDlwqWN3cBD',\n",
       " '2bQ6JedH8i3lrYLD0Zw57k',\n",
       " '44lusH2vzc4sRAwsooRhPh',\n",
       " '6ZOBP3NvffbU4SZcrnt1k6',\n",
       " '5sZ3xD192Bksbg6uBvd8Ig',\n",
       " '6ZzYETKetIfNUsZUb23jgG',\n",
       " '5ROshySAFh5odQX66q0anm',\n",
       " '0q6LuUqGLUiCPP1cbdwFs3',\n",
       " '0W9Xvd4Qx1aZPxEi94vgRY',\n",
       " '3GZD6HmiNUhxXYf8Gch723',\n",
       " '5PntSbMHC1ud6Vvl8x56qd',\n",
       " '4e9eGQYsOiBcftrWXwsVco']"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recommend_track_id('4FCb4CUbFCMNRkI6lYc1zI')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"rec_track_id\":{\"0\":\"6jvvpPJQJy5rMOEkLlADl6\",\"1\":\"17h2obBWaYI5UaRMtwnazd\",\"2\":\"645hAlwdOj1cx9dbf5Yu8A\",\"3\":\"3XnknFTGnFwK2Ffmgg1BH3\",\"4\":\"74tQaH4CxM5Rs9BzerEbHr\",\"5\":\"5o54O3MOnMvcPTmkguYkwg\",\"6\":\"4CMrdHWqic0usIZfTrKoI3\",\"7\":\"4CbKVDZkYKdv69I4bCaKUq\",\"8\":\"0c3gqQj20DX64pnVC4gLGR\",\"9\":\"3rjM7GhxdVq1YySsHBs21i\",\"10\":\"2z4pcBLQXF2BXKFvd0BuB6\",\"11\":\"2nLtzopw4rPReszdYBJU6h\",\"12\":\"3fMKnwiByu9yfeD5ISn9Et\",\"13\":\"0bxmVPKnEopTyuMMkaTvUb\"}}'"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recommend_json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Draft2.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "U4S12-NLP (Python3)",
   "language": "python",
   "name": "u4s12-nlp"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
