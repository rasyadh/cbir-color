import os, json

from flask import Flask, request, Response, jsonify, json
from flask import render_template, url_for, redirect, send_from_directory
from flask import make_response, abort, session
from werkzeug.utils import secure_filename

from project import app

from cbir.indexing import Indexing
from cbir.colordescriptor import ColorDescriptor
from cbir.searcher import Searcher
from cbir.search import Search

# Web Profile
@app.route('/')
def index():
    return redirect(url_for('sepatu_image'))

# Sepatumu Image Search
@app.route('/sepatumu/image/')
def sepatu_image():
    return render_template('sepatumu/image.html', title="Gambar Sepatumu")

@app.route('/sepatumu/image/features/')
def features():
    data = None
    with open('dataset_features.json') as f:
        data = json.load(f)
        f.close()

    return render_template('sepatumu/features.html', title="Fitur Gambar", data=data)

@app.route('/sepatumu/image/process_features/')
def process_features():
    indexer = Indexing.indexer()

    return redirect('/sepatumu/image/features/')

@app.route('/sepatumu/image/result', methods=['GET', 'POST'])
def image_result():
    result = None
    if request.method == 'POST':
        f = request.files['search']
        name = secure_filename(f.filename)
        img = f.read()
        
        # query by color
        s = Search(img, name)

        result, query = s.query_search()
    return render_template('sepatumu/result_image.html', title=name, data=result, query=query['query'])