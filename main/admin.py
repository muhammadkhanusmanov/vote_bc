from django.contrib import admin
from .models import Polls,Vote,Hujjat


admin.site.register(
    [Polls,Vote,Hujjat]
)
