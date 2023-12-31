![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://lessoleg.t.me/)
# Bookery
**Bookery** - это программа для хранения книг, выполненная по ТЗ.

Приложение представляет собой базу управления книгами в библиотеке. Пользователь может добавить и удалять книгу. 
У книг имеется жанры. Пользователь иметь возможность поиска книги по названию и/или автору. (поиск через один запрос)

### Основная функциональность: ###

#### Добавление новой книги: ####
- Пользователь может добавить новую книгу указав название, автора, описание и жанр книги. Пользователю предложены жанры, 
которые ранее прописаны в базе данных. Так же пользователь может ввести свой жанр.

#### Просмотр списка книг: ####
- Приложение отображает список всех книг (название и автор).
- Пользователь может выбрать книгу из списка для просмотра подробной информации.
- Пользователь может вывести книги с определенным жанром.

#### Поиск книги: ####
- Пользователь может ввести ключевое слово или фразу для поиска.
- Приложение отображает список книг, содержащих данное ключевое слово в полях 'автор' и 'название книги'.

#### Удаление книги: ####
- Пользователь может выбрать книгу из списка и удалить её.
- Книга удаляется из базы данных.

## Используемые библиотеки
В этом проекте я использовал: 
- **click** *(для ожидания нажатия любой кнопки от пользователя)*
- **colorama** *(для красивого цветного отображения текста в консоли)*
- **art** *(точнее tprint для логотипа Bookery)*.
- **dumb** *(это модифицированный dumb-menu для меню)*

## Структура программы
- **main.py** - главный и запускаемый файл
- **requirements.txt** - файл с необходимыми библиотеками
- **system**
  - **db_api**
    - **book.py** - работа с БД "Книги"
    - **genre.py** - работа с БД "Жанры"
  - **utils**
    - **book.py** - работа с книгами в меню
    - **genre.py** - работа с жанрами в меню
    - **dumb.py** - модифицированный dumb-menu для меню
   - **text.py** - файл с текстом для программы

## Как запустить?
1. Для запуска необходимо с помощью файла *requirements.txt* установить все нужные библиотеки:
   
   ```pip install -r requirements.txt```

   После запустить *main.py*, и программа будет запущена
2. Скачать готовый [exe](https://github.com/keyfawn/Bookery/releases/tag/v1.0.0) и запустить

## Контакты
[Мой тг](https://lessoleg.t.me/)

[Моя зеленка](https://zelenka.guru/lessoleg/)
