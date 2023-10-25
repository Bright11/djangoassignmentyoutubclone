from django.urls import path

from . import views

app_name="youtubeapp"
urlpatterns = [
    path("",views.index.as_view(),name='index'),
    path("upload/",views.upload.as_view(),name='upload'),
    path("watch/<slug:vwatch>/",views.watch.as_view(),name='watch'),
    path("likesvideo/<slug:likesvideo>/",views.likesvideo.as_view(),name='likesvideo'),
    path("reply/<int:pk>/",views.reply.as_view(),name="reply")
]
