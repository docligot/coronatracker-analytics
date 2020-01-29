import json
import yaml
from datetime import date
from twitterscraper import query_tweets

def config_args(config):
    """Return arguments from the configuration file.
    Keyword arguments:
    config -- the configuration file that contains the parameters needed for the program.
    """
    with open('config.yaml', 'rb') as file:
        conf = yaml.safe_load(file)
    return conf['scrape']

if __name__ == '__main__':
    args = config_args('config.yaml')
    query_string = args['query']
    print(query_string)
    limit = args['limit']
    b_date = date.today()
    e_date = date.today()
    tweets = []
    for tweet in query_tweets(query_string, limit):
        tweets.append(tweet.text)
    
    with open('datasets/data.json', 'a') as f:
        f.write(json.dumps(tweets))

