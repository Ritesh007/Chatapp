
class History():

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