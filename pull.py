import praw, json

def pull(subreddit):

    with open('secret.json') as data_file:
        secret = json.load(data_file)

    client_id     = secret['client_id']
    client_secret = secret['client_secret']

    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         redirect_uri='http://localhost:8080',
                         user_agent='Common by /u/resloves')

    posts = []

    for post in reddit.subreddit(subreddit).rising():
        posts.append(post)

    return posts
