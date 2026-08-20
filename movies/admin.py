from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_year', 'rating', 'watched']
    list_filter = ['genre', 'release_year', 'watched']
    search_fields = ['title', 'genre']