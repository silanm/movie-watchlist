from .models import Movie
from .forms import MovieForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()  # Meta.ordering already newest-first
    q = request.GET.get("q", "").strip()
    if q:
        movies = movies.filter(title__icontains=q)
    return render(request, "movies/movie_list.html", {"movies": movies, "q": q})

def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie added successfully")
            return redirect("movie_list")
    else:
        form = MovieForm()
    return render(request, "movies/movie_form.html", {"form": form, "action": "Add", "button_text": "Add Movie"})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie updated successfully")
            return redirect("movie_list")
    else:
        form = MovieForm(instance=movie)
    return render(request, "movies/movie_form.html", {"form": form, "action": "Update", "button_text": "Update Movie"})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Movie deleted successfully")   
        return redirect("movie_list")
    return render(request, "movies/movie_confirm_delete.html", {"movie": movie})

def toggle_watched(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.watched = not movie.watched
        movie.save()
        messages.success(request, "Movie watched status toggled")
        return redirect("movie_list")
    else:
        return render(request, "movies/movie_confirm_toggle_watched.html", {"movie": movie})