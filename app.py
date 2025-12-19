from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Comprehensive Book Database
BOOKS = [
    # Fiction
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "fiction",
        "pages": 324,
        "rating": 4.8,
        "description": "A gripping tale of racial injustice and childhood innocence in the American South.",
        "moods": ["thoughtprovoking", "emotional"],
        "themes": ["justice", "morality", "racism"]
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "genre": "fiction",
        "pages": 328,
        "rating": 4.7,
        "description": "A dystopian social science fiction novel and cautionary tale about totalitarianism.",
        "moods": ["thoughtprovoking", "thrilling"],
        "themes": ["surveillance", "freedom", "control"]
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "fiction",
        "pages": 180,
        "rating": 4.5,
        "description": "A portrait of the Jazz Age in all of its decadence and excess.",
        "moods": ["emotional", "thoughtprovoking"],
        "themes": ["wealth", "love", "american dream"]
    },
    # Mystery & Thriller
    {
        "id": 4,
        "title": "The Girl with the Dragon Tattoo",
        "author": "Stieg Larsson",
        "genre": "mystery",
        "pages": 465,
        "rating": 4.6,
        "description": "A journalist and a hacker investigate a woman's disappearance in this gripping thriller.",
        "moods": ["thrilling", "adventurous"],
        "themes": ["mystery", "crime", "investigation"]
    },
    {
        "id": 5,
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "genre": "mystery",
        "pages": 432,
        "rating": 4.5,
        "description": "A psychological thriller about a woman who goes missing on her anniversary.",
        "moods": ["thrilling", "thoughtprovoking"],
        "themes": ["marriage", "deception", "mystery"]
    },
    {
        "id": 6,
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "mystery",
        "pages": 489,
        "rating": 4.3,
        "description": "A murder in the Louvre leads to a discovery that could rock the foundations of Christianity.",
        "moods": ["thrilling", "adventurous"],
        "themes": ["conspiracy", "history", "religion"]
    },
    # Fantasy
    {
        "id": 7,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "fantasy",
        "pages": 310,
        "rating": 4.8,
        "description": "A hobbit's unexpected journey to reclaim a treasure guarded by a dragon.",
        "moods": ["adventurous", "lighthearted"],
        "themes": ["adventure", "courage", "friendship"]
    },
    {
        "id": 8,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "fantasy",
        "pages": 309,
        "rating": 4.9,
        "description": "A young wizard's first year at Hogwarts School of Witchcraft and Wizardry.",
        "moods": ["adventurous", "lighthearted"],
        "themes": ["magic", "friendship", "good vs evil"]
    },
    {
        "id": 9,
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "genre": "fantasy",
        "pages": 662,
        "rating": 4.7,
        "description": "The tale of Kvothe, a legendary figure's journey from student to renowned magician.",
        "moods": ["adventurous", "emotional"],
        "themes": ["magic", "revenge", "legend"]
    },
    # Science Fiction
    {
        "id": 10,
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "scifi",
        "pages": 688,
        "rating": 4.6,
        "description": "A sweeping tale of desert planet Arrakis and the valuable resource that brings power.",
        "moods": ["adventurous", "thoughtprovoking"],
        "themes": ["power", "ecology", "politics"]
    },
    {
        "id": 11,
        "title": "The Martian",
        "author": "Andy Weir",
        "genre": "scifi",
        "pages": 369,
        "rating": 4.7,
        "description": "An astronaut's fight for survival after being stranded alone on Mars.",
        "moods": ["adventurous", "inspiring"],
        "themes": ["survival", "science", "perseverance"]
    },
    {
        "id": 12,
        "title": "Neuromancer",
        "author": "William Gibson",
        "genre": "scifi",
        "pages": 271,
        "rating": 4.4,
        "description": "A hacker and his crew take on a dangerous heist in cyberspace.",
        "moods": ["thrilling", "thoughtprovoking"],
        "themes": ["technology", "ai", "cyberpunk"]
    },
    # Romance
    {
        "id": 13,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "romance",
        "pages": 279,
        "rating": 4.7,
        "description": "A classic tale of love and misunderstanding in Georgian England.",
        "moods": ["emotional", "lighthearted"],
        "themes": ["love", "society", "pride"]
    },
    {
        "id": 14,
        "title": "The Notebook",
        "author": "Nicholas Sparks",
        "genre": "romance",
        "pages": 214,
        "rating": 4.6,
        "description": "An enduring love story that spans decades and challenges.",
        "moods": ["emotional", "inspiring"],
        "themes": ["love", "memory", "devotion"]
    },
    {
        "id": 15,
        "title": "Me Before You",
        "author": "Jojo Moyes",
        "genre": "romance",
        "pages": 369,
        "rating": 4.5,
        "description": "A moving story about love, loss, and living life to the fullest.",
        "moods": ["emotional", "thoughtprovoking"],
        "themes": ["love", "choice", "life"]
    },
    # Biography
    {
        "id": 16,
        "title": "Steve Jobs",
        "author": "Walter Isaacson",
        "genre": "biography",
        "pages": 656,
        "rating": 4.6,
        "description": "The exclusive biography of the Apple co-founder and tech visionary.",
        "moods": ["inspiring", "thoughtprovoking"],
        "themes": ["innovation", "business", "technology"]
    },
    {
        "id": 17,
        "title": "Educated",
        "author": "Tara Westover",
        "genre": "biography",
        "pages": 334,
        "rating": 4.8,
        "description": "A memoir about a woman who grows up in a survivalist family and goes on to earn a PhD.",
        "moods": ["inspiring", "emotional"],
        "themes": ["education", "family", "perseverance"]
    },
    {
        "id": 18,
        "title": "The Diary of a Young Girl",
        "author": "Anne Frank",
        "genre": "biography",
        "pages": 283,
        "rating": 4.7,
        "description": "Anne Frank's diary during the Holocaust, a testament to the human spirit.",
        "moods": ["emotional", "thoughtprovoking"],
        "themes": ["war", "hope", "humanity"]
    },
    # Self-Help
    {
        "id": 19,
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "selfhelp",
        "pages": 320,
        "rating": 4.8,
        "description": "Practical strategies for building good habits and breaking bad ones.",
        "moods": ["inspiring", "thoughtprovoking"],
        "themes": ["habits", "productivity", "improvement"]
    },
    {
        "id": 20,
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen Covey",
        "genre": "selfhelp",
        "pages": 381,
        "rating": 4.7,
        "description": "A holistic approach for solving personal and professional problems.",
        "moods": ["inspiring", "thoughtprovoking"],
        "themes": ["effectiveness", "leadership", "principles"]
    },
    {
        "id": 21,
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "genre": "selfhelp",
        "pages": 499,
        "rating": 4.6,
        "description": "Explores the two systems that drive the way we think and make decisions.",
        "moods": ["thoughtprovoking"],
        "themes": ["psychology", "decision-making", "cognition"]
    },
    # History
    {
        "id": 22,
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "genre": "history",
        "pages": 443,
        "rating": 4.7,
        "description": "A narrative history of humanity from the Stone Age to the modern age.",
        "moods": ["thoughtprovoking", "inspiring"],
        "themes": ["evolution", "civilization", "humanity"]
    },
    {
        "id": 23,
        "title": "The Immortal Life of Henrietta Lacks",
        "author": "Rebecca Skloot",
        "genre": "history",
        "pages": 381,
        "rating": 4.6,
        "description": "The story of a woman whose cells revolutionized medicine without her knowledge.",
        "moods": ["thoughtprovoking", "emotional"],
        "themes": ["science", "ethics", "medical history"]
    },
    {
        "id": 24,
        "title": "Guns, Germs, and Steel",
        "author": "Jared Diamond",
        "genre": "history",
        "pages": 528,
        "rating": 4.5,
        "description": "An examination of how geography shaped human history and civilization.",
        "moods": ["thoughtprovoking"],
        "themes": ["civilization", "geography", "society"]
    },
]

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_books():
    """Get all books"""
    return jsonify({
        'books': BOOKS,
        'total': len(BOOKS)
    })

@app.route('/api/recommend', methods=['GET'])
def recommend_books():
    """Get personalized book recommendations based on preferences"""
    genre = request.args.get('genre', '').lower()
    mood = request.args.get('mood', '').lower()
    length = request.args.get('length', '').lower()
    
    recommendations = []
    
    for book in BOOKS:
        score = 0
        max_score = 0
        
        # Genre matching (40 points)
        if genre:
            max_score += 40
            if book['genre'] == genre:
                score += 40
        
        # Mood matching (40 points)
        if mood:
            max_score += 40
            if mood in book['moods']:
                score += 40
        
        # Length preference (20 points)
        if length:
            max_score += 20
            if length == 'short' and book['pages'] < 300:
                score += 20
            elif length == 'medium' and 300 <= book['pages'] <= 500:
                score += 20
            elif length == 'long' and book['pages'] > 500:
                score += 20
        
        # Calculate match percentage
        if max_score > 0:
            match_percentage = int((score / max_score) * 100)
            
            # Only include books with at least 50% match
            if match_percentage >= 50:
                book_copy = book.copy()
                book_copy['match_score'] = match_percentage
                recommendations.append(book_copy)
    
    # Sort by match score and rating
    recommendations.sort(key=lambda x: (x['match_score'], x['rating']), reverse=True)
    
    # Return top 6 recommendations
    return jsonify({
        'recommendations': recommendations[:6],
        'total': len(recommendations),
        'preferences': {
            'genre': genre,
            'mood': mood,
            'length': length
        }
    })

@app.route('/api/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Get a specific book by ID"""
    book = next((b for b in BOOKS if b['id'] == book_id), None)
    
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    return jsonify({'book': book})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)