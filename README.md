# Movie Watchlist

A Django app for managing a personal movie list. Add titles, search by name, rate them with stars, and mark movies as watched or unwatched.

## Stack

- Python 3.12
- Django 6.0
- PostgreSQL 18 (via Docker)
- Server-rendered templates with function-based views and `ModelForm`

## Features

- List movies (newest first)
- Search by title (`?q=`)
- Add, edit, and delete movies
- Optional 1-5 star rating (or leave unrated)
- Toggle watched status from the list
- Django Admin for browsing and filtering

## Project layout

```
movie-watchlist/
├── movie_watchlist/   # project settings and root URLs
├── movies/            # Movie model, views, forms, templates
├── manage.py
└── requirements.txt
```

## Prerequisites

- Docker and Docker Compose
- Shared virtualenv
- PostgreSQL container

## Setup

### 1. Start PostgreSQL

```bash
cd movie-watchlist
docker compose up -d
```

### 2. Activate the virtual environment

```bash
source .venv/bin/activate
```

Install dependencies if you have not already:

```bash
pip install -r requirements.txt
```

### 3. Create the database

```bash
docker exec -it postgres psql -U ... -d ... -c "CREATE DATABASE movie_watchlist;"
```

If the database already exists, skip this step.

### 4. Run migrations

```bash
cd movie-watchlist
python manage.py migrate
```

### 5. Create an admin user (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the watchlist and [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) for Django Admin.

## URLs


| URL                     | Name             | Description                     |
| ----------------------- | ---------------- | ------------------------------- |
| `/`                     | `movie_list`     | Watchlist and search            |
| `/add/`                 | `movie_create`   | Add a movie                     |
| `/<id>/edit/`           | `movie_update`   | Edit a movie                    |
| `/<id>/delete/`         | `movie_delete`   | Delete confirmation             |
| `/<id>/toggle-watched/` | `toggle_watched` | Toggle watched (POST from list) |
| `/admin/`               | -                | Django Admin                    |


## Movie model


| Field          | Type     | Notes                                 |
| -------------- | -------- | ------------------------------------- |
| `title`        | string   | Required                              |
| `genre`        | choice   | Optional; Action, Comedy, Drama, etc. |
| `release_year` | integer  | Optional; 1800-2026                   |
| `rating`       | integer  | Optional; 1-5                         |
| `watched`      | boolean  | Default `False`                       |
| `date_added`   | datetime | Set automatically                     |


`MovieForm` exposes `title`, `genre`, `release_year`, and `rating` only.

## Tests

```bash
python manage.py test movies
```



---

## Credits

Django application logic, models, views, forms, and tests were implemented by myself.
UI redesign, theming, templates, and CSS were created with AI assistance.