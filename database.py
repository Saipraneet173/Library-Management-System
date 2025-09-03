# Student ID - F224272
def read_from_bookfile():
    """
    The following function reads from the book records and stores in a list
    and returns the list.
    """
    global booklist
    a = open("books_info.txt", "r")
    booklist = []
    for line in a:
        book = line.split(",")
        for j in range(0, len(book)):
            book[j] = book[j].strip()
        booklist.append(book)
    return booklist

def read_from_logfile():
    """
    The following function reads from the logfile and stores in a list
    and returns the list.
    """
    global loglist
    b = open("logfile.txt", "r")
    loglist = []
    for line in b:
        log = line.split(",")
        for i in range(0,len(log)):
            log[i] = log[i].strip()
        loglist.append(log)
    return loglist


def validate_bookId():
    """
    The following function checks whether the entered bookId is valid or not.


    ###
    bookId: '12' would be acceptable.
    bookId: '23' would give an error message.
    ###
    """
    counter = 0
    while counter != 5:
        try:
            bookId = int(input("Enter the Id of the book: "))
        except ValueError:
            bookId = -1
        if 0 <= bookId <= 20:
            return bookId
        else:
            print("Please enter a valid bookId")
            counter += 1
    print("Too many invalid attempts please try again later")

def validateId():
    """
    The following function checks whether the entered member id is valid or not.

    ### example ###
    member id = "2345" would return True
    member id = "lol" would return error message
    """
    counter = 0
    while counter != 5:
        try:
            member_id = int(input("Enter member id: "))
        except ValueError:
            member_id = -1
        if len(str(member_id)) == 4 and 0000 <= member_id <= 9999:
           return member_id
        else:
            print("Please enter a valid member ID")
            counter += 1
    print("Too many invalid attempts, please try again later")

def append_file(loglist):
    """
    The following procedure overwrites the logfile with the list passed into the procedure as a parameter.
    """
    global member_id1, book_id2, reservation_date2, date22, return_date3
    a = open("logfile.txt", "w")
    for record in loglist:
        member_id1 = record[0]
        book_id2 = record[1]
        reservation_date2 = record[2]
        date22 = record[3]
        return_date3 = record[4]
        comma = ","
        line1 = member_id1 + comma + book_id2 + comma + reservation_date2  + comma + date22 + comma + return_date3
        a.write(line1+"\n")


def availability(id):
    """
    The following function checks through the log file, by taking the book id as the parameter, if the book was checked
    out before.
    Returns True if the book was returned after being checked out before.
    Returns False if the book was checked out before and not returned.
    """
    list2 = read_from_logfile()
    available = False
    for book in list2:
        if str(id) == book[1] and book[4] != "None":
            available = True
    return available

# test code
if __name__ == "__main__":
    read_from_bookfile()
    read_from_logfile()
    validateId()
    validate_bookId()



