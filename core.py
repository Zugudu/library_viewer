#!/usr/bin/env python3
from flask import Flask, render_template, url_for
from os import walk, listdir
from os.path import isdir, join, isfile

app = Flask(__name__)
hentai_dir = 'hentai'


@app.route('/')
def index():
    title = [f for f in listdir(join('static', hentai_dir)) if isdir(join('static', hentai_dir, f))]
    manga_list = []
    for i in title:
        manga = [j for j in listdir(join('static', hentai_dir, i)) if isdir(join('static', hentai_dir, i, j))]
        manga_list.append({'name': i,
            'manga': [m for m in manga]
        })
    #print('\n\n', manga_list, '\n\n')
    return render_template('main.html', title = manga_list)


@app.route('/w/<path:url>')
def w(url):
    img = sorted([f for f in listdir(join('static', hentai_dir, url)) if isfile(join('static', hentai_dir, url, f))])
    root = url_for('static', filename=join(hentai_dir, url))
    return render_template('show.html', img = img, root = root)


if __name__ == '__main__':
    app.run(port=8081, debug=True)
