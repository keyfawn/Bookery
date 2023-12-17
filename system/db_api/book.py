import sqlite3


class DBbook:
    def __init__(self):
        """Работа с БД "Книги\""""
        self.path = 'system/db/books.db'  # путь к бд
        self.db = sqlite3.connect(self.path)  # подключение к бд

    def create(self) -> None:
        """Создание таблицы"""
        self.db.execute('CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                        'title TEXT, author TEXT, desc TEXT, genre INTEGER);')
        self.db.commit()

    def add_book(self, title: str, author: str, desc: str, genre: int) -> None:
        """
        Добавление новой книги
        :param title: название
        :param author: автор
        :param desc: описание
        :param genre: жанр
        """
        self.db.execute(f'INSERT INTO Books (title, author, desc, genre) '
                        f'VALUES ("{title}", "{author}", "{desc}", {genre})')
        self.db.commit()

    def all_books(self, genre=0) -> list:
        """
        Возвращает книги
        :param genre: жанр (необязателен)
        :return: список книг
        """
        if genre:
            return self.db.execute(f'SELECT * FROM Books WHERE genre={genre}').fetchall()
        return self.db.execute(f'SELECT * FROM Books').fetchall()

    def search(self, title: str) -> dict:
        """
        Возвращает найденое по запросу
        :param title: запрос
        :return: словарь с ключами: title, author
        """
        info = {}
        data = self.db.execute(f'SELECT id, title FROM Books').fetchall()
        info['title'] = list(filter(lambda x: x, [book if title in book[1] else None for book in data]))
        data = self.db.execute(f'SELECT id, author FROM Books').fetchall()
        info['author'] = list(filter(lambda x: x, [book if title in book[1] else None for book in data]))
        return info

    def return_book(self, key: int) -> dict:
        """
        Вовзращает книгу по id
        :param key: id книги
        :return: словарь о книге
        """
        info = self.db.execute(f'SELECT title, author, genre, desc FROM Books WHERE id={key}').fetchone()
        return {'Название': info[0], "Автор": info[1], "Жанр": info[2], "Описание": info[3]}

    def delete_book(self, id_: int) -> None:
        """
        Удаляет книгу по id
        :param id_: id книги
        """
        self.db.execute(f'DELETE FROM Books WHERE id={id_};')
        self.db.commit()
