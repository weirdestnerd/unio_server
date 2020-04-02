from djongo import models


class Chat(models.Model):
    timestamp = models.DateTimeField(unique=True)
    message = models.TextField()
    isBotMessage = models.BooleanField()

    class Meta:
        abstract = True


class User(models.Model):
    username = models.CharField(max_length=50, default='default_username')
    chats = models.ArrayField(
        model_container=Chat
    )

    objects = models.DjongoManager()
