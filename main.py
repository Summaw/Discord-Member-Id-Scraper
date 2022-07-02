from random import random
import requests
import asyncio
import os
import discum
import time
from time import sleep
import sys
from colorama import Fore
import random

green = Fore.LIGHTGREEN_EX
white = Fore.WHITE
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX

def sprint(str):
       for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4./90)


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def close_after_fetching(token, guild_id):
	bot = discum.Client(token=token)
	if bot.gateway.finishedMemberFetching(guild_id):
		lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
		print(str(lenmembersfetched)+' members fetched')
		bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.close()

def get_members(token, guild_id, channel_id):
	bot = discum.Client(token=token)
	bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
	bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
	bot.gateway.run()
	bot.gateway.resetSession()
	return bot.gateway.session.guild(guild_id).members

def Menu():
    	printlogo()
a=input(f": "+ white)
if a == "1":
	guild_id = input(yellow + '\n[?] Enter the Guild id you would like to scrape: ' + white)
	sprint(yellow + f"[{white}+{yellow}] Checking Guild ID...")
	channel_id = input(yellow + '\n [?] Enter the Channel id you would like to scarpe: ' + white)
	sprint(yellow + f"[{white}+{yellow}] Checking Channel ID...")
	token = input(yellow + '\n [?] What token would you like to scrape everything with?: '+ white)
	sprint(yellow + f"[{white}+{yellow}] Checking Token...")
	members = get_members(token, guild_id, channel_id)
	memberslist = []
	for memberID in members:
		memberslist.append(memberID)
	print(memberID)
	f = open('users.txt', "a")
	for element in memberslist:
		f.write(element + '\n')
	f.close()

if a == "2":
	header = mainHeader('yourdiscordtoken')
payload = {"content": "hello mate!!", "tts": "false"}

response = requests.post(f'https://discord.com/api/v9/channels/targetsuserid/messages', headers=header,json=payload)

if response.ok:
    	print(f'Successfully Sent a message')
else:
    	print(f"Failed to send dm")
sleep(5)
Menu()



def printlogo1():
    	print(f"""
			   __                    _____       	
			  /  )             /      /  '  /    	
			 /  /o_  _.____ __/    ,-/-,. ./_ __ 	
			/__/</_)(_(_) ((_/_   (_/  (_// </ (_	
											
			Made By Olympus Coding Service		
				Developer: ImNotSummer 				
												""")


def printlogo():
    	 print(f"""\n\n __                    _____       	
			  /  )             /      /  '  /    	
			 /  /o_  _.____ __/    ,-/-,. ./_ __ 	
			/__/</_)(_(_) ((_/_   (_/  (_// </ (_	
											
			Made By Olympus Coding Service		
				Developer: ImNotSummer 	  	
											
	[?] Please Select An Option			
	[1] Start Member Scarper			
	[2] Start Mass Dm						
												""")

if __name__ == "__main__":
    Menu()
