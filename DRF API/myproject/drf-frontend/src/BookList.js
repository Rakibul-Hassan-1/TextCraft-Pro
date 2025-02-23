import axios from "axios";
import React, { useEffect, useState } from "react";
import "./App.css";

const BookList = () => {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState(""); // for filtering by title or author
  const [sortOption, setSortOption] = useState("title"); // sorting by title or author
  const [currentPage, setCurrentPage] = useState(1);
  const [booksPerPage] = useState(6); // Customize the number of books per page

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/books/") // Replace with your API endpoint
      .then((response) => {
        setBooks(response.data);
        setLoading(false);
      })
      .catch((err) => {
        setError("Failed to load data. Please check your API.");
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  // Filter books based on search term
  const filteredBooks = books.filter(
    (book) =>
      book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      book.author.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // Sort books based on selected option
  const sortedBooks = filteredBooks.sort((a, b) => {
    if (sortOption === "title") {
      return a.title.localeCompare(b.title);
    } else {
      return a.author.localeCompare(b.author);
    }
  });

  // Pagination Logic
  const indexOfLastBook = currentPage * booksPerPage;
  const indexOfFirstBook = indexOfLastBook - booksPerPage;
  const currentBooks = sortedBooks.slice(indexOfFirstBook, indexOfLastBook);

  // Change page handler
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <div className="book-container">
      <header className="header">
        <h1 className="header-title">Explore Our Book Collection</h1>
        <p className="header-description">
          Discover the best books across various genres and authors.
        </p>
      </header>

      <div className="search-sort-container">
        {/* Search Input */}
        <input
          className="search-input"
          type="text"
          placeholder="Search by title or author..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        {/* Sort Options */}
        <div className="sort-container">
          <label className="sort-label">Sort by: </label>
          <select
            className="sort-select"
            value={sortOption}
            onChange={(e) => setSortOption(e.target.value)}
          >
            <option value="title">Title</option>
            <option value="author">Author</option>
          </select>
        </div>
      </div>

      {/* Book Cards */}
      <div className="book-grid">
        {currentBooks.map((book) => (
          <div className="book-card" key={book.id}>
            <div className="book-card-header">
              <h2>{book.title}</h2>
              <p className="book-author">by {book.author}</p>
            </div>
            <div className="book-card-body">
              <p><strong>Published:</strong> {book.published_date}</p>
              <p><strong>ISBN:</strong> {book.isbn}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Pagination */}
      <div className="pagination">
        {Array.from({ length: Math.ceil(filteredBooks.length / booksPerPage) }, (_, index) => (
          <button
            key={index + 1}
            onClick={() => paginate(index + 1)}
            className={`pagination-button ${currentPage === index + 1 ? 'active' : ''}`}
          >
            {index + 1}
          </button>
        ))}
      </div>
    </div>
  );
};

export default BookList;
