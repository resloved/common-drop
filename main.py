# @Refactor: find better way of getting functions
from time import sleep, time
from pull import pull
from send import send
from parse import parse
import json


def update_settings(location):
    with open(location) as data_file:
        return json.load(data_file)

settings = update_settings('settings.json')

rose = []

while True:

    print("==> PULLING")
    posts = pull('leagueoflegends')

    if posts:

        rising = []
        for post in posts:
            if post.id not in rose:
                rising.append(post)

        print("==> PARSING {} MESSAGES".format(len(rising)))
        hits = parse(rising)
        rose = posts

        if hits:
            print("==> SENDING")
            send(hits)
        else:
            print(" -> NO HITS")

    else:
        print(" -> EMPTY")

    interval = settings['interval']
    print("==> SLEEPING FOR {}s".format(interval))
    sleep(interval)

    settings = update_settings('settings.json')
