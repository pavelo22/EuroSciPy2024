class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __getattribute__(self, item):
        print(f"__getattribute__ called for {item}")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print(f"__getattr__ called for {item}")
        if item == 'contents':
            return 'Content of the book not supported yet'
        return object.__getattribute__(self, item)

    def __setattr__(self, name, value):
        if name == 'contents':
            super().__setattr__('contents', value)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        raise AttributeError("No attribute should be deleted")


book = Book('The Book', 'The Author', 'The Year')
print(book.title)
print(book.contents)
book.contents = 'The Book contents'
print(book.contents)

try:
    del book.contents
except AttributeError:
    print('Works as intended')
