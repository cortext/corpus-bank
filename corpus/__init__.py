from flask import Flask, render_template

import glob

from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.query import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
	r = glob.glob("repository/*")
	
	items = []
	
	for corpus_dir in r:
		item = {}
		item["name"] = corpus_dir.split("/",1)[1]
		
		ix = open_dir(corpus_dir)
		
		item["count"] = ix.doc_count()
		
		items.append(item)
	
	return render_template("home.html", items = items)

@app.route("/corpus/<corpus_id>/schema")
def schema(corpus_id):
	ix = open_dir("repository/"+corpus_id)
	return str(ix.schema)

@app.route("/corpus/<corpus_id>/list")
def corpus_list(corpus_id):
	ix = open_dir("repository/"+corpus_id)
	
	sc = ix.searcher()
	
	q = Every()
	
	r = sc.search(q, limit="none")
	
	return render_template("list.html", items = r)