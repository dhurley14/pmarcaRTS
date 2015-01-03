import os
import sys
import requests
import json
import ast

""" This script will pass my list of URL's with articles to diffbot,
which will then extract the body text and write that to a file I 
will then download.  This script is a copy of the code I found on
blog.mathandpencil.com/using-latent-dirichlet-allocation-to-categorize-my-twitter-feed/

"""

DIFF_BOT_TOKEN = 'xxx'

def create_bulk_job(urls, name):
    """ urls will be whitespace separated values
    
    """
    apiUrl = 'http://api.diffbot.com/v3/article'
    params = dict(token=DIFF_BOT_TOKEN, name=name, urls=urls, apiUrl=apiUrl)
    response = requests.post('http://api.diffbot.com/v3/bulk',data=params)
    moarData = json.loads(response.content)
    # response from diffbot wrote data here..
    target = open('output_from_diffbot.txt','a')
    target.write(str(moarData))
    print moarData['jobs'][0]['downloadJson']

if __name__ == '__main__':
    tweetDICTurls = ast.literal_eval(open("tweetdict.txt").read())
    urls = " ".join([u.strip().replace('"','') for u in tweetDICTurls.keys()])
    name = "HURLEY"
    create_bulk_job(urls=urls,name=name)
