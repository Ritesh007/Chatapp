
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

from datetime import datetime
from Chatapp.utilities.accessFiles import AccessFiles
from Chatapp.utilities import history


# Main Logic
class ChatTexts():
    texts = True

    def enter_texts(self):
     try:
        accessFiles = AccessFiles()
        accessFiles.store_users()
        while self.texts == True:
             text=input("Enter you text here with your name -> ")
             AccessFiles.store_texts(text+"  "+str(datetime.now()))
             if text == "end":
                 a=AccessFiles.thankyou_note("Thank you the chat has ended; Please restart the application again to start the chat")
                 print(a)
                 AccessFiles.store_users_end()
                 self.texts=False
             elif text == "ch":
                 history.History.chat_history()
             elif text == "users":
                 history.History.users_history()
     except Exception as e:
        print("OOPS something went wrong!!..Check out the Exception ---> "+e)
     finally:
         print("FAILED OR PASSED the code has completed execution")


# Main block
def main():
    chat=ChatTexts()
    chat.enter_texts()

if __name__ == "__main__":
    main()