def parse(posts):
    links = []
    for post in posts:
        links.append(post.shortlink)
    return links
