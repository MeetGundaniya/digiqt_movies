from django.contrib import admin
from movieapi.models import MovieDB

# Register your models here.

class MovieDBModelAdmin(admin.ModelAdmin):
  list_display = ('name', 'rating', 'release', 'duration')
  search_fields = ('name',)
  list_filter = ('rating',)



admin.site.register(MovieDB, MovieDBModelAdmin)