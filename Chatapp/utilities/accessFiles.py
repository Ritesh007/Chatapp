
from datetime import datetime
import os

# Welcome block Statements
# Parent Class
class ChatWelcome():
    def __init__(self):
        print ("Welcome to the chat app")

    @staticmethod
    def participant():
        name1=input("Enter first participant name -> ")
        name2 = input("Enter second participant name -> ")
        return name1,name2


# Child Class to access and write to the files
class AccessFiles(ChatWelcome):

# Writes to chat.txt
    @staticmethod
    def store_texts(text) :
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '..\\files\\chat.txt')
        store_file=open(filename,"a")
        store_file.write(text+"\n")
        store_file.close()


# Writes to users.txt @Chat start
    def store_users(self):
        users = super().participant()
        users_file=open("../Chatapp/Chatapp/files/users.txt","a")
        users_file.write("\n"+"  participant1 - {0}  participant2 - {1} ---> Chat started @ {2}" .format(users[0],users[1],datetime.now()))
        users_file.close()


# Writes to users.txt @Chat end
    @staticmethod
    def store_users_end():
        users_file = open("../Chatapp/Chatapp/files/users.txt", "a")
        users_file.write("\n" + "---> Chat ended @ {0}".format(datetime.now()))
        users_file.close()

#Lambda funtion to return a thank you note
    thankyou_note = lambda *args: str(args[0])