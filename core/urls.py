from django.contrib import admin
from django.urls import path

from main.views import UserView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create/', UserView.as_view()),
    path('user/delete/', UserView.as_view()),
]
