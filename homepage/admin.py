from django.contrib import admin

from homepage.models import Topic, Comment, Tag

admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Tag)