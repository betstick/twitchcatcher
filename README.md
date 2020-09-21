# twitchcatcher
twitch stream catcher to automatically download streams for you

written in python.


requirements:

a twitch dev account with an api key. use google to figure out how to get one.

streamlink python library

python 3.5+

hopefully linux

500MB of ram?

installation:

clone the repo to your computer

configure the config.template and rename it to: config

run main.py in a terminal


notes:

the default stream quality is 'source' and it takes up a ton of space.

somewhere around line 9 in recorder.py you can change it to something else.

options are: high, low, medium, mobile, source, worst

for some reason it freaks out and misses the first minute or so of streams. not sure why. i blame twitches broken api for not updating quickly.


if you have questions throw it in the issues tab please.
