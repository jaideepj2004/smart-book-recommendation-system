# Smart Book Recommendation System

An intelligent **book recommendation web app** built with **Flask** and a rule-based scoring algorithm. Users select their preferred genre, reading mood, and book length, and the app scores every book in the database and returns the top matches.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Book Catalogue](#book-catalogue)
- [Recommendation Algorithm](#recommendation-algorithm)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Setup & Running](#setup--running)

---

## Overview

The system hosts a catalogue of **24 curated books** across 8 genres. Users filter by genre, mood, and length preference — the app scores each book against these preferences on a 100-point scale and returns up to 6 best-matching recommendations.

---

## Features

- 24 books across genres: Fiction, Mystery, Fantasy, Sci-Fi, Romance, Biography, Self-Help, History
- Mood-based filtering: thoughtprovoking, emotional, adventurous, thrilling, inspiring, lighthearted
- Length preference: Short (<300 pages), Medium (300–500), Long (>500)
- Weighted scoring system (Genre 40%, Mood 40%, Length 20%)
- REST JSON API + HTML/CSS frontend
- CORS-enabled (Flask-CORS)

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| CORS | Flask-CORS |
| Frontend | HTML, CSS, JavaScript (`templates/`, `static/`) |
| Data Store | In-memory Python list (no database) |

---

## Book Catalogue

| Genre | Example Titles |
|---|---|
| Fiction | To Kill a Mockingbird, 1984, The Great Gatsby |
| Mystery | Gone Girl, The Da Vinci Code, The Girl with the Dragon Tattoo |
| Fantasy | The Hobbit, Harry Potter, The Name of the Wind |
| Sci-Fi | Dune, The Martian, Neuromancer |
| Romance | Pride and Prejudice, The Notebook, Me Before You |
| Biography | Steve Jobs, Educated, The Diary of a Young Girl |
| Self-Help | Atomic Habits, The 7 Habits, Thinking Fast and Slow |
| History | Sapiens, Guns Germs and Steel, The Immortal Life of Henrietta Lacks |

---

## Recommendation Algorithm

Each book receives a **match score (0–100)**:

```
Genre match     →  +40 points (if genre == selected genre)
Mood match      →  +40 points (if selected mood in book.moods list)
Length match    →  +20 points (short: <300 | medium: 300–500 | long: >500 pages)
```

Only books with ≥ 50% match are shown. Results are sorted by match score (primary) and rating (secondary). Top 6 are returned.

---

## Project Structure

```
smart-book-recommendation-system/
├── app.py               # Flask app + book database + recommendation logic
├── requirements.txt     # Dependencies (flask, flask-cors)
├── templates/
│   └── index.html       # Web UI
├── static/              # CSS / JS assets
├── .gitignore
└── README.md
```

---

## API Reference

### `GET /`
Returns the main UI.

### `GET /api/books`
Returns all 24 books.
```json
{ "books": [...], "total": 24 }
```

### `GET /api/recommend?genre=fantasy&mood=adventurous&length=medium`
Returns up to 6 matched books with `match_score`.

**Query params:**

| Param | Values |
|---|---|
| `genre` | fiction, mystery, fantasy, scifi, romance, biography, selfhelp, history |
| `mood` | thoughtprovoking, emotional, adventurous, thrilling, inspiring, lighthearted |
| `length` | short, medium, long |

### `GET /api/book/<id>`
Returns a single book by its integer ID.

---

## Setup & Running

```bash
git clone https://github.com/jaideepj2004/smart-book-recommendation-system.git
cd smart-book-recommendation-system
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.
