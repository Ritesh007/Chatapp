"""
This is a Console Chat application
Please read the prompts when you run the application
Type 'ch' for ----> Chat History
Type 'users' for ----> Users History
Type 'end' to ----> End the Chat
"""

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


# Chat content go here
# Child Class
class ChatTexts(ChatWelcome):
    texts = True

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

# Chat history
    @staticmethod
    def chat_history():
        chat_history_text = open("../../Chatapp/Chat_consoleapp/files/chat.txt","r")
        for chat_history_texts in chat_history_text:
             print (chat_history_texts)
        chat_history_text.close()

# Participant history
    @staticmethod
    def users_history():
        users_history_text = open("../../Chatapp/Chat_consoleapp/files/users.txt", "r")
        for users_history_texts in users_history_text:
            print(users_history_texts)
        users_history_text.close()

# Main Logic
    def enter_texts(self):
        self.store_users()
        while self.texts == True:
             text=input("Enter you text here with your name -> ")
             self.store_texts(text+"  "+str(datetime.now()))
             if text == "end":
                 print("Thank you the chat has ended; Please restart the application again to start the chat")
                 self.store_users_end()
                 self.texts=False
             elif text == "ch":
                 self.chat_history()
             elif text == "users":
                 self.users_history()

# Main block
def main():
    chat=ChatTexts()
    chat.enter_texts()

main()