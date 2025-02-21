#RETRIVE OPERATION

book = Book.object.get(title="1984")print (f"Title:{book:title},Author:{book.author},Year:{book.publication_year}")

#Expected output = Title:1984,Author: George Orwell,Year:1984
