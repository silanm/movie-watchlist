from django import forms
from .models import Movie


class StarRatingWidget(forms.RadioSelect):
    template_name = 'movies/widgets/star_rating.html'
    option_template_name = 'movies/widgets/star_rating_option.html'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year', 'rating']
        widgets = {
            'rating': StarRatingWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['genre'].choices = [('', 'Select genre')] + list(Movie.Genre.choices)
        self.fields['rating'].choices = [(i, str(i)) for i in range(5, 0, -1)]
        self.fields['rating'].required = False
        self.fields['title'].widget.attrs['placeholder'] = 'Movie title'
        self.fields['release_year'].widget = forms.NumberInput(attrs={
            'class': 'field-input',
            'min': 1800,
            'max': 2026,
            'placeholder': 'e.g. 2000',
        })
        for name, field in self.fields.items():
            if name == 'rating':
                continue
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'field-select'
            else:
                field.widget.attrs.setdefault('class', 'field-input')