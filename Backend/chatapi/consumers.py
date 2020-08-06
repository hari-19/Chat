import json
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .helper import get_chat_name

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def add_to_group(self):
        self.user = self.scope['user']
        friends = self.user.contacts.friends
        print(self.user)
        print(friends)
        if friends == None:
            print("reached")
            return
        
        friends = friends.all()

        print(friends)

        for friend in friends:
            print("1")
            chat_name = get_chat_name(self.user, friend)
            print(chat_name)
            print(self.channel_name)
            try:
                async_to_sync(self.channel_layer.group_add)(chat_name, self.channel_name)
                # print(self.channel_layer.group_add(chat_name, self.channel_name))
            except Exception as e:
                print(str(e))

    def remove_from_group(self):
        self.user = self.scope['user']
        friends = self.user.contacts.friends
        if friends == None:
            return
        
        friends = friends.all()
       
        for friend in friends:
            chat_name = get_chat_name(self.user, friend)
            async_to_sync(self.channel_layer.group_discard)(chat_name, self.channel_name)

    def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = 'chat_%s' % self.room_name
        # async_to_sync(self.channel_layer.group_add)('test', self.channel_name)

        self.add_to_group()
        
        self.accept()

    def disconnect(self, close_code):

        # Leave room group
        self.remove_from_group()

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("Recieved")
        message = text_data_json['message']
        chat_name = text_data_json['chat_name']

        print(message)
        print(chat_name)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            chat_name,
            {
                'type': 'chat_message',
                'message': message,
                'chat_name': chat_name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        chat_name = event["chat_name"]
        print("reached")

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'chat_name': chat_name
        }))