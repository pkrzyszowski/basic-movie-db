from django.contrib import admin

from .models import Movie, Comment


admin.site.register([Movie, Comment])
