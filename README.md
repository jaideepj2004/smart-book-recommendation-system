# Smart Book Recommendation System 📚

An intelligent book recommendation system that provides **personalized book suggestions** based on your reading preferences. Built with a modern frontend (HTML/CSS/JS) and a powerful Flask backend.

## ✨ Features

### 🎯 **Personalized Recommendations**
- Select your favorite genre (Fiction, Mystery, Fantasy, Sci-Fi, Romance, Biography, Self-Help, History)
- Choose your reading mood (Inspiring, Thrilling, Emotional, Lighthearted, Thought-Provoking, Adventurous)
- Set your preferred book length (Short, Medium, Long)
- Get **intelligent recommendations** with match percentage scores

### 🔍 **Browse & Search**
- View all 24 curated books in the library
- Real-time search by title or author
- Filter by genre
- Beautiful card-based UI with ratings and descriptions

### 🧠 **Smart Algorithm**
Our recommendation engine uses a scoring system that considers:
- **Genre matching** (40% weight) - Matches your preferred genre
- **Mood matching** (40% weight) - Aligns with your current reading mood
- **Length preference** (20% weight) - Respects your time commitment
- Only shows books with **50%+ match** to ensure quality recommendations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jaideepj2004/smart-book-recommendation-system.git
   cd smart-book-recommendation-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📖 How to Use

### Getting Recommendations

1. **Select Your Preferences:**
   - Choose a genre from the dropdown
   - Pick a mood that matches what you're looking for
   - Optionally select book length preference

2. **Click "Get Recommendations"**
   - The system analyzes all books against your preferences
   - Returns top 6 matches with percentage scores
   - Each book shows why it's a good match for you

3. **Browse Results:**
   - See match percentage badges (e.g., "⭐ 100% Match")
   - View book details: title, author, rating, description
   - Match score bar at the bottom shows compatibility

### Sample Inputs to Try:

**For Adventure Lovers:**
- Genre: Fantasy
- Mood: Adventurous
- Length: Any
→ Get books like "The Hobbit", "Harry Potter"

**For Deep Thinkers:**
- Genre: History  
- Mood: Thought-Provoking
- Length: Medium/Long
→ Get books like "Sapiens", "Guns, Germs, and Steel"

**For Quick Reads:**
- Genre: Romance
- Mood: Emotional
- Length: Short
→ Get books like "The Notebook", "Pride and Prejudice"

**For Thrill Seekers:**
- Genre: Mystery & Thriller
- Mood: Thrilling
- Length: Medium
→ Get books like "Gone Girl", "The Girl with the Dragon Tattoo"

## 🏗️ Project Structure

```
smart-book-recommendation-system/
├── app.py                 # Flask backend with recommendation logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML page
├── static/
│   ├── style.css         # Stylesheet
│   └── script.js         # Frontend JavaScript logic
└── README.md             # This file
```

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic structure
- **CSS3** - Modern styling with gradients, animations, and responsive design
- **JavaScript (Vanilla)** - Dynamic interactions and API calls

### Backend
- **Python Flask** - Lightweight web framework
- **Flask-CORS** - Cross-origin resource sharing

## 📊 Book Library

24 carefully curated books across 8 genres:
- **Fiction** (3 books) - Classic literature
- **Mystery & Thriller** (3 books) - Page-turners
- **Fantasy** (3 books) - Magical adventures
- **Science Fiction** (3 books) - Future visions
- **Romance** (3 books) - Love stories
- **Biography** (3 books) - Real-life inspiration
- **Self-Help** (3 books) - Personal growth
- **History** (3 books) - Learn from the past

## 🔌 API Endpoints

### Get All Books
```
GET /api/books
```
Returns complete book library with metadata.

### Get Recommendations
```
GET /api/recommend?genre={genre}&mood={mood}&length={length}
```
**Parameters:**
- `genre` (optional): fiction, mystery, fantasy, scifi, romance, biography, selfhelp, history
- `mood` (optional): inspiring, thrilling, emotional, lighthearted, thoughtprovoking, adventurous
- `length` (optional): short, medium, long

**Response:** Top 6 books with match scores

### Get Single Book
```
GET /api/book/{book_id}
```
Returns detailed information about a specific book.

## 🎨 Features Showcase

### Visual Elements
- 🎨 Beautiful gradient background
- 📱 Fully responsive design
- ✨ Smooth animations and transitions
- 🏆 Match percentage badges on recommendations
- ⭐ Star ratings for each book
- 📖 Clean card-based layout

### User Experience
- ⚡ Fast and responsive
- 🔍 Real-time search and filtering
- 📊 Clear match scoring system
- 💡 Helpful error messages
- 🎯 Intuitive interface

## 🚀 Future Enhancements

- 👤 **User Accounts** - Save favorite books and reading history
- 📈 **Reading Tracker** - Track books you've read
- 💬 **Reviews & Ratings** - Let users rate and review books
- 🤖 **ML-Based Recommendations** - Use machine learning for better suggestions
- 📚 **Larger Database** - Integrate with external book APIs
- 🔗 **Social Features** - Share recommendations with friends
- 📖 **Reading Lists** - Create custom reading lists

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📚 Add more books to the database

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Jaideep Jaiswal**
- GitHub: [@jaideepj2004](https://github.com/jaideepj2004)
- Repository: [smart-book-recommendation-system](https://github.com/jaideepj2004/smart-book-recommendation-system)

## 🙏 Acknowledgments

- Book data curated from popular and critically acclaimed works
- UI design inspired by modern reading platforms
- Built as a demonstration of full-stack development skills

---

**📚 Happy Reading! Discover your next favorite book today! 📚**