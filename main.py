import os
from time import sleep

from colorama import init

from system import text
from system.db_api.book import DBbook
from system.db_api.genre import DBgenre
from system.utils import dumb

import getpass
from colorama import Fore, Style
from art import tprint

init()
logo = ['print(Fore.LIGHTRED_EX)', 'os.system("cls||clear")', 'tprint("Bookery")']  # логотип Bookery

# проверка на папку system
if not os.path.isdir('system'):
    os.mkdir('system')

# проверка на папку system/db
if not os.path.isdir('system/db'):
    os.mkdir('system/db')

db_book, db_genre = DBbook(), DBgenre()

if __name__ == '__main__':
    from system.utils.book import Book
    from system.utils.genre import Genre
    book, genre = Book(), Genre()

    os.system('cls||clear')

    # создание бд для книг
    db_book.create()
    # создание бд для жанров
    db_genre.create()

    while True:
        options = ["Поиск", "Книги", "Жанры", "Информация", "Выход"]  # главное меню
        index_book = dumb.get_menu_choice(options, [*logo, text.start])  # вывод текста и кнопок меню
        match index_book:
            case 0:
                [eval(_) for _ in logo]  # print logo
                [eval(_) for _ in text.default_search]  # print text
                search = input('\n')
                if search:
                    info = db_book.search(search)  # ищем авторов и названий книг по запросу
                    options = ["Назад"]
                    dumb.get_menu_choice(options,
                                         [*logo,
                                          *text.search.format(len(info['author']),
                                                              '\n'.join([f'print("{author[1]}")' for author
                                                                         in info["author"]]),
                                                              len(info['title']),
                                                              '\n'.join([f'print("{title[1]}")' for title
                                                                         in info["title"]])).split('\n')]
                                         if info['title'] or info['author'] else [*logo, *text.non_search.split('\n')])
            case 1:
                book.view()  # выбор кнопки "Книги"
            case 2:
                genre.view()  # выбор кнопки "Жанры"
            case 3:
                options = ["Назад"]
                # выбор кнопки "Информация"
                dumb.get_menu_choice(options, [*logo, *text.information])
            # exit
            case 4:
                [eval(_) for _ in logo]
                eval(text.exit)
                sleep(3)
                break
    exit()
