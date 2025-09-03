# Student ID - F224272
import database
import datetime

def append_record():
    """
    The following function appends a record to the log file, about the book that was checked out.
    """
    global member_id1, book_id2, reservation_date2, date22, return_date3
    data = datetime.datetime.now()
    date = data.strftime('%d/%m/%y')
    Id = database.validateId()
    book_id = database.validate_bookId()
    check = database.availability(book_id) #checking if the book was returned, if it was checked out before.
    if check == True:
        Id = str(Id)
        book_id = str(book_id)
        date = str(date)
        loglist2 = database.read_from_logfile()
        loglist2.append([Id, book_id , "", date, "None"])
        database.append_file(loglist2)
        print("Your book has been checked out successfully")
    else:
        print("sorry this book has been already checked out, kindly try again later or you could check out some other book.")

# Test code
if __name__ == "__main__":
    append_record()






















# def append_file():
#     """
#     The following function overwrites the file with the appended list.
#     """
#     global member_id, book_id, date, return_date, reservation_date
#     a = open("logfile.txt", "w")
#     loglist = append_record()
#     for record in loglist:
#         for i in record:
#             member_id = record[0]
#             book_id = record[1]
#             reservation_date = record[2]
#             date = record[3]
#             return_date = record[4]
#         comma = ","
#         line1 = member_id + comma + book_id + comma + reservation_date + comma + "" + comma + date + comma + "" + return_date
#         a.write(line1+"\n")
#
# append_file()
# append_file()







