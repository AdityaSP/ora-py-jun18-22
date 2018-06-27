import requests
import json
import os
import shutil
import threading

movie_name = raw_input("Enter movie name: ")
dir_name = movie_name + "_posters"

if os.path.exists(dir_name):
    if os.path.isfile(dir_name):
        raise ValueError('A file exists with the same name')
else:
    os.mkdir(dir_name)

def download(movie):
    poster_url = movie['Poster']
    poster = requests.get(poster_url)
    if poster.ok:
        file_name = dir_name + "/" + movie['imdbID'] + ".jpg"
        with open(file_name, 'wb') as fh:
            fh.write(poster.content)

r = requests.get(r'https://www.omdbapi.com/?s='+ movie_name + '&apikey=b4e17ea0')
if r.ok:
    data = json.loads(r.text)
    for movie in data['Search']:
        print "Downloading poster for", movie['Title']
        poster_url = movie['Poster']
        if poster_url != 'N/A':
            t = threading.Thread(target=download, args=(movie,))
            t.start()