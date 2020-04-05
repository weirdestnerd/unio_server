from djongo import models


class Chat(models.Model):
    timestamp = models.BigIntegerField(primary_key=True)
    message = models.TextField()
    isBotMessage = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(models.Model):
    username = models.CharField(max_length=50, default='default_username', unique=True)
    chats = models.ArrayField(
        model_container=Chat,
        unique=True
    )

    objects = models.DjongoManager()
