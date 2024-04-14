from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40, unique=True)
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    date_create = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name="upvote_posts", blank=True)
    downvotes = models.ManyToManyField(User, related_name="downvote_posts", blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmark_posts", blank=True)

    STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )
    status = models.IntegerField(choices=STATUS, default=0)

    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()