from coreprogramming.elementaryprojects.booktracker.book_functions import (
    add_book,
    display_books,
)


def main():
    books = []
    while True:
        print("\n1. Add a Book")
        print("2. Display All Books")
        print("3. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            add_book(books, title, author, year)

        elif choice == "2":
            display_books(books)

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
