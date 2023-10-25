from django.contrib import admin
from .models import Video,Comment,Likevideo,Reply
# Register your models here.

admin.site.register([Video,Comment,Likevideo,Reply])