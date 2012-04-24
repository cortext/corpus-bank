from flask import Flask
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh import qparser

app = Flask(__name__)
app.debug = True

@app.route("/corpus/<corpus_id>/schema")
def schema(corpus_id):
	ix = open_dir("repository/"+corpus_id)
	return str(ix.schema)

@app.route("/corpus/<corpus_id>/list")
def corpus_list(corpus_id):
	ix = open_dir("repository/"+corpus_id)
	
	sc = ix.searcher()
	
	qu = qparser.QueryParser("AB", ix.schema).parse(u"gene")
	
	r = sc.search(qu)
	
	return str(len(r))
	# return str(qu)