from django.contrib import admin  
from .models import Book  

class BookAdmin(admin.ModelAdmin):  
    # Specify the fields to display in the list view  
    list_display = ('title', 'author', 'publication_year')  
    
    # Add search capabilities for the title and author fields  
    search_fields = ('title', 'author')  

    # Add filters for publication year  
    list_filter = ('publication_year',)  

# Register the Book model with the custom admin interface  
admin.site.register(Book, BookAdmin)