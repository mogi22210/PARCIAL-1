class Library:
    def __init__(self):
        self.books = ["Introduction to Python", "Data Structures and Algorithms", "Machine Learning"]

    def check_book_availability(self, book):
        return book in self.books
