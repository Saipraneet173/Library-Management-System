# 📚 Library Management System

> A simple yet powerful library management solution built with Python, designed to streamline book lending operations and enhance library administration.

## 🎯 Project Overview

This Library Management System was developed as part of the **22COA122 Introduction to Programming** coursework at Loughborough University. It provides librarians with an intuitive interface to manage book checkouts, returns, and inventory tracking - all while maintaining a comprehensive transaction history.

### ✨ Key Highlights

- **Smart Search Functionality** - Find books quickly by title or author
- **Automated Checkout System** - Seamless book lending with member validation
- **Visual Analytics** - Beautiful bar charts showing book popularity by genre
- **Robust Error Handling** - User-friendly error messages and input validation
- **Transaction Logging** - Complete audit trail of all library activities

## 🚀 Features

### 📖 Book Management
- **Check Out Books** - Process book loans with member ID verification
- **Return Books** - Simple return process with automatic availability updates
- **Search Catalog** - Find books by title or author with partial matching
- **Visual Reports** - Generate colorful charts showing checkout patterns by genre

### 🗄️ Data Organization
The system uses text-based databases for simplicity and portability:
- `books_info.txt` - Complete book inventory with 20+ titles
- `logfile.txt` - Transaction history tracking all checkouts and returns

## 💻 Getting Started

### Prerequisites
- Python 3.8 or higher
- Matplotlib library for data visualization

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Saipraneet173/Library-Management-System.git
   cd library-management-system
   ```

2. **Install required dependencies**
   ```bash
   pip install matplotlib
   ```

3. **Run the application**
   ```bash
   python menu.py
   ```

## 📋 How to Use

When you launch the program, you'll see a friendly menu with five options:

```
Welcome to library management system.
Kindly choose what you want to do:
1) Book checkout
2) Book search  
3) Book return
4) Book select
5) quit
```

### 🔍 Searching for Books
Choose option 2 and search by:
- **Author name** - Find all books by a specific author
- **Book title** - Search using partial or full title

### 📤 Checking Out Books
1. Select option 1
2. Enter your 4-digit member ID (e.g., 1234)
3. Enter the book ID (1-20)
4. Receive confirmation of successful checkout

### 📥 Returning Books
1. Select option 3
2. Enter the book ID you're returning
3. Enter your member ID for verification
4. Get confirmation of successful return

### 📊 Viewing Statistics
Option 4 generates a colorful bar chart showing:
- Book checkout frequency
- Genre popularity with color coding:
  - 🟢 Classic (Green)
  - 🟡 Fiction (Yellow)
  - 🟠 Horror (Orange)
  - 🔵 Non-Fiction (Cyan)
  - 🔴 Mystery (Red)
  - 🟤 Sci-Fi (Brown)
  - 🟣 Fantasy (Purple)

## 🏗️ Project Structure

```
library-management-system/
│
├── menu.py              # Main program entry point
├── BookCheckout.py      # Handles book checkout logic
├── Return_book.py       # Manages book returns
├── BookSearch.py        # Search functionality
├── book_select.py       # Data visualization module
├── database.py          # Common database operations
├── books_info.txt       # Book inventory database
├── logfile.txt          # Transaction history
└── README.md           # Project documentation
```

## 📝 Important Notes

### Input Validation
- **Member IDs** must be exactly 4 digits (1000-9999)
- **Book IDs** range from 1-20
- Maximum 5 incorrect attempts before the system exits (security feature)

### Current Limitations
- One copy per book title
- No reservation queue system (future enhancement)
- Text-based storage (could migrate to SQL in future versions)

## 🎨 Technical Implementation

The project showcases several programming concepts:
- **Modular Design** - Separate modules for different functionalities
- **File I/O Operations** - Reading and writing to text databases
- **Data Visualization** - Using Matplotlib for graphical reports
- **Error Handling** - Robust validation and user-friendly messages
- **List Comprehensions** - Efficient data processing

## 🤝 Contributing

While this is a coursework project, suggestions for improvements are always welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation
- Share feedback

## 📄 License

This project was created for educational purposes as part of university coursework.

## 🙏 Acknowledgments

- Loughborough University for the project specification
- Course instructors for guidance and support
- Python and Matplotlib communities for excellent documentation

---

**Student ID:** F224272  
**Course:** 22COA122 Introduction to Programming  
**Academic Year:** 2022-2023

---

*Made with ❤️ and lots of ☕ during late-night coding sessions*
