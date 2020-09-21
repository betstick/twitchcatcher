import requests, json, ast, configparser, threading, time, streamlink, datetime
from recorder import record

#Q: why are there so many comments in here???
#A: so i don't forget how it works!

#read in the config file
config = configparser.ConfigParser()
config.read('config')

#grab stuff from the config file
client_id = config['client_info']['client_id']
client_secret = config['client_info']['client_secret']
userlist = (config['users']['userlist']).split(',')#splits string into list
output_location = (config['paths']['output'])

def get_token(client_id,client_secret):
	post = "https://id.twitch.tv/oauth2/token?client_id="+client_id+"&client_secret="+client_secret+"&grant_type=client_credentials"
	success = 0

	#retry connection in case of failure, will hang all code, but that's okay
	while (success == 0):
		try:
			acesss_token = json.dumps((requests.post(post).json())["access_token"]).replace('"','')
			success = 1
		except:
			print("Connection failed. Retrying..")
	
	return acesss_token

def list_check(userlist,client_id,acesss_token):
	online_list = []

	for username in userlist:
		userurl = 'https://api.twitch.tv/helix/streams?user_login='+username
		get = requests.get(userurl, headers={"Authorization": "Bearer "+acesss_token,"Client-ID": client_id})

		#check theres a dict before we try to eval it to prevent error
		if(len((get.json())["data"]) > 0):
			print(username + "'s chanenl is active")
			try:
				status = ast.literal_eval(json.dumps((get.json())['data'])[:-1][1:])
			except:
				get = requests.get(userurl, headers={"Authorization": "Bearer "+acesss_token,"Client-ID": client_id})
				status = ast.literal_eval(json.dumps((get.json())['data'])[:-1][1:])
				print(get.json())
			if(status["type"]=="live"): #and(status["user_name"]==username)):
				print(status["user_name"]+" is online")
				online_list.append(username)
		else:
			print(username+" is offline")

	return online_list

access_token = get_token(client_id,client_secret)

#twitch tokens expire after roughly two months, so we need to
#make new tokens early to prevent expiration, ten days early
expires = 0
timeout = 5000000 #like 50 days lol, never checked if this works.
#you should seriously reboot your servers weekly. granted for
#running an application like this, rebooting may not be available
#at all times. figure out your own solution.

while(1==1):
	#run this preemptively to prevent token expiration
	if(expires > timeout):
		access_token = get_token(client_id,client_secret)

	succ = 0
	while(succ == 0):
		try:
			online_list = list_check(userlist,client_id,access_token)
			succ = 1
		except:
			print("Online check failed, retrying...")
			pass

	for username in online_list:
		#threads exist, so see if the one you want to make exists
		found = 0
		for thread in threading.enumerate():
			if((username+"_recorder") in str(thread)):
				found = 1
		
		if(found==0):
			threading.Thread(name=(username+"_recorder"),target=record,args=(username,output_location)).start()
		else:
			print("Thread found, no new thread.")

	#sleep 10 seconds to prevent spamming twitch api
	#and to not waste cpu cycles, also clock in time
	time.sleep(10)
	expires = expires + 10
