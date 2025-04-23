from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    # This creates a many-to-one relationship with the User model
    # If the user gets deleted, all their tweets will also be deleted (on_delete=models.CASCADE).
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/',blank=True , null=True) #blank=True allows the field to be left empty in forms, and null=True allows it to be empty in the database.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f'{self.user.username} - {self.text[:10]}'  # It defines how the object will be shown in places like the Django admin panel or the shell. It returns a string like: aryen - This is my (first 10 characters of the tweet).

        
 