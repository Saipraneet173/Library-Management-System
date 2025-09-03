#Student ID - F224272
import database

def booksearch():
    """
    The following function searches through the record of books, by either the author's name or the book's name and
    provides the user with the details of the book he/she is searching for, if its exists in the library.
    """
    booklist = database.read_from_bookfile()
    found = False
    while True:
        print("By what parameter do you want to search through the record?")
        print("[1] - author\n[2] - Book name")
        option = (input("Enter your option: "))
        if option == "1":
            search_item = input("Enter the author's name:")
            for book in booklist:
                if search_item.lower() in book[3].lower():
                    print(booklist[0])
                    print(book)
                    found = True
            break
        elif option == "2":
            search_item = input("Enter the book's name:")
            for book in booklist:
                if search_item.lower() in book[2].lower():
                    print(booklist[0])
                    print(book)
                    found = True
            break

        else:
            print("Error please choose a valid option")

    if not found:
        print("Sorry the book you are searching for is not found")


#Test code
if __name__ == "__main__":
    booksearch()


