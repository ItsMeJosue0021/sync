from django.contrib import admin
from .models import Post, PostImage, Attachment, Comment, Group, GroupMembership

# admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Attachment)
admin.site.register(Comment)
admin.site.register(Group)
admin.site.register(GroupMembership)
