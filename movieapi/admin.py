from django.contrib import admin
from movieapi.models import MovieDB

# Register your models here.

class MovieDBModelAdmin(admin.ModelAdmin):
  pass



admin.site.register(MovieDB, MovieDBModelAdmin)