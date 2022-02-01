# MADE BY LAUNDER
# DEV STARTED ON 29/1/22
# DISCORD BOT FOR AUTOMATING CONVERSATION IN A CHANNEL
# STRICTLY FOR RESEARCH PURPOSES ONLY
from urllib.error import ContentTooShortError
import discum     
import time
import random

global count
global token_count
global last_message
global TOKEN
global CHANNELID
# helper function to read files i think this can be simplified at some point but it works rn
def read_file(file_name):
    with open (file_name, 'r', encoding = 'UTF-8') as file:
        contents = file.readlines()
    return contents

# helper function to remove line from file so they dont get used again
def delete_line(file_name, line_num, messages):
    # adds the removed lines to a new file to keep data
    removed_msg = open(file_name+'RemovedMsg.txt', 'a')
    removed_msg.write(messages[line_num])
    removed_msg.close()
    del messages[line_num]
    new_messages = open(file_name+'Msg.txt', "w+")
    for line in messages:
        new_messages.write(line)
    new_messages.close()

def message(name, count, messageId, reply):
    global token_count, last_message
    # these get the file and shuffle it to randomize the message and token order
    tokens = read_file(name+'Tokens.txt')
    num_tokens = len(tokens)
    rand_list_tokens = list(range(num_tokens))
    random.shuffle(rand_list_tokens)

    messages = read_file(name+'Msg.txt')
    num_messages = len(messages)
    rand_list = list(range(num_messages))
    random.shuffle(rand_list)

    token = tokens[rand_list_tokens[token_count]].strip() # gets rid of the new line character on the end
    bot.switchAccount(token) # switchs to the new account
    print("Account switched to: " + token)

    token_count += 1
    if (token_count == num_tokens): 
        # resets the account count so if there are more accounts then messages it will cycle through them
        # this is a temp solution as it will need to be reshuffled at some point or else easy to see the pattern of messges
        token_count = 0
    if reply:

        bot.reply(CHANNELID, messageId, messages[rand_list[count]]) #this takes the channel id for where you want to send the message 
        print("Replying with: " + messages[rand_list[count]])
        last_message = ""
    else:
        bot.sendMessage(CHANNELID, messages[rand_list[count]]) #this takes the channel id for where you want to send the message 
        print("Sending: " + messages[rand_list[count]])
        last_message = messages[rand_list[count]]
    delete_line(name, rand_list[count], messages)
    
# gets the user info and channel
TOKEN = (read_file('config.txt')[0]).strip()
CHANNELID = (read_file('config.txt')[1]).strip()

# setting up counts for while loops
token_count = 0
adminMessages = read_file('adminMsg.txt')
adminCount = len(adminMessages) - 1

userMessages = read_file('userMsg.txt')
userCount = len(userMessages) - 1

secondMessages = read_file('secondUserMsg.txt')
secondUserCount = len(secondMessages) -1

bot = discum.Client(token=TOKEN, log=False) # discord token to login with

print("Started Text Spam")
# send inital admin message to start convo
bot.sendMessage(CHANNELID, "How are we all going??")
last_message = "How are we all going??"

# these loops deal with the actual sending and ordering of messages
# randomization makes sure that it doesnt sent all the messages at once

while adminCount >= 0:
    message('admin', adminCount, "", False)
    time.sleep(10)
    result = bot.searchMessages(CHANNELID, textSearch=last_message)
    lastMessageString = bot.filterSearchResults(result)
    lastMessageId = lastMessageString[0].get("id")
    adminCount -= 1
    time.sleep(1)

    while userCount >= (random.randint(0, userCount)+1):
        message('user', userCount, lastMessageId, True)
        userCount -= 1
        time.sleep(1)
        
        while secondUserCount >= (random.randint(0, secondUserCount)+1):
            print(secondUserCount) 
            message('secondUser', secondUserCount, lastMessageId, False)
            secondUserCount -= 1
            time.sleep(1)
            
# TO-DO
# USE AN IF STATEMENT TO GO TO 3RD DEPTH OF CONVERSATION
# NEED TO TIDY UP THE RANDOM IN THE WHILE LOOP AS ENDS ONE ITERATION EARLY
# SETUP GITHUB REPO