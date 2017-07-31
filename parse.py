def parse(posts, terms):

    print("==> PARSING {} MESSAGES".format(len(posts)))

    if not terms:
        print(" -> NO TERMS SET")
        return posts

    hits = []

    for post in posts:
        post.hits = []
        for term in terms:
            if term in post.title.lower() or term in post.selftext.lower():
                post.hits.append(term)
        if len(post.hits) > 0:
            hits.append(post)

    if hits:
        print(" -> {} HITS".format(len(hits)))
    else:
        print(" -> NO HITS")

    return hits
