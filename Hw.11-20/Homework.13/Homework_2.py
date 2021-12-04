class Author:
    def __init__(self, author_name, author_country, birthday, author_books = []):
        self.author_name = author_name
        self.author_country = author_country
        self.birthday = birthday
        self.author_books = author_books

    def __repr__(self):
        return f'{self.author_name}'

    def __str__(self):
        return f'{self.author_name}'


class Book:

    def __init__(self, books_name, year, author: Author):
        self.books_name = books_name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'({self.books_name}, {self.year}, {self.author})'

    def __str__(self):
        return f'({self.books_name}, {self.year}, {self.author})'


class Library:
    sum_books = 0

    def __init__(self, l_name, books = [], authors = []):
        self.l_name = l_name
        self.books = books
        self.authors = authors

    def __repr__(self):
        return f'{self.l_name}, {self.books}, {self.authors}'

    def __str__(self):
        return f'{self.l_name}, {self.books}, {self.authors}'

    def new_book(self, name, year, author: Author):
        if not name:
            print("Empty book name")
            return

        temp_book = Book(name, year, author)
        self.books.append(temp_book)

        if not author in self.authors:
            self.authors.append(author)

        self.sum_books += 1

        return temp_book

    def group_by_author(self, author: Author):
        group = []
        for book in self.books:
            if author == book.author:
                group.append(book)
        return group

    def group_by_year(self, year: int):
        group = []
        for book in self.books:
            if year == book.year:
                group.append(book)
        return group


author_1 = Author('Jotaro', 'Japan', '1989')
author_2 = Author('Jiorno', 'Italy', '2002')
author_3 = Author('Jolin', 'Japan', '2012')
l = Library('Library')
book_1 = l.new_book('Sartdust', 1989, author_1)
book_2 = l.new_book('Golden Wind', 2002, author_2)
book_3 = l.new_book('Stone Ocean', 2012, author_2)
print(l)
print(l.group_by_author(author_2))
print(f'JoJo: {l.sum_books}')
