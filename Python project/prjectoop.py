from datetime import datetime

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        self.chatroom = chatroom
        chatroom.add_user(self)
        print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if self.chatroom:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if self.chatroom:
            message = Message(self, content)
            self.chatroom.broadcast_message(message)
        else:
            print(f"{self.username} is not in a chatroom!")


class Message:
    def __init__(self, sender, content):
        self.sender = sender.username
        self.content = content
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%H:%M:%S')}] {self.sender}: {self.content}"


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast_message(self, message):
        self.messages.append(message)
        for user in self.users:
            print(message)

    def view_history(self):
        print(f"--- Chat History of {self.name} ---")
        for msg in self.messages:
            print(msg)

            # Create chatroom
chatroom = ChatRoom("Gaming Room")

# Create users
mahesh = User("Mahesh")
sir = User("Sir")

# Users join chatroom
mahesh.join_chatroom(chatroom)
sir.join_chatroom(chatroom)

# Sending messages
mahesh.send_message("Hello everyone!")
sir.send_message("Hey Mahesh, ready for BGMI?")

# View chat history
chatroom.view_history()

# User leaves
mahesh.leave_chatroom()