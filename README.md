## <center>Небольшой учебный django-проект сайта библиотеки</center>
Сайт использует данные из базы `db.sqlite3`, которая содержит информацию о книгах, их авторах и издательствах. Описание моделей ***Book***, ***Author***, ***Publishing_house*** содержится в файле **models.py**.

Навигация по сайту осуществляется при помощи меню в верхней части каждой страницы.
На главной странице сайта (за её отображение отвечает шаблон **index.html**), доступной обычно по адресу `http://localhost:8000/`, отбражается приветствие.

Страница `books/` (**books.html**) содержит полную информацию обо всех книгах библиотеки, включая количество имеющихся в наличии копий (количество которых можно изменять при помощи кнопок &#9650; и &#9660;).

На странице `publishers/` (**publishers.html**) отображается информация об издательствах, чьи книги представлены в библиотеке. При клике на названии издательства можно изменить информацию о нём, при клике на названии книги - изменить информацию о книге. Эта возможность предоставлена пользователям с правами администратора. Пользователи, не обладающие правами администратора, могут только ознакомиться с детальной информацией (без возможности изменения).

В базе данных в ознакомительных целях созданы два пользователя - администратор с правами superuser (`admin` с паролем `1`) и обычный пользователь (`user_1` с паролем `password_1`). Разграничение прав пользователей (в нашем случае - предоставление прав пользователю `user_1`) сделано через административную панель стандартным способом путём добавления пользователя в группу &#171;Общая&#187;. Разрешения для группы предварительно настроены также через панель администратора. Панель администратора доступна по адресу **admin/**.

Для стилизации элементов страниц используется bootstrap, который подключён стандартным способом в теге `<link>` шаблона **index.html**. Остальные шаблоны наследуют шаблон **index.html** при помощи тега `{% extends 'index.html' %}`.

### <center>Установка и запуск</center>
Склонируйте репозиторий на локальный компьютер, введя в консоли команду:
```
git clone https://github.com/A-NB/SF-D4_10_HW_django-library.git
```
Затем необходимо перейти в папку проекта и создать для него виртуальное окружение:
```
cd SF-D4_10_HW_django-library
python -m venv env
```
Дождитесь завершения операции, после чего активируйте виртуальное окружение:
```
.\env\Scripts\activate
```
Зависимости, необходимые для проекта, установите, используя файл `requirements.txt`:
```
pip install -r requirements.txt
```
После установки зависимостей запустите сервер командой:
```
python manage.py runserver
```
При успехе Вы увидите в консоли сообщение:
```
Starting development server at http://127.0.0.1:8000/
```
Если порт :8000 занят другим приложением, номер порта может отличаться. Перейдите в своём браузере по адресу, указанному в консоли, чтобы попасть на главную страницу сайта.

*Поскольку проект **учебный**, в настройках приложения в файле **settings.py** содержится в открытом виде SECRET_KEY, а параметр DEBUG = True.*