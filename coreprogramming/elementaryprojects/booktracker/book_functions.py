from coreprogramming.elementaryprojects.booktracker.book import Book


def display_books(books):
    if not books:
        print("No books to display.")
        return
    for book in books:
        print(book)


def add_book(books, title, author, year):
    new_book = Book(title, author, year)
    books.append(new_book)
