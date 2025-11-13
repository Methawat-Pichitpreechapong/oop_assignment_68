# test_oop.py
# Test suite for the OOP Library System
# Covers basic operations and required edge cases

from library_oop import Book, Member, Library


def test_add_books_and_members():
    lib = Library()

    # Add book
    b1 = Book(1, "Dune", "Frank Herbert", 3)
    assert lib.add_book(b1) == True
    assert lib.add_book(b1) == False  # duplicate IDs

    # Add member
    m1 = Member(1, "Alice", "alice@example.com")
    assert lib.add_member(m1) == True
    assert lib.add_member(m1) == False  # duplicate IDs


def test_borrow_and_return_basic():
    lib = Library()

    b1 = Book(10, "1984", "George Orwell", 2)
    m1 = Member(100, "Bob", "bob@example.com")

    lib.add_book(b1)
    lib.add_member(m1)

    # Borrow success
    result = lib.borrow_book(100, 10)
    assert result == "success"
    assert b1.available_copies == 1

    # Borrow again (same member, same book)
    result = lib.borrow_book(100, 10)
    assert result == "already_borrowed"

    # Return success
    result = lib.return_book(100, 10)
    assert result == "success"
    assert b1.available_copies == 2


def test_borrow_unavailable_book():
    lib = Library()

    b = Book(1, "Sapiens", "Yuval Noah Harari", 1)
    m = Member(1, "Tom", "tom@example.com")
    lib.add_book(b)
    lib.add_member(m)

    # Borrow first time → OK
    assert lib.borrow_book(1, 1) == "success"

    # Book now has 0 copies
    assert b.available_copies == 0

    # Borrow again → no copies
    assert lib.borrow_book(1, 1) == "no_available_copies"


def test_return_not_borrowed_book():
    lib = Library()

    b = Book(5, "The Hobbit", "Tolkien", 2)
    m = Member(7, "Eve", "eve@example.com")
    lib.add_book(b)
    lib.add_member(m)

    # Return without borrowing → should fail
    assert lib.return_book(7, 5) == "not_borrowed"


def test_invalid_member_and_book():
    lib = Library()

    # No books, no members yet
    assert lib.borrow_book(999, 1) == "member_not_found"
    assert lib.return_book(999, 1) == "member_not_found"

    # Add a member but still no book
    m = Member(1, "Max", "max@example.com")
    lib.add_member(m)

    assert lib.borrow_book(1, 999) == "book_not_found"
    assert lib.return_book(1, 999) == "book_not_found"


def test_display_functions():
    lib = Library()

    # Initially empty
    assert lib.display_books() == "No books available."
    assert lib.display_members() == "No members available."

    # Add data
    lib.add_book(Book(1, "Test", "Author", 1))
    lib.add_member(Member(1, "User", "user@example.com"))

    # Now there should be something to display
    assert "Test" in lib.display_books()
    assert "User" in lib.display_members()
