# Launder
# choose which function to run
# 11/02/22

# import react as react
import main
import react
import spam

print(" _                           _           ")
print("| |                         | |          ")
print("| |     __ _ _   _ _ __   __| | ___ _ __ ")
print("| |    / _` | | | | '_ \ / _` |/ _ \ '__|")
print("| |___| (_| | |_| | | | | (_| |  __/ |   ")
print("|______\__,_|\__,_|_| |_|\__,_|\___|_|")
print("For the message react press 1")
print("For the conversation creator press 2")
print("For the message spam press 3")
id = int(input("id:"))

if (id==1):
    react.main()

if (id==2):
    main.main()

if (id==3):
    spam.main()

# TO-DO 
# CAN USE THIS TO CREATE MULTITHREADING
