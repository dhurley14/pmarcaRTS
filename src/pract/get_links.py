""" This script is responsible for acquiring

 all of Marc Andreessen's most recent retweets.
 01/19/2015  
"""
from twython import Twython

def get_authentication():
    """ Get a connection to the Twitter API using Twython.

    return a new instance of the Twython object.
    """
    APP_KEY = 'xxx'
    APP_SECRET = 'xxxxx'
    twitter = Twython(APP_KEY, APP_SECRET)
    return twitter

def get_tweets(username='pmarca', **kwargs):
    """ Get a user's timeline

    :param username: (default pmarca)
    :param tweetID: 
    """
    twitter = get_authentication()

    # to get all 3200 possible tweets, I must cycle
    # through, and change the max_id on each call to be the lowest
    # id , so that my next call gets all the tweets below that id,
    # and so on and so forth.
    user_timeline = ""

    if len(kwargs) == 0:
        user_timeline = twitter.get_user_timeline(screen_name=username, count=200)
    else:
        user_timeline = twitter.get_user_timeline(screen_name=username, count=200, max_id=kwargs['anId'])    

    return user_timeline

def output_all_rts():
    user_timeline = get_tweets()
    #print(user_timeline[0]['entities']['urls'][0]['url'])
    #for i in xrange(16):
    #print("len = "+str(len(user_timeline)))
    urls = {user_timeline[i]['entities']['urls'][0]['expanded_url']: user_timeline[i]['text']  for i in xrange(len(user_timeline)) if user_timeline[i]['entities']['urls'] and "RT" in user_timeline[i]['text']}
    """rts = [user_timeline[i]['text'].encode('utf-8') for i in xrange(len(user_timeline)) 
        if "RT " in user_timeline[i]['text']]"""
    for i in xrange(16):
        user_timeline = get_tweets(username='pmarca',anId=user_timeline[len(user_timeline)-1]['id'])
        urls.update({user_timeline[i]['entities']['urls'][0]['expanded_url']: user_timeline[i]['text'] for i in xrange(len(user_timeline))
            if user_timeline[i]['entities']['urls'] and "RT" in user_timeline[i]['text']})
    print len(urls)
    output_file = open("pmarca_rts_links_dict.txt", "w+b")
    output_file.write(str(urls))
    #for link,text in urls.items():
    #    output_file.write(''.join(link,text)+"\n")
    output_file.close()

if __name__ == '__main__':
    output_all_rts()
