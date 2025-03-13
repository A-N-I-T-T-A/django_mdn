from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register the models
admin.site.register(Genre)
admin.site.register(Language)

# Inline class for BookInstance (to include it in BookAdmin)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # Removes extra empty rows

# Admin class for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')  # Display title, author, and genres
    inlines = [BooksInstanceInline]  # Include inline BookInstance listing

# Admin class for BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id','borrower')  # Added details for BookInstance
    list_filter = ('status', 'due_back')  # Filter by status and due_back
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id','borrower')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

# Inline class for Book (to include in AuthorAdmin)
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0  # Removes extra empty rows

# Admin class for Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')  # Display author details
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]  # Form layout
    inlines = [BooksInline]  # Include inline Book listing

# Register the AuthorAdmin class with the Author model
admin.site.register(Author, AuthorAdmin)
