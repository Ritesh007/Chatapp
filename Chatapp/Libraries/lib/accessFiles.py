
from _datetime import datetime


# Welcome block Statements and logic go here
# Parent Class
class ChatWelcome():
    def __init__(self):
        print ("Welcome to the chat app")

    @staticmethod
    def participant():
        name1=input("Enter first participant name -> ")
        name2 = input("Enter second participant name -> ")
        return name1,name2


class AccessFiles(ChatWelcome):

# Writes to chat.txt
    @staticmethod
    def store_texts(text) :
        store_file=open("../../Chatapp/Chat_consoleapp/files/chat.txt","a")
        store_file.write(text+"\n")
        store_file.close()


# Writes to users.txt @Chat start
    def store_users(self):
        users = super().participant()
        users_file=open("../../Chatapp/Chat_consoleapp/files/users.txt","a")
        users_file.write("\n"+"  participant1 - {0}  participant2 - {1} ---> Chat started @ {2}" .format(users[0],users[1],datetime.now()))
        users_file.close()


# Writes to users.txt at Chat end
    @staticmethod
    def store_users_end():
        users_file = open("../../Chatapp/Chat_consoleapp/files/users.txt", "a")
        users_file.write("\n" + "---> Chat ended @ {0}".format(datetime.now()))
        users_file.close()

