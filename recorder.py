import requests, json, ast, configparser, threading, time, streamlink, datetime

def record(username_in,output_in):
	print("recording "+username_in)
	try:
		streams = streamlink.streams("http://twitch.tv/"+username_in)
	except:
		print("type error or 410 for "+username_in+", no clue why, maybe something else...")#it was happening to fextralife
	stream = streams["best"]#always select best, we're not messing around
	filename = username_in+(datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S.ts"))
	output_file = (output_in+filename)
	open(output_file, "w+")#creates the first file
	
	with open(output_file, "ab") as ouput:
		fd = stream.open()
		recording = 1
		while(recording==1): #this is dirty but it'll work for now :/
			try:
				data = fd.read(1024)
			except OSError:
				#try to close then reopen the file :P
				print("file read timeout hiccup, fix later")
				fd.close()
				fd = stream.open()

			#checks if the data stream has ended, if so, ends the recording
			if not data:
				fd.close()
				ouput.close
				print(username_in+"'s stream has ended, go in peace")
				recording = 0

			ouput.write(data)