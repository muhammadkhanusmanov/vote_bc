from django.contrib import admin
from .models import Poll,Vote


admin.site.register([Poll,Vote])
