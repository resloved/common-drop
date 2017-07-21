def parse(posts):
    links = []
    for post in posts:
        links.append(post[2])
    return links
