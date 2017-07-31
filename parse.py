def parse(posts, terms):
    hits = []
    for post in posts:
        post.hits = []
        for term in terms:
            if term in post.title.lower() or term in post.selftext.lower():
                post.hits.append(term)
        if len(post.hits) > 0:
            hits.append(post)
    return hits
