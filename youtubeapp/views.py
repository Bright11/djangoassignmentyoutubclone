from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth import get_user
from .forms import VideoForm,ReplyForm
from .models import Video, Likevideo,Comment
import uuid
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

class index(View):
    def get(sef,request):
        name="django youtubeclone"
        video=Video.objects.all()
        constext={"title":"Youtube clone","name":name,"video":video}
        return render(request,"pages/index.html",constext)
    


class upload(View):
    def get(self,request):
        videoform=VideoForm()
        context={'videoform':videoform}
        return render(request,'pages/upload.html',context)
        

    def post(self,request):
       # user= get_user(request)
        savevideo=VideoForm(request.POST,request.FILES)
       
        if savevideo.is_valid():
            print("valide")
            video=savevideo.save(commit=False)
            video.user=request.user
            video.slug=str(uuid.uuid4()).replace("-", "")
            video.save()
            messages.success(request,"Video submited")
            return redirect('youtubeapp:upload')
        #pass


class watch(View):
    def get(self,request,vwatch):
        video=get_object_or_404(Video,slug=vwatch)
        user_has_liked = Likevideo.objects.filter(userid=request.user.id, video_id=video.id).exists()
        comment=Comment.objects.filter(videoid=video).order_by("created_at") #getting videos comment
        replyform=ReplyForm()
        

        #likes=get_object_or_404(Likevideo, video.video_id)
        #print("pk is",video.id)
        context={"title":"watch","video":video,"likes":user_has_liked,"comment":comment,"replyform":replyform}
        return render(request,'pages/watch.html',context)

    def post(self,request,vwatch):
        pass

        #pass


class likesvideo(View):
    def get(self,request,likesvideo):
        referer = request.META.get('HTTP_REFERER')
        if referer:
            video=get_object_or_404(Video,slug=likesvideo)
            checklike=Likevideo.objects.filter(userid=request.user.id, video_id=video.id).exists()
            if checklike:
                 return redirect(referer)

            else:
                liksvideo=Likevideo.objects.create(
                    like=True,
                    userid=request.user,
                    video_id=video
                )
                liksvideo.save()
                return redirect(referer)
           
        else:
            return redirect("youtubeapp:index")
        #pass

    def post(self,request,likesvideo):
        
        referer = request.META.get('HTTP_REFERER')
        video=get_object_or_404(Video,slug=likesvideo)
        if referer:
             comment=Comment.objects.create(
                 comment=request.POST.get('comment'),
                 user_id=request.user,
                 videoid=video
             )
             comment.save()
             return redirect(referer)
        


class reply(View):
    def post(self,request,pk):
        referer = request.META.get('HTTP_REFERER')
       # video=get_object_or_404(Video,slug=vwatch)
        comment=get_object_or_404(Comment,pk=pk)
        replyform=ReplyForm(request.POST)
        if replyform.is_valid():
            print("valid")
            reply=replyform.save(commit=False)
            reply.usersid=request.user
            reply.commentid=comment
            reply.save()
            return redirect(referer)