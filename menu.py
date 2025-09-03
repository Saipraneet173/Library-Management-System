# Student ID - F224272
import database
import BookCheckout
import book_select
import Return_book
import BookSearch
print("Welcome to library management system.")
print("Kindly choose what you want to do:\n1) Book checkout\n2) Book search\n3) Book return\n4) Book select\n5) quit")
counter = 0
while True:
    option = int(input("Enter your option: "))
    if option == 1:
        BookCheckout.append_record()
    elif option == 2:
        BookSearch.booksearch()
    elif option == 3:
        Return_book.return_book()
    elif option == 4:
        book_select.book_select()
    elif option == 5:
        break
    else:
        counter += 1
        if counter == 5:
            print("Too many wrong attempts please try again later.")
            break
print("Thanks for using the library management system, can't wait to see you again :)")
