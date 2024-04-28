from django.contrib import admin
from django.urls import path

from main.views import UserView,UserLogin,PollView,VoteView,PollStatistics,get_all_users,cd_file,SaveFile,get_files



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create/', UserView.as_view()),
    path('user/delete/', UserView.as_view()),
    path('user/login/', UserLogin.as_view()),
    path('poll/create/', PollView.as_view()),
    path('poll/delete/', PollView.as_view()),
    path('allpoll/get/', PollView.as_view()),
    path('polls/',VoteView.as_view()),
    path('get/poll/<str:id>',VoteView.as_view()),
    path('vote/poll/',VoteView.as_view()),
    path('poll/statistic/',PollStatistics.as_view()),
    path('get/all/users/',get_all_users),
    path('add/file/',cd_file,name='cre'),
    path('delete/file/',cd_file,name='del'),
    path('save/<str:id>',SaveFile.as_view()),
    path('allfiles/',get_files)
]
