from _datetime import datetime

#Welcome block Statements and logic go here
#Parent Class
class Chat_welcome():
    def __init__(self):
        print ("Welcome to the chat app")
    def participant(self):
        name1=input("Enter first participant name")
        name2 = input("Enter second participant name")

#Chat content go here
#Child Class
class Chat_texts(Chat_welcome):
    texts = True
    def store_texts(self,text) :
        store_file=open("../../Chatapp/Chat_consoleapp/files/chat.txt","a")
        store_file.write(text+"\n")
        store_file.close()

    def enter_texts(self):
        super().participant()
        while self.texts == True:
             text=input("Enter you text here with your name -> ")
             self.store_texts(text+"  "+str(datetime.now()))
             if text == "end":
                 print ("Thank you the chat has ended; Please the application again to start the chat")
                 self.texts=False

def main():
    chat=Chat_texts()
    chat.enter_texts();

main()