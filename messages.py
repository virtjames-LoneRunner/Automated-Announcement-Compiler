from itertools import islice
from fbchat import Client
from fbchat.models import *
from getpass import getpass
from time import sleep

from sys import argv, exit
import csv

from cs50 import SQL

import logging

#logging.getLogger("client").setLevel(logging.WARNING)

# Print an error message if the right number of arguments is not provided
if len(argv) != 2:
    print("Usage: messages.py [CSV Filename]")
    #exit(1)
    pass

faculty_file = "trial.csv"

with open(faculty_file, 'r') as csv_file:
    cursor = csv.DictReader(csv_file)

    data_list = []

    # Appends each dictionary into a list for looping and indexing
    for row in cursor:
        data_list.append(row)

f_write = open("log.txt", 'a')

faculty_with_id = []

user = input("Enter Your Username or Email:")
password = getpass("Enter your password(For safety purposes your password will either be shown as asterisks or not at all):")

client = Client(user, password)

#Previous messages
#prev_messages_db = SQL("sqlite:///messages.db")
#prev_messages = prev_messages_db.execute("SELECT * FROM messages")

messages = {}

#for prev_message in prev_messages:
#    messages[prev_message["Subject"]] = prev_message["Text"]

print (data_list[0])
print (data_list[0]["GroupChatID"])
#print (data_list[1])
#print (data_list[1]["GroupChatID"])

while True:

    #try:
    for item in data_list:

        sleep(5)

        thread_id = item["GroupChatID"]
        thread_type = ThreadType.GROUP

        print("Listening for messages from: " + item["Name"] +  " on group chat: " + item["Subject"])

        message = client.fetchThreadMessages(thread_id, limit=1)
        message_1 = message[0]
        message = message[0]
        accepted = True

        if message_1.author != item["UID"]:
            accepted = False
            print(item["Name"])
            print("Does not match user ID")
            break
       
        if messages[item["Subject"]] != message.text:
            messages[item["Subject"]] = message.text
            #message = message[0]

            print(message.text + '\n' + ' -' + item["Name"])
            
            message_to_send = message.text + '\n' + ' -' + item["Name"]
            f_write.write(message_to_send + '\n')

            client.send(Message(text=message_to_send), thread_id=thread_id, thread_type=thread_type)
            
        else:
            print("No new updates from " + item["Subject"])
    #except:
    #    print("An error has occured, please try again.")
    #    exit(1)
