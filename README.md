Описание
=
Данный проект приводит статистику вакансий программистов с сайтов работы hh.ru, superjob.ru

Установка
=

```
pip install -r requirements.txt
```

Переменные окружения
=
Для настройки переменных окружения нужно создать файл .env указать там переменную окружения с токеном ```SUPER_JOB_KEY=токен``` .

Ключ API.  Ключ SuperJob можно получить зарегистрировавшись в кабинете  [SuperJob](https://api.superjob.ru/?from_refresh=1).


Инструкция
=

```
python3 main.py
``` 
Запускает программу по поиску вакансий.


Примеры запуска скриптов
=

```
$ python3 main.py
```
Запускает программу по поиску вакансий и отрисовывает их в таблицы.


