from django.db import models

class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors={}
        if len(post_data['first_name'])<2:
            errors['first_name']= "First name must be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name']= "Last name must be at least 2 characters"
        if len(post_data['email']) == 0:
            errors['email']="Email must be provided"
        if len(post_data['password']) ==0:
            errors['password']="Password must be provided"
        emails_query = self.filter(email=post_data['email'])
        if len(emails_query) >0:
            errors['email'] = "User with that email already exists"
        if post_data['password'] != post_data['password_confirmation']:
            errors['password_confirmation'] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    objects = UserManager()

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages")
    content=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user=models.ForeignKey(User, related_name="comments")
    message=models.ForeignKey(Message, related_name="comments")
    content=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    



