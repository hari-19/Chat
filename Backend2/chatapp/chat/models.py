from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .helper import get_chat_name
from django.db import transaction

User = get_user_model()

class Contact(models.Model):
    user = models.OneToOneField(User, related_name="contacts", on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    chat_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.chat_name

class Message(models.Model):
    chat = models.ForeignKey(Chat,related_name="messages", on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name='chat_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username

def on_transaction_commit(func):
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))

    return inner


@receiver(post_save, sender=Contact)
@on_transaction_commit
def create_chat(sender, instance ,**kwargs):
    user1 = instance.user
    friends = instance.friends

    if friends is None :
        return

    for friend in friends.all():
        chat_name = get_chat_name(user1, friend)
        if chat_name == None:
            continue
        chat = Chat.objects.get_or_create(chat_name=chat_name)

@receiver(post_save, sender=User)
def create_contact(sender, instance, created, **kwargs):
    if created:
        Contact.objects.get_or_create(user=instance)