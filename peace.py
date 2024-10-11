class VirtualLibrarySystem:
    def __init__(self):
        # Stack to keep track of book requests for undoing
        self.request_stack = []
        
        # Queue for book rentals
        self.rental_queue = []
        
        # List of available digital books
        self.available_books = []
    
    # Stack operations: Book request (push) and undo request (pop)
    def request_book(self, book):
        self.request_stack.append(book)
        print(f'Book "{book}" has been requested.')
    
    def undo_request(self):
        if self.request_stack:
            last_request = self.request_stack.pop()
            print(f'Undo request: "{last_request}" has been undone.')
        else:
            print("No requests to undo.")
    
    # Queue operations: Rent a book (enqueue) and process rental (dequeue)
    def rent_book(self, user):
        self.rental_queue.append(user)
        print(f'User "{user}" has been added to the rental queue.')
    
    def process_rental(self):
        if self.rental_queue:
            next_user = self.rental_queue.pop(0)
            print(f'User "{next_user}" is now renting the book.')
        else:
            print("No users in the rental queue.")
    
    # List operations: Display available books, add book, remove book
    def display_available_books(self):
        if self.available_books:
            print("Available books:", ", ".join(self.available_books))
        else:
            print("No books available.")
    
    def add_book(self, book):
        self.available_books.append(book)
        print(f'Book "{book}" has been added to the available list.')
    
    def remove_book(self, book):
        if book in self.available_books:
            self.available_books.remove(book)
            print(f'Book "{book}" has been removed from the available list.')
        else:
            print(f'Book "{book}" is not in the available list.')

# Example usage
library_system = VirtualLibrarySystem()

# Adding books to the available list
library_system.add_book("Breaking clay")
library_system.add_book("Andrej")
library_system.display_available_books()

# Requesting and undoing book requests (stack operations)
library_system.request_book("Breaking clay")
library_system.request_book("Andrej")
library_system.undo_request()  # Undo last request

# Renting books (queue operations)
library_system.rent_book("peace")
library_system.rent_book("shennah")
library_system.process_rental()  # Process first rental
library_system.process_rental()  # Process next rental

# Managing the available books (list operations)
library_system.remove_book("Breaking clay")
library_system.display_available_books()
