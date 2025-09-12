from django.contrib.auth.models import User    # Django's built in User model
from django.db import models

# Create your models here.

class Conversation(models.Model):
    # Link each conversation to a specific user 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    # ForeignKey means "this conversation belongs to one user"
    # on_delete=models.CASCADE means "if user is deleted, delete their conversations too"
    # null=True, blank=True means "this field can be empty" (for backward compatibility)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_input = models.TextField()
    bot_response = models.TextField()

    def __str__(self):
        return f"Conversation by {self.user.username if self.user else 'Anonymous'} at {self.timestamp}"
    
    class Meta:
        ordering = ['-timestamp']  # Always show newest conversations first


# Optional : Srore extra user information
class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # OneToOneField means "each user has exactly one profile"

    # Extra fields we can add
    preferred_language = models.CharField(max_length=10, default='en')
    chat_theme = models.CharField(max_length=20, default='light')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Profile for {self.user.username}"