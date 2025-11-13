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