import click

from main import logo, db_book, db_genre
from system import text
from system.utils import dumb

from colorama import Fore, Style
from art import tprint
import os


class Book:
    def __init__(self):
        """Работа с "Книгами\""""
        self.sort = 0  # сортировка

    def view(self):
        """Основное меню"""
        books = db_book.all_books(self.sort)
        gen_sor = db_genre.return_genre(self.sort)
        options = [f'Сортировка: {gen_sor if gen_sor != "жанр удален" else "нет"}',
                   *[f"{book[1]} - {book[2]}" for book in books]]
        bookes = {}
        for ind, book in enumerate(books):
            bookes[ind + 1] = book[0]
        options.append('добавить новую книгу...')
        options.append('назад')
        index_book = dumb.get_menu_choice(options, [*logo, text.view_book])
        self.vote_book(index_book, bookes, options)

    def vote_book(self, index_book, bookes, options):
        """
        Выбираем выбранную кнопку
        :param index_book: индекс кнопки
        :param bookes: словарь с книгами
        :param options: меню кнопок
        """
        # сортировка
        if index_book == 0:
            self.s0rt()

        # выбранная книга
        if index_book in range(1, len(options) - 2):
            self.view_book(index_book, bookes)

        # добавить новую книгу
        elif index_book == len(options) - 2:
            self.add_book()

    def s0rt(self):
        """Сортировка по жанру"""
        genres = db_genre.all_genre()
        options = ['нет', *[genre[1] for genre in genres]]
        genrees = {}
        for ind, genre in enumerate(genres):
            genrees[ind + 1] = genre[0]
        index_genr3 = dumb.get_menu_choice(options, [*logo, text.sort_book])

        # если "нет"
        if not index_genr3:
            self.sort = 0

        # выбранный жанр
        else:
            self.sort = genrees[index_genr3]

        self.view()

    def view_book(self, index_book, bookes):
        """
        Просмотр книги
        :param index_book: индекс книги
        :param bookes: словарь книг
        """
        info = db_book.return_book(bookes[index_book])
        info['Жанр'] = db_genre.return_genre(info['Жанр'])
        options = ['удалить', 'назад']
        index = dumb.get_menu_choice(options, [*logo, *text.full_book.format(index_book, info['Название'],
                                                                             info['Автор'], info['Жанр'],
                                                                             info['Описание']).split('\n')])
        match index:
            # удалить книгу
            case 0:
                self.delete_book(index_book, bookes)

            # назад
            case 1:
                self.view()

    def add_book(self):
        """Добавить новую книгу"""

        # если введено название книги
        if title := self.__add_title():

            # если введен автор книги
            if author := self.__add_author():

                # если введено описание книги
                if desc := self.__add_desc():
                    options, genrees, index = self.__add_genre()

                    # если выбран жанр книги
                    if index in range(len(options) - 1):
                        [eval(_) for _ in logo]
                        eval(text.save_book)
                        db_book.add_book(title, author, desc, genrees[index])
                        click.pause('Чтобы продолжить, нажмите Enter')
        self.view()

    def __add_title(self) -> str:
        """возвращает название книги"""
        [eval(_) for _ in logo]
        [eval(_) for _ in text.new_title_book]
        return input('\n')

    def __add_author(self) -> str:
        """возвращает автора книги"""
        [eval(_) for _ in logo]
        [eval(_) for _ in text.new_author_book]
        return input('\n')

    def __add_desc(self) -> str:
        """возвращает описание книги"""
        [eval(_) for _ in logo]
        [eval(_) for _ in text.new_desc_book]
        return input('\n')

    def __add_genre(self):
        """возвращает жанр книги"""
        genres = db_genre.all_genre()
        options = [genre[1] for genre in genres]
        genrees = {}
        for ind, genre in enumerate(genres):
            genrees[ind] = genre[0]
        options.append('отмена')
        return options, genrees, dumb.get_menu_choice(options, [*logo, *text.new_genre_book])

    def delete_book(self, index_book, bookes):
        """
        Удаляет книгу
        :param index_book: индекс книги
        :param bookes: словарь книг
        """
        options = ["ДА", 'НЕТ']
        index = dumb.get_menu_choice(options, [*logo, text.pre_delete_book])
        match index:
            # "ДА"
            case 0:
                db_book.delete_book(bookes[index_book])
                [eval(_) for _ in logo]
                eval(text.delete_book)
                click.pause('Чтобы продолжить, нажмите Enter')
                self.view()

            # "НЕТ"
            case 1:
                self.view_book(index_book, bookes)
