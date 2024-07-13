from django.shortcuts import render
from django.template import  loader
from .models import Movie

def index(request):
   movies = Movies.objects.order_by('type')
   template = loader.get_template('index.html')
   return HttpResponse(template.render({'movies':movies}, request))


def movie(request, movie_id):
    movie = Movie.objects.get(pk = pokemon_id)
    template = loader.get_template('display_movie.html')
    context = {
            'movie': movie
            }
    return HttpResponse(template.tender(context, request))
