from django.db import models
from loginapp.models import User
#from django.contrib.auth.models import User
# Create your models here.

class Video(models.Model):
    title=models.CharField(max_length=200)
    description= models.TextField()
    video=models.FileField(upload_to='videos',blank=False)
    channel= models.CharField(max_length=200)
    # ownnerimage=models.ImageField(upload_to='profile')
    keywords=models.TextField()
    slug=models.SlugField(null=True)
    user=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class Likevideo(models.Model):
    video_id=models.ForeignKey(Video,related_name="video_id",on_delete=models.CASCADE)
    like=models.BooleanField(default=False)
    dislike=models.BooleanField(default=False)
    userid=models.ForeignKey(User,related_name="userid", on_delete=models.CASCADE)
    def __str__(self):
        return self.userid.username
    
class Comment(models.Model):
    videoid=models.ForeignKey(Video,related_name="videoid",on_delete=models.CASCADE)
    comment=models.TextField()
    user_id=models.ForeignKey(User,related_name='user_id',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_id.username
    

class Reply(models.Model):
    commentid=models.ForeignKey(Comment,related_name="commentid",on_delete=models.CASCADE)
    reply=models.TextField()
    usersid=models.ForeignKey(User,related_name="usersid",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.usersid.username