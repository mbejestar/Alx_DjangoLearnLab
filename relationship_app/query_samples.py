import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Ensure this path is correct
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample Queries

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return f"Author '{author_name}' does not exist."

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."
    except Librarian.DoesNotExist:
        return f"No librarian assigned to '{library_name}'."

# Example Usage
if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':", query_books_by_author('J.K. Rowling'))
    print("Books in Library 'Central Library':", list_books_in_library('Central Library'))
    print("Librarian for Library 'Central Library':", retrieve_librarian_for_library('Central Library'))