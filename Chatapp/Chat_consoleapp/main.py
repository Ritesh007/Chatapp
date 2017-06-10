
"""
This is a Console Chat application
Please read the prompts when you run the application
Type 'ch' for ----> Chat History
Type 'users' for ----> Users History
Type 'end' to ----> End the Chat
-----> environment variable to change syspath permanently :-
Simply add this path to your PYTHONPATH environment variable.
To do this, go to Control Panel / System / Advanced / Environment variable,
and in the 'User variables' sections, check if you already have PYTHONPATH.
If yes, select it and click 'Edit', if not, click 'New' to add it.
here it is - PYTHONPATH : C:\\Users\\Kuchukulla\\PycharmProjects\\Python\\Chatapp\\Libraries\\lib
Paths in PYTHONPATH should be separated with ;
"""

# -----> To modify syspath in code :-
#import sys
#sys.path.append("C:\\Users\\Kuchukulla\\PycharmProjects\\Python\\Chatapp\\Libraries\\lib")

from _datetime import datetime
from history import History
from accessFiles import AccessFiles


# Chat content go here
# Child Class
class ChatTexts():
    texts = True

# Main Logic
    def enter_texts(self):
        accessFiles=AccessFiles()
        accessFiles.store_users()
        while self.texts == True:
             text=input("Enter you text here with your name -> ")
             AccessFiles.store_texts(text+"  "+str(datetime.now()))
             if text == "end":
                 print("Thank you the chat has ended; Please restart the application again to start the chat")
                 AccessFiles.store_users_end()
                 self.texts=False
             elif text == "ch":
                 History.chat_history()
             elif text == "users":
                 History.users_history()

# Main block
def main():
    chat=ChatTexts()
    chat.enter_texts()

main()