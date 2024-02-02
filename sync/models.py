from django.db import models
from django.contrib.auth.models import User

    
#=========================================================
# Post
#=========================================================

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
#=========================================================
# PostImage
#=========================================================

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='post_images/')

#=========================================================
# Attachment
#=========================================================

class Attachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='attachments/')

    
#=========================================================
# Comment
#=========================================================

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.post.title}"
    
#=========================================================
# Group
#=========================================================
    
class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='group_memberships') 

    def __str__(self):
        return self.name
    
#=========================================================
# GroupMembership
#=========================================================

class GroupMembership(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} in {self.group.name}"
     