import praw, json

ID_LOCATION = 'old_post_ids.json'

def pull(subreddit):

    print("==> PULLING")

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

    if posts:
        print(" -> PULLED {} POSTS".format(len(posts)))

        # @Hack: Everything is terrible. Something wrong with reading json if
        #        its both read and write.
        old_ids = []

        # Remove old posts and update json
        with open(ID_LOCATION, 'r') as f:
            old = json.load(f)
            old_ids = old['ids']

        tmp = []
        data = {}
        data['ids'] = []

        with open(ID_LOCATION, 'w') as f:
            # @Refactor: probably a way using sets to find difference
            for post in posts:
                data['ids'].append(post.id)
                if post.id not in old_ids:
                    tmp.append(post)
            json.dump(data, f)
            posts = tmp

        print(" -> {} NEW POSTS".format(len(posts)))
    else:
        print(" -> EMPTY")

    return posts
