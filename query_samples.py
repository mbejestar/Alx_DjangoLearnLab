import os  
import django  

# Set up Django environment  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Introduction_to_Django.settings")  
django.setup()  

from relationship_app.models import Author, Book, Library, Librarian  

# Query all books by a specific author  
def get_books_by_author(author_name):  
    author = Author.objects.get(name=author_name)  
    books = Book.objects.filter(author=author)  
    return books  

# List all books in a library  
def get_books_in_library(library_name):  
    library = Library.objects.get(name=library_name)  
    books = library.books.all()  
    return books  

# Retrieve the librarian for a library  
def get_librarian_for_library(library_name):  
    library = Library.objects.get(name=library_name)  
    librarian = Librarian.objects.get(library=library)  
    return librarian  

# Sample calls to test the queries  
if __name__ == "__main__":  
    print("Books by Author John Doe:")  
    for book in get_books_by_author("John Doe"):  
        print(book.title)  

    print("\nBooks in Library Central Library:")  
    for book in get_books_in_library("Central Library"):  
        print(book.title)  

    print("\nLibrarian for the Central Library:")  
    print(get_librarian_for_library("Central Library").name)