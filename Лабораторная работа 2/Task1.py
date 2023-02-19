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
        Создание и подготовка к работе объекта "Книга"
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
        return f'Книга {self.name!r}'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    list_books = [Book(id_ = dict_books["id"], name = dict_books["name"], pages = dict_books["pages"]) for dict_books in BOOKS_DATABASE]
    for book in list_books:
        print(book)
        print(list_books)
