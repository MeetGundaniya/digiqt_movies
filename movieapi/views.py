from multiprocessing import context
from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from movieapi.models import MovieDB

# Create your views here.

class API(View):
  
  def get(self, request, **kwargs):
    context = []
    
    for row in MovieDB.objects.filter(name=kwargs['movie_name']):
      context.append({
        "movie_name": row.name, 
        "movie_rating": row.rating,
        "Mydate": row.release,
        "movie_duration": row.duration,
        "movie_desc": row.description
      })
    return JsonResponse({'data':context})