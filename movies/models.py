from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = 'action', 'Action'
        COMEDY = 'comedy', 'Comedy'
        DRAMA = 'drama', 'Drama'
        HORROR = 'horror', 'Horror'
        ROMANCE = 'romance', 'Romance'
        SCI_FI = 'sci_fi', 'Sci-Fi'
        THRILLER = 'thriller', 'Thriller'
        WESTERN = 'western', 'Western'
        ANIMATION = 'animation', 'Animation'
        ADVENTURE = 'adventure', 'Adventure'
        FANTASY = 'fantasy', 'Fantasy'

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=30, choices=Genre.choices, blank=True)
    release_year = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1800), MaxValueValidator(2026)])
    rating = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)], choices=[(i, i) for i in range(1, 6)])
    watched = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        if self.release_year is None:
            return f"{self.title}"
        else:
            return f"{self.title} ({self.release_year})"