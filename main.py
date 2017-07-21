# use praw(?)
# pull all posts off frugalmalefashion
# find key words on posts

import praw, json

with open('secret.json') as data_file:
    secret = json.load(data_file)

client_id     = secret['client_id']
client_secret = secret['client_secret']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     redirect_uri='http://localhost:8080',
                     user_agent='Common by /u/resloves')

for sub in reddit.subreddit('all-frugalmalefashion').new():
    print(sub)

#posts = reddit.get_subreddit('f
#print(reddit.auth.url(['identity'], '...', 'permanent'))


