# Student ID - F224272
import database
import datetime


def return_book():
    """
    The following functions checks if the book id is valid and allows to return a specific book.
    """
    global match
    data = datetime.datetime.now()
    date = data.strftime('%d/%m/%y')
    book_id = database.validate_bookId()
    member_id = database.validateId()
    loglist1 = database.read_from_logfile()
    match = True
    for record in loglist1:
        if str(book_id) == record[1] and record[4] == "None" and str(member_id) == record[0]:
            record[4] = str(date)
            database.append_file(loglist1)
            match = True
            print("Thanks for returning the book, it has been returned successfully.")
            break
        else:
            match = False
    if match == False:
        print("Sorry either the book already exists or you have entered wrong member id, kindly check your member and book id again.")


# Test code
if __name__ == "__main__":
    return_book()
