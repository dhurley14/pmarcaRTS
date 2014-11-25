""" This script is responsible for acquiring

 all of Marc Andreessen's most recent retweets.  
"""
from twython import Twython

def get_authentication():
    """ Get a connection to the Twitter API using Twython.

    return a new instance of the Twython object.
    """
    APP_KEY = 'xxxxxxx'
    APP_SECRET = 'xxxxxxxxxxxx'
    twitter = Twython(APP_KEY, APP_SECRET)
    return twitter

def get_tweets(username='pmarca'):
    """ Get a user's timeline

    :param username: (default pmarca)
    """
    twitter = get_authentication()
    # to get all 3200 possible tweets, I must cycle
    # through, and change the max_id on each call to be the lowest
    # id , so that my next call gets all the tweets below that id,
    # and so on and so forth.
    user_timeline = twitter.get_user_timeline(screen_name=username, count=200, max_id=536687397044772864)
    return user_timeline

def output_all_rts():
    user_timeline = get_tweets()
    rts = [user_timeline[i]['text'].encode('utf-8') for i in xrange(len(user_timeline)) 
        if "RT " in user_timeline[i]['text']]
    print len(rts)
    output_file = open("pmarca_rts.txt", "w+b")
    for line in rts:
        output_file.write(''.join(line)+"\n")
    output_file.close()

if __name__ == '__main__':
    output_all_rts()
