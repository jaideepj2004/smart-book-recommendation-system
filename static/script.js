const API_URL = '/api';

let allBooks = [];

// DOM Elements
const genreSelect = document.getElementById('genreSelect');
const moodSelect = document.getElementById('moodSelect');
const lengthSelect = document.getElementById('lengthSelect');
const getRecommendationsBtn = document.getElementById('getRecommendationsBtn');
const searchInput = document.getElementById('searchInput');
const filterGenre = document.getElementById('filterGenre');
const allBooksGrid = document.getElementById('allBooksGrid');
const recommendationsSection = document.getElementById('recommendationsSection');
const recommendationsGrid = document.getElementById('recommendationsGrid');
const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error');

// Event Listeners
getRecommendationsBtn.addEventListener('click', getRecommendations);
searchInput.addEventListener('input', filterBooks);
filterGenre.addEventListener('change', filterBooks);

// Initialize - Load all books
loadBooks();

async function loadBooks() {
    try {
        const response = await fetch(`${API_URL}/books`);
        if (!response.ok) throw new Error('Failed to load books');
        
        const data = await response.json();
        allBooks = data.books;
        displayBooks(allBooks, allBooksGrid, false);
    } catch (error) {
        showError('Failed to load books. Please refresh the page.');
        console.error('Error loading books:', error);
    }
}

async function getRecommendations() {
    const genre = genreSelect.value;
    const mood = moodSelect.value;
    const length = lengthSelect.value;
    
    if (!genre && !mood && !length) {
        showError('Please select at least one preference to get recommendations!');
        setTimeout(() => hideError(), 3000);
        return;
    }
    
    showLoading(true);
    hideError();
    
    try {
        const params = new URLSearchParams();
        if (genre) params.append('genre', genre);
        if (mood) params.append('mood', mood);
        if (length) params.append('length', length);
        
        const response = await fetch(`${API_URL}/recommend?${params}`);
        if (!response.ok) throw new Error('Failed to get recommendations');
        
        const data = await response.json();
        
        if (data.recommendations.length === 0) {
            showError('No books found matching your preferences. Try different options!');
            setTimeout(() => hideError(), 3000);
        } else {
            displayBooks(data.recommendations, recommendationsGrid, true);
            recommendationsSection.style.display = 'block';
            recommendationsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    } catch (error) {
        showError('Failed to get recommendations. Please try again.');
        console.error('Error getting recommendations:', error);
    } finally {
        showLoading(false);
    }
}

function filterBooks() {
    const searchTerm = searchInput.value.toLowerCase();
    const genre = filterGenre.value;
    
    let filtered = allBooks.filter(book => {
        const matchesSearch = !searchTerm || 
            book.title.toLowerCase().includes(searchTerm) ||
            book.author.toLowerCase().includes(searchTerm);
        
        const matchesGenre = genre === 'all' || book.genre === genre;
        
        return matchesSearch && matchesGenre;
    });
    
    displayBooks(filtered, allBooksGrid, false);
}

function displayBooks(books, container, showMatchScore = false) {
    if (books.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: #666; grid-column: 1/-1; padding: 40px;">No books found.</p>';
        return;
    }
    
    container.innerHTML = books.map(book => `
        <div class="book-card">
            ${showMatchScore && book.match_score ? `<div class="recommended-badge">⭐ ${book.match_score}% Match</div>` : ''}
            <div class="book-cover">
                📚
            </div>
            <div class="book-info">
                <h3 class="book-title">${book.title}</h3>
                <p class="book-author">by ${book.author}</p>
                <div class="book-meta">
                    <span class="book-genre">${formatGenre(book.genre)}</span>
                    <span class="book-pages">${book.pages} pages</span>
                </div>
                <div class="book-rating">
                    ${'⭐'.repeat(Math.floor(book.rating))}
                    <span>${book.rating}/5</span>
                </div>
                <p class="book-description">${book.description}</p>
            </div>
            ${showMatchScore && book.match_score ? `<div class="match-score">${book.match_score}% Match for You</div>` : ''}
        </div>
    `).join('');
}

function formatGenre(genre) {
    const genreMap = {
        'fiction': 'Fiction',
        'mystery': 'Mystery & Thriller',
        'fantasy': 'Fantasy',
        'scifi': 'Science Fiction',
        'romance': 'Romance',
        'biography': 'Biography',
        'selfhelp': 'Self-Help',
        'history': 'History'
    };
    return genreMap[genre] || genre;
}

function showLoading(show) {
    loadingDiv.style.display = show ? 'block' : 'none';
}

function showError(message) {
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function hideError() {
    errorDiv.style.display = 'none';
}