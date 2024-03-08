class Student:
    def __init__(self, student_id, name, user, password):
        self.student_id = student_id
        self.name = name
        self.user = user
        self.password = password
        self.borrowed_books = []

def reserve_book(self, book):
        """
        Permite al estudiante reservar un libro de la librería.
        """
        self.borrowed_books.append(book)