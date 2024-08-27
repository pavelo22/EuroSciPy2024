class Book:
    def __call__(self):
        return 'We started reading the book'

book = Book()
assert book() == 'We started reading the book1'
