# стартовый текст
start = 'print(Style.RESET_ALL + "Привет, " + Fore.GREEN + Style.BRIGHT + getpass.getuser() + "!" + Style.RESET_ALL)'
# текст в конце программы
exit = 'print(Style.RESET_ALL + "Пока, " + Fore.GREEN + Style.BRIGHT + getpass.getuser() + "!" + Style.RESET_ALL)'


# текск поиска
default_search = ('print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Поиск:" + Style.RESET_ALL)',
                  'print(Fore.CYAN + "для отмены просто " + Fore.RED + "enter" + Style.RESET_ALL)')
# найденно по поиску
search = ('print(Fore.LIGHTCYAN_EX + "Автор {}: " + Style.RESET_ALL)\n'
          '{}\n'
          'print()\n'
          'print(Fore.LIGHTCYAN_EX + "Название {}: " + Style.RESET_ALL)\n'
          '{}\n'
          'print()')
# ничего не нашлось
non_search = ('print(Fore.LIGHTCYAN_EX + "Ничего не нашлось" + Style.RESET_ALL)\n'
              'print()')


# текст информации
information = ('print(Style.RESET_ALL + Fore.LIGHTRED_EX + "Bookery " + Fore.WHITE + "- это программа, для хранения '
               'книг. Выполнено по тз")',
               'print()',
               'print("Автор:")',
               'print(Fore.LIGHTCYAN_EX + "тг" + Fore.WHITE + " - " + Fore.LIGHTBLUE_EX + "https://lessoleg.t.me/")',
               'print(Fore.LIGHTGREEN_EX + "zelenka" + Fore.WHITE + " - " + Fore.LIGHTBLUE_EX + '
               '"https://zelenka.guru/lessoleg/")',
               'print(Style.RESET_ALL)')


# основной текст при кнопки "Книги"
view_book = 'print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Книги:" + Style.RESET_ALL)'
# сортировка книг по жанру
sort_book = 'print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Сортировка по жанру:" + Style.RESET_ALL)'
# выбранная книга
full_book = ('print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Книга {}:")\n'
             'print()\n'
             'print(Fore.LIGHTGREEN_EX + "Название: " + Fore.WHITE + "{}")\n'
             'print(Fore.LIGHTGREEN_EX + "Автор: " + Fore.WHITE + "{}")\n'
             'print(Fore.LIGHTGREEN_EX + "Жанр: " + Fore.WHITE + "{}")\n'
             'print(Fore.LIGHTGREEN_EX + "Описание: " + Fore.WHITE + "{}")\n'
             'print()')
# сохранение книги
save_book = 'print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Новая книга сохранена" + Style.RESET_ALL)'
# название новой книги
new_title_book = ('print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Напиши название новой книги:" + '
                  'Style.RESET_ALL)', 'print(Fore.CYAN + "для отмены просто " + Fore.RED + "enter" + Style.RESET_ALL)')
# автор новой книги
new_author_book = ('print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Напиши автора новой книги:" + '
                   'Style.RESET_ALL)', 'print(Fore.CYAN + "для отмены просто " + Fore.RED + "enter" + Style.RESET_ALL)')
# описание новой книги
new_desc_book = ('print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Напиши описание новой книги:" + '
                 'Style.RESET_ALL)', 'print(Fore.CYAN + "для отмены просто " + Fore.RED + "enter" + Style.RESET_ALL)')
# жанр новой книги
new_genre_book = ('print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Выбере жанр новой книги:" + Style.RESET_ALL)',
                  'print(Fore.CYAN + "для отмены просто выбери" + Fore.RED + " последний вариант" + Style.RESET_ALL)')
# подтверждение удаления книги
pre_delete_book = 'print(Fore.RED + Style.BRIGHT + "Точно удалить выбранную книгу?" + "!" + Style.RESET_ALL)'
# удаление книги
delete_book = 'print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Выбранная книга удалена" + Style.RESET_ALL)'


# основной текст при кнопки "Жанры"
view_genre = 'print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Жанры:" + Style.RESET_ALL)'
# все жанры
full_genre = ('print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Жанр {}:")\n'
              'print()\n'
              'print(Fore.LIGHTGREEN_EX + "Жанр: " + Fore.WHITE + "{}")\n'
              'print()')
# сохранение жанра
save_genre = 'print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Новый жанр сохранен" + Style.RESET_ALL)'
# название названия нового жанра
new_name_genre = ('print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Напиши название нового жанра:" + '
                  'Style.RESET_ALL)', 'print(Fore.CYAN + "для отмены просто " + Fore.RED + "enter" + Style.RESET_ALL)')
# подтверждение удаления жанра
pre_delete_genre = 'print(Fore.RED + Style.BRIGHT + "Точно удалить выбранный жанр?" + "!" + Style.RESET_ALL)'
# удаление жанра
delete_genre = 'print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Выбранный жанр удален" + Style.RESET_ALL)'
