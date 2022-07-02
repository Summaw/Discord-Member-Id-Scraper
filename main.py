from pyparsing import White
import requests
import asyncio
import os
import discum
import time
from time import sleep
import sys
from colorama import Fore
    		
    		
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
    	os.system('clear')


green = Fore.LIGHTGREEN_EX
white = Fore.WHITE
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX

bot = discum.Client(token="")



def sprint(str):
       for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4./90)	

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        #print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members 

members = get_members(f'{guild_id}', f'{channel_id}') 
memberslist = []

for memberID in members:
    memberslist.append(memberID)
    print(memberID)

f = open('users.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()


def Menu():
	print(f"   __                    _____       	")
	print(f"  /  )             /      /  '  /    	")
	print(f" /  /o_  _.____ __/    ,-/-,. ./_ __ 	")
	print(f"/__/</_)(_(_) ((_/_   (_/  (_// </ (_	")
	print(f"										")
	print(f"		Developer: Summer 	  		")
	print(f"										")
	print(f"[?] Please Select An Option				")
	print(f"[1] Start Member Scarper				")
	print(f"[2] Start Mass Dm						")
	print("											")
	a=input(f">> "+ white)
	if a == "1":
		guild_id =int(input(yellow + '\n[?] Enter the Guild id you would like to scrape: ' + white))
		sprint(yellow + f"[{white}+{yellow}] Checking Guild ID...")
		channel_id = int(input(yellow + '\n [?] Enter the Channel id you would like to scarpe: ' + white))
		sprint(yellow + f"[{white}+{yellow}] Checking Channel ID...")
		sleep(3)
		clear()
		get_members(guild_id, channel_id)

if __name__ == "__main__":
    Menu()


