import gensim, logging, sys, nltk
from gensim import corpora



#build lda model here.

def createDict(myTextFile):
    dictionary = corpora.Dictionary(line.lower().split() for line in open(sys.argv[1]))
    STOP_WORDS = nltk.corpus.stopwords.words('english')
    stoplist = set(STOP_WORDS)
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
    dictionary.filter_tokens(once_ids + stop_ids)
    dictionary.compactify()
    dictionary.save('tmp/rt_articles_ids.dict')
    return dictionary

class MyCorpus(object):
    def __iter__(self):
        aFile = sys.argv[1]
        dictionary = createDict(aFile)
        for line in open(aFile): #aFile is the corpus
            yield dictionary.doc2bow(line.split())

def createModel(aFile):
    mem_friendly_corpus = MyCorpus()
    corpora.MmCorpus.serialize('corpus.mm',mem_friendly_corpus)
    id2word = gensim.corpora.Dictionary.load('tmp/rt_articles_ids.dict')
    mm = gensim.corpora.MmCorpus('corpus.mm')
    lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=16, update_every=0, passes=30)
    topics = lda.show_topics()
    lda.save('tmp/lda_model.lda')
    target = open('tmp/16topics.txt','a+b')
    for topic in topics:
        target.write(topic.encode('utf-8') + '\n')
    target.close()

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    createModel(sys.argv[1])
    
