#!/usr/bin/python

import twitter
import datetime

planpin = datetime.datetime.now().time('','','','')

t = twitter.Twitter(auth=twitter.OAuth()

if datetime.time(hour=0) <= planpin < datetime.time(hour=4):
    print "Selamat malam"
    tweet = 'planpin bot tweet: ' + 'Selamat malam'
    t.statuses.update(status=tweet)
if datetime.time(hour=4) <= planpin < datetime.time(hour=9):
    print "Selamat pagi"
    tweet = 'planpin bot tweet: ' + 'Selamat pagi'
    t.statuses.update(status=tweet)
if datetime.time(hour=9) <= planpin < datetime.time(hour=15):
    print "Selamat siang"
    tweet = 'planpin bot tweet: ' + 'Selamat siang'
    t.statuses.update(status=tweet)
if datetime.time(hour=15) <= planpin < datetime.time(hour=21):
    print "Selamat sore"
    tweet = 'planpin bot tweet: ' + 'Selamat sore'
    t.statuses.update(status=tweet)
if datetime.time(hour=21) <= planpin < datetime.time(hour=0):
    print "Selamat malam"
    tweet = 'planpin bot tweet: ' + 'Selamat malam'
    t.statuses.update(status=tweet)
~                                     
