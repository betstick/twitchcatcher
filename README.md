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

streams can become "malformed" due to ads and the twitch api being bad. can cause buggy and difficult to navigate timelines in the videos. re-encode the videos to fix it? not sure. haven't checked. re-encoding 6 hour videos takes 6+ hours on my systems. the people behind streamlink have explained in depth that its twitch messing up encoding or something to that effect. blocking ads is the solution for us, twitch fixing their platform should be the solution but they probably don't care.

the default stream quality is 'source' and it takes up a ton of space.

somewhere around line 9 in recorder.py you can change it to something else.

options are: high, low, medium, mobile, source, worst

for some reason it freaks out and misses the first minute or so of streams. not sure why. i blame twitches broken api for not updating quickly.

also, if you don't want ads in your streams, install the nightly version of streamlink: pip3 install git+https://github.com/streamlink/streamlink

if you see lots of errors in the logs when streamers go offline, that's normal. its twitch's api (again) not updating quickly and so my code tries to keep reading from a nonexistant stream. better to try recording the stream and fail then to not try and potentially miss a stream or break up files due to an error.

if you have questions throw it in the issues tab please.
