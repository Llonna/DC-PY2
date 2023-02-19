BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Стакан"
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        Пример:
        >>> book = Book(0, "Bible", 1600)
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа string")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name!r}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        :return: идентификатор для добавления новой книги в библиотеку
        """
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        :return: Индекс книги в списке.
        """
        for index, books in enumerate(self.books):
            if books.id_ == id_:
                return index
        raise TypeError("Книги с таким индексом не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [Book(id_=dict_books["id"], name=dict_books["name"], pages=dict_books["pages"]) for dict_books in
                  BOOKS_DATABASE]

    library_with_books = Library(books = list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))