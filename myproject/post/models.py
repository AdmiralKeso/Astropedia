from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField(max_length=400)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
content = models.TextField()
date_create = models.DateTimeField(auto_now_add=True)
STATUS = ((0, "Draft"), (1, "Published"))
status = models.IntegerField(choices=STATUS, default=0)