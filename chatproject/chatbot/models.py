from django.db import models

# Create your models here.

class Conversation(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user_input = models.TextField()
    bot_response = models.TextField()

    def __str__(self):
        return f"Conversation at {self.timestamp}"