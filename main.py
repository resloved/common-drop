from time import sleep, time
from pull import pull
from send import send
import json


def get_settings(location):
    with open(location) as data_file:
        return json.load(data_file)

SETTINGS_LOCATION = 'settings.json'

total = 0

while True:

    settings = get_settings(SETTINGS_LOCATION)
    posts = pull('frugalmalefashion')
    if posts:
        send(posts)

    interval = settings['interval']
    print("==> SLEEPING FOR {}s. TOTAL OF {}s".format(interval, total))
    sleep(interval)
    total += interval
