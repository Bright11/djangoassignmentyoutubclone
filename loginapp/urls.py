from django.urls import path

from . import views

app_name="loginapp"
urlpatterns = [
    path('register/',views.register.as_view(),name="register"),
    path("logoutuser/",views.logoutuser,name="logoutuser"),
]
