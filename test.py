from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh import qparser
from whoosh.qparser import QueryParser

def schema(corpus_id):
	ix = open_dir("repository/"+corpus_id)
	return str(ix.schema)

def corpus_list(corpus_id):
	ix = open_dir("repository/"+corpus_id)

	sc = ix.searcher()
	
	qp = QueryParser("AB", ix.schema)
	qu = qp.parse(u"gene")
	r = sc.search(qu)
	
	print qp
	print qu
	
#	sc.close()
	return str(len(r))
#	return str(qu)

print corpus_list("biosynth")