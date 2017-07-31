# @Refactor: find better way of getting functions
from time import sleep, time
from pull import pull
from send import send
from parse import parse
import json


# @Refactor: Could have as one function or seperate files that handle each
#            aspect. Terms in particular should be with users
def terms(location):
    return []
    return ['common projects', 'cp', 'cps']

def settings(location):
    with open(location) as data_file:
        return json.load(data_file)

TERMS_LOCATION = 'terms.json'
SETTINGS_LOCATION = 'settings.json'

rose = []
total = 0

while True:

    settings = settings(SETTINGS_LOCATION)
    posts = pull('frugalmalefashion')
    if posts:
        # @Refactor: Move to seperate file/function that deals with old posts
        rising = []
        for post in posts:
            if post.id not in rose:
                rising.append(post)
        rose = posts

        # Later parsing will be based on user choice so it will probably be
        # during email process
        hits = parse(rising, terms(TERMS_LOCATION))

        if hits:
            send(hits)

    interval = settings['interval']
    total += interval
    print("==> SLEEPING FOR {}s. TOTAL OF {}s".format(interval, total))
    sleep(interval)
