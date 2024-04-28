from django.contrib import admin
from django.urls import path

from main.views import UserView,UserLogin,PollView,VoteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create/', UserView.as_view()),
    path('user/delete/', UserView.as_view()),
    path('user/login/', UserLogin.as_view()),
    path('poll/create/', PollView.as_view()),
    path('poll/delete/', PollView.as_view()),
    path('allpoll/get/', PollView.as_view()),
    path('polls/',VoteView.as_view()),
    path('get/poll/<str:id>',VoteView.as_view())
]
