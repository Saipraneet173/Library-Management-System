# Student ID - F224272
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import database

def book_select():
    """
    The following function generates a bar graph, by taking the data from the log-file.
    """
    # a is a list consisting of 20 0's, each time a book of certain book id is encountered while looping through the logfile
    # the corresponding index is appended in the list.
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # book_sort is used to read from the logfile and sort the list according to the alphabetical order, so that all
    # the books from same genre could be grouped together.
    book_sort = database.read_from_bookfile()
    book_sort.sort(key=lambda x: x[1])
    loglist = database.read_from_logfile()
    for log in loglist:
        for i in range(1, 21):
            if log[1] == str(i):
                a[i - 1] += 1
    booklist = database.read_from_bookfile()
    book_names = []
    for j in booklist[1:21]:
        b = j[2]
        book_names.append(b)
    #Looping through the book_sort list, and for each genre, colour is assigned and appended the empty list 'colours'
    colours = []
    for s in book_sort:
        if s[1].lower() == "classic":
            colours.append("green")
        elif s[1].lower() == "fiction":
            colours.append("yellow")
        elif s[1].lower() == "horror":
            colours.append("orange")
        elif s[1].lower() == "non-fiction":
            colours.append("cyan")
        elif s[1].lower() == "mystery":
            colours.append("red")
        elif s[1].lower() == "sci-fi":
            colours.append("brown")
        elif s[1].lower() == "fantasy":
            colours.append("purple")
    #Using matplot lib to represent the data in a bar graph.
    plt.bar(book_names, a, color=colours)
    plt.xlabel("Book names")
    plt.xticks(rotation = 270)
    plt.ylabel("Number of books purchase")
    lcolours = {'classic':'green', 'fiction':'yellow', 'horror':'orange', 'non-fiction':'cyan', 'mystery':'red', 'sci-fi':'brown', 'fantasy':'purple'}
    labels = list(lcolours.keys())
    handles = [plt.Rectangle((0,0),1,1, color=lcolours[label]) for label in labels]
    plt.legend(handles, labels)
    plt.show()

# test code
if __name__ == "__main__":
    book_select()
