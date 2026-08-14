import json

FILE_NAME = "library.json"


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed = False

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "borrowed": self.borrowed
        }


class Library:

    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

                for book in data:
                    new_book = Book(
                        book["book_id"],
                        book["title"],
                        book["author"]
                    )

                    new_book.borrowed = book["borrowed"]
                    self.books.append(new_book)

        except FileNotFoundError:
            self.books = []

    def save_books(self):
        data = []

        for book in self.books:
            data.append(book.to_dict())

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def add_book(self):
        book_id = input("Enter book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists.")
                return

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(book_id, title, author)

        self.books.append(book)
        self.save_books()

        print("Book added successfully!")

    def search_book(self):
        keyword = input("Enter book title: ")

        found = False

        for book in self.books:
            if keyword.lower() in book.title.lower():
                print("\nBook Found")
                print("ID     :", book.book_id)
                print("Title  :", book.title)
                print("Author :", book.author)
                print("Status :", "Borrowed" if book.borrowed else "Available")

                found = True

        if not found:
            print("Book not found.")

    def borrow_book(self):
        book_id = input("Enter book ID to borrow: ")

        for book in self.books:

            if book.book_id == book_id:

                if book.borrowed:
                    print("Book is already borrowed.")
                    return

                book.borrowed = True
                self.save_books()

                print("Book borrowed successfully!")
                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter book ID to return: ")

        for book in self.books:

            if book.book_id == book_id:

                if not book.borrowed:
                    print("This book is already available.")
                    return

                book.borrowed = False
                self.save_books()

                print("Book returned successfully!")
                return

        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n===== LIBRARY BOOKS =====")

        for book in self.books:
            print("\nID     :", book.book_id)
            print("Title  :", book.title)
            print("Author :", book.author)
            print("Status :", "Borrowed" if book.borrowed else "Available")


library = Library()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.search_book()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice.")