#!/usr/bin/python

import twitter
import datetime

now = datetime.datetime.now().time()
midnight = now.replace(hour=23, minute=59, second=59, microsecond=59)
nowstring = datetime.datetime.now().strftime("%H:%M:%S")

t = twitter.Twitter(auth=twitter.OAuth('','','','')

if datetime.time(hour=0) <= now < datetime.time(hour=4):
    print "Selamat malam"
    tweet = nowstring + ' Selamat malam dari planpin | Planet Python Indonesia! http://planet.python.or.id'
    t.statuses.update(status=tweet)
if datetime.time(hour=4) <= now < datetime.time(hour=9):
    print "Selamat pagi"
    tweet = nowstring + ' Selamat pagi dari planpin | Planet Python Indonesia! http://planet.python.or.id'
    t.statuses.update(status=tweet)
if datetime.time(hour=9) <= now < datetime.time(hour=15):
    print "Selamat siang"
    tweet = nowstring + ' Selamat siang dari planpin | Planet Python Indonesia! http://planet.python.or.id'
    t.statuses.update(status=tweet)
if datetime.time(hour=15) <= now) < datetime.time(hour=21):
    print "Selamat sore"
    tweet = nowstring + ' Selamat sore dari planpin | Planet Python Indonesia! http://planet.python.or.id'
    t.statuses.update(status=tweet)
if datetime.time(hour=21) <= now < midnight:
    print "Selamat malam"
    tweet = nowstring + ' Selamat malam dari planpin | Planet Python Indonesia! http://planet.python.or.id'
    t.statuses.update(status=tweet)
