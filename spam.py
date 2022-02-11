# Launder
# script for spamming one message
# started dev on 11/02/22

from os import kill
import discum
import time

# function for reading file and extracting the data each line
def read_file(file_name):
    with open (file_name, 'r', encoding = 'UTF-8') as file:
        contents = file.readlines()
    return contents

TOKEN = (read_file('config.txt')[0]).strip()
TOKENS = read_file('./textFiles/tokens.txt')
tokenNum = len(TOKENS)
CHANNELID = (read_file('config.txt')[1]).strip()

bot = discum.Client(token=TOKEN, log=False) # discord token to login with
print("Amount of Available Accounts: "+str(tokenNum))
NUM_SEND = int(input("amount of msg:")) # takes console input
if (NUM_SEND > tokenNum): # checks to see if too many reacts 
    print("Can't msg that many times.")
    exit(200) #exits out
MESSAGE = input("message:")
count = 0
# loop to run through and react to ceartain id
for token in TOKENS:
    bot.switchAccount(token.strip())
    bot.typingAction(CHANNELID)
    time.sleep(5)
    bot.sendMessage(CHANNELID, MESSAGE)
    count+=1
    if (count == NUM_SEND):
        break
