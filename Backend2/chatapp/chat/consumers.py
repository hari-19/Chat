import json
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .helper import get_chat_name, get_chat_name_id

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def add_to_group(self):
        self.user = self.scope['user']
        friends = self.user.contacts.friends

        chat_name = get_chat_name(self.user, self.user)
        async_to_sync(self.channel_layer.group_add)(chat_name, self.channel_name)
        
        friends = friends.all()

        for friend in friends:
            chat_name = get_chat_name(self.user, friend)
            async_to_sync(self.channel_layer.group_add)(chat_name, self.channel_name)

    def remove_from_group(self):
        self.user = self.scope['user']
        friends = self.user.contacts.friends
        
        chat_name = get_chat_name(self.user, self.user)
        async_to_sync(self.channel_layer.group_discard)(chat_name, self.channel_name)

        friends = friends.all()
       
        for friend in friends:
            chat_name = get_chat_name(self.user, friend)
            async_to_sync(self.channel_layer.group_discard)(chat_name, self.channel_name)

    def connect(self):
        self.add_to_group()      
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        self.remove_from_group()

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print("Hello")
        print(text_data_json)

        try:
            chat_name = text_data_json['chat_name']
        except Exception as e:
            print(str(e))
            None

        try:
            to_id = text_data_json['to_id']
            chat_name = get_chat_name_id(int(self.user.id), int(to_id))
            print(chat_name)
        except Exception as e:
            print(str(e))
            None

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

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'chat_name': chat_name
        }))