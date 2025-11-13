class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    # Borrow 1 copy of this book
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    # Return 1 copy of this book
    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    # Display book info (useful for menu/CLI)
    def display_info(self):
        return f"[{self.id}] {self.title} by {self.author} | Total: {self.total_copies}, Available: {self.available_copies}"

    # Reset book copies (useful for testing)
    def reset(self):
        self.available_copies = self.total_copies


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []   # store book IDs or book objects

    # Borrow book (book object expected)
    def borrow_book(self, book):
        # Prevent borrowing same book twice
        if book.id in self.borrowed_books:
            return False

        if book.borrow():  # call Book.borrow()
            self.borrowed_books.append(book.id)
            return True

        return False  # cannot borrow (no copies)

    # Return book
    def return_book(self, book):
        if book.id not in self.borrowed_books:
            return False  # cannot return what wasn't borrowed

        if book.return_copy():  # call Book.return_copy()
            self.borrowed_books.remove(book.id)
            return True

        return False

    # Show member info
    def display_info(self):
        borrowed = ", ".join([str(b) for b in self.borrowed_books])
        if borrowed == "":
            borrowed = "None"
        return f"Member[{self.id}] {self.name} ({self.email}) | Borrowed: {borrowed}"


class Library:
    def __init__(self):
        self.books = {}      # book_id → Book object
        self.members = {}    # member_id → Member object

    # -------------------------------
    # Add book
    # -------------------------------
    def add_book(self, book):
        if book.id in self.books:
            return False
        self.books[book.id] = book
        return True

    # -------------------------------
    # Add member
    # -------------------------------
    def add_member(self, member):
        if member.id in self.members:
            return False
        self.members[member.id] = member
        return True

    # -------------------------------
    # Borrow flow
    # -------------------------------
    def borrow_book(self, member_id, book_id):
        # Validate member
        if member_id not in self.members:
            return "member_not_found"

        # Validate book
        if book_id not in self.books:
            return "book_not_found"

        member = self.members[member_id]
        book = self.books[book_id]

        # Try borrowing
        success = member.borrow_book(book)
        if not success:
            if book.available_copies == 0:
                return "no_available_copies"
            else:
                return "already_borrowed"

        return "success"

    # -------------------------------
    # Return flow
    # -------------------------------
    def return_book(self, member_id, book_id):
        # Validate member
        if member_id not in self.members:
            return "member_not_found"

        # Validate book
        if book_id not in self.books:
            return "book_not_found"

        member = self.members[member_id]
        book = self.books[book_id]

        success = member.return_book(book)
        if not success:
            return "not_borrowed"

        return "success"

    # -------------------------------
    # Display all books
    # -------------------------------
    def display_books(self):
        if not self.books:
            return "No books available."
        return "\n".join(book.display_info() for book in self.books.values())

    # -------------------------------
    # Display all members
    # -------------------------------
    def display_members(self):
        if not self.members:
            return "No members available."
        return "\n".join(member.display_info() for member in self.members.values())