import click

from main import logo, db_genre
from system import text
from system.utils import dumb

from colorama import Fore, Style
from art import tprint
import os


class Genre:
    """Работа с "Жанрами\""""
    def view(self):
        """Основное меню"""
        genres = db_genre.all_genre()
        options = [genre[1] for genre in genres]
        genrees = {}
        for ind, genre in enumerate(genres):
            genrees[ind] = genre[0]
        options.append('добавить новый жанр...')
        options.append('назад')
        index_genre = dumb.get_menu_choice(options, [*logo, text.view_genre])
        self.vote_genre(index_genre, genrees, options)

    def vote_genre(self, index_genre, genrees, options):
        """
        Выбираем выбранный жанр
        :param index_genre: индекс жанра
        :param genrees: словарь жанров
        :param options: меню кнопок
        """
        if index_genre in range(len(options) - 2):
            self.view_genre(index_genre, genrees)
        elif index_genre == len(options) - 2:
            self.add_genre()

    def view_genre(self, index_genre, genrees):
        """
        Просмотр жанра
        :param index_genre: индекс жанра
        :param genrees: словарь жанров
        """
        info = db_genre.return_genre(genrees[index_genre])
        options = ['удалить', 'назад']
        index = dumb.get_menu_choice(options, [*logo, *text.full_genre.format(index_genre, info).split('\n')])
        match index:
            case 0:
                self.delete_genre(index_genre, genrees)
            case 1:
                self.view()

    def add_genre(self):
        """Добавить новый жанр"""

        # если введено название жанра
        if genre := self.__add_genre():
            [eval(_) for _ in logo]
            eval(text.save_genre)
            db_genre.add_genre(genre)
            click.pause('Чтобы продолжить, нажмите Enter')
        self.view()

    def __add_genre(self):
        """возвращает название жанра"""
        [eval(_) for _ in logo]
        [eval(_) for _ in text.new_name_genre]
        return input('\n')

    def delete_genre(self, index_genre, genrees):
        """
        Удаляет жанр
        :param index_genre: индекс жанра
        :param genrees: словарь жанров
        """
        options = ["ДА", 'НЕТ']
        index = dumb.get_menu_choice(options, [*logo, text.pre_delete_genre])
        match index:
            # "ДА"
            case 0:
                db_genre.delete_genre(genrees[index_genre])
                [eval(_) for _ in logo]
                eval(text.delete_genre)
                click.pause('Чтобы продолжить, нажмите Enter')
                self.view()

            # "НЕТ"
            case 1:
                self.view_genre(index_genre, genrees)
