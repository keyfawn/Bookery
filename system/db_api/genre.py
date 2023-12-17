import sqlite3


class DBgenre:
    def __init__(self):
        """Работа с БД "Жанры\""""
        self.path = 'system/db/genre.db'  # путь к бд
        self.db = sqlite3.connect(self.path)  # подключение к бд

    def create(self) -> None:
        """Создание таблицы"""
        self.db.execute('CREATE TABLE IF NOT EXISTS Genre (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);')
        self.db.commit()

        # добавление базовых жанров
        # если нет ни одного жанра в бд
        if not self.all_genre():
            [self.add_genre(genre) for genre in ['комедия', 'трагедия', 'драма', 'ужасы']]

    def add_genre(self, name: str) -> None:
        """
        Добавление нового жанра
        :param name: название жанра
        """
        if not self.check_book(name):
            self.db.execute(f'INSERT INTO Genre (name) VALUES ("{name}")')
            self.db.commit()

    def check_book(self, name: str) -> bool:
        """
        Существование жанра
        :param name: название жанра
        :return: True or False
        """
        return True if self.db.execute(f'SELECT id FROM Genre WHERE name = "{name}"').fetchone() else False

    def all_genre(self) -> list:
        """
        Возвращает жанры
        :return: список жанров
        """
        return self.db.execute(f'SELECT * FROM Genre').fetchall()

    def return_id(self, name: str) -> int:
        """
        Возвращает id жанра
        :param name: название жанра
        :return: id жанра
        """
        return self.db.execute(f'SELECT id FROM Genre WHERE name = "{name}"').fetchone()[0]

    def return_genre(self, id_: int) -> str:
        """
        Возвращает название жанра
        :param id_: id жанра
        :return: название жанра
        """
        try:
            return self.db.execute(f'SELECT name FROM Genre WHERE id = {id_}').fetchone()[0]
        except Exception:
            return 'жанр удален'

    def delete_genre(self, id_: int) -> None:
        """
        Удаляет жанр по id
        :param id_: id жанра
        """
        self.db.execute(f'DELETE FROM Genre WHERE id={id_};')
        self.db.commit()
