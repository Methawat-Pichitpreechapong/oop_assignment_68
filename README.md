# Library Management System (OOP Version)

This project is a refactored version of an existing procedural-style library
management system. The assignment requires transforming the original procedural
implementation into a fully object-oriented design using Python, complete with
testing and Git version control.

---

## 📌 Project Overview

This project simulates a basic library system where books can be stored,
borrowed, returned, and managed by library members.  
The goal is to convert the original procedural code into a clear, maintainable,
and modular OOP structure following good design practices.

The final OOP solution includes three main classes:

- **Book** – Represents a book in the library  
- **Member** – Represents a library member  
- **Library** – Manages collections of books and members and handles borrowing operations

Additionally, this project includes a full test suite (`test_oop.py`) to ensure
correct functionality and to validate edge cases.

---

## 📁 Project Structure

library-management-oop/
│
├── README.md
│
├── procedural_version/
│ ├── library_procedural.py # Original procedural code
│ └── test_procedural.py # Provided procedural test suite
│
└── oop_solution/
├── library_oop.py # Final OOP implementation (Book, Member, Library)
└── test_oop.py # Test suite for OOP version

---

## 🧱 Design Overview

### ### 1. **Book Class**

**Attributes**
- `id` – Unique book identifier  
- `title` – Book title  
- `author` – Book author  
- `total_copies` – Total number of copies  
- `available_copies` – Copies currently available  

**Key Methods**
- `borrow()` – Decreases available copies  
- `return_copy()` – Increases available copies  
- `display_info()` – String representation of book details  

---

### ### 2. **Member Class**

**Attributes**
- `id` – Unique member ID  
- `name` – Member name  
- `email` – Contact email  
- `borrowed_books` – List of borrowed book IDs  

**Key Methods**
- `borrow_book(book)` – Attempts to borrow a Book  
- `return_book(book)` – Returns a borrowed Book  
- `display_info()` – Summarizes member information  

Borrowing rules:
- A member cannot borrow the same book twice  
- A member cannot return a book they never borrowed  

---

### ### 3. **Library Class**

**Attributes**
- `books` – Dictionary mapping book ID → Book object  
- `members` – Dictionary mapping member ID → Member object  

**Key Methods**
- `add_book(book)` – Adds a new book to the library  
- `add_member(member)` – Registers a new library member  
- `borrow_book(member_id, book_id)` – Borrowing logic controller  
- `return_book(member_id, book_id)` – Return controller  
- `display_books()` – View all books  
- `display_members()` – View all members  

The borrow/return functions return status codes such as:

- `"success"`
- `"book_not_found"`
- `"member_not_found"`
- `"already_borrowed"`
- `"no_available_copies"`
- `"not_borrowed"`

These make testing much easier.

---

## 🧪 Testing

The file `test_oop.py` provides a complete test suite for the system.  
It covers:

### ✔️ **Basic Operations**
- Adding books  
- Adding members  
- Borrowing books  
- Returning books  
- Displaying lists of books and members  

### ✔️ **Edge Cases**
- Borrowing when no copies are available  
- Borrowing the same book twice  
- Returning a book that was never borrowed  
- Non-existent book IDs  
- Non-existent member IDs  
- Duplicate book/member registrations  

---

## ▶️ How to Run the Tests

1. Navigate to the `oop_solution` directory:


2. Run the test file using Python:


If everything works correctly, there should be **no errors**.

---

## 📝 Version Control (Git)

This project follows the required commit structure:

1. **Initial commit** – Original procedural code  
2. **Second commit** – Book class implemented & tested  
3. **Third commit** – Member class implemented & tested  
4. **Fourth commit** – Library class implemented & tested  
5. **Final commit** – Integrated system + full test suite + README.md  

---

## ✅ Conclusion

This project successfully converts the initial procedural design into a fully
object-oriented system while improving structure, readability, and testing
coverage. The final solution demonstrates key OOP principles such as
encapsulation, modularity, and clean separation of responsibilities.
