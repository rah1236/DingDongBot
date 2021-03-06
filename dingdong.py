import time #for delay (in seconds)
import pygame #used for mixer to play doorbell sound
from slackclient import SlackClient #Used for slack client

slack_client = SlackClient("INSERT API KEY HERE") #Api Key initialization

if slack_client.rtm_connect(): #Connect slack client
	print "Connected!"
pygame.mixer.init() #initialize pygame mixer
pygame.mixer.music.load("Ding-dong-chime.mp3") #load doorbell sound

while True: #loop forever
	for message in slack_client.rtm_read():
		if 'text' in message and message['text'].startswith("!dingdong"):
                  	pygame.mixer.music.play()
			print "Doorbell Rang!"
	time.sleep(1) #delay for 1 second
