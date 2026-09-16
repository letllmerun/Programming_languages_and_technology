def add_book(self, title):
    self.books.append(title)

def remove_book(self, title):
    if title in self.books:
        self.books.remove(title)
        print("Book removed:", title)
    else:
        print("Book not found:", title)

def find_book(self, title):
    if title in self.books:
        print("Book found:", title)
    else:
        print("Book not found:", title)

def show_books(self):
    print("Books in library:")
    for book in self.books:
        print("-", book)
