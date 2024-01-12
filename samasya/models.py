from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 10, unique=True, null=False, blank = False)
    email = models.EmailField(max_length = 35, unique = True, null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else None

    def username(self):
        return self.user.username if self.user else None


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    text = models.TextField()
    level = models.CharField(max_length = 250)
    category = models.CharField(max_length = 300)
    upvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.text[:100]}..."


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='posts')
    text = models.TextField()
    upvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.text[:50]}...'



