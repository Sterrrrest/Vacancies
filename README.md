Описание
=
Данный проект скачивает фото с сайтов NASA, Space-X.

Установка
=

```
pip install -r requirements.txt
```

Переменные окружения
=
Для настройки переменных окружения нужно создать файл .env указать там переменную окружения с токеном ```NASA_TOKEN=токен```
```SUPER_JOB_KEY=токен``` .

Ключ API.  Ключ SuperJob можно получить зарегистрировавшись в кабинете  [SuperJob](https://api.superjob.ru/?from_refresh=1).


Инструкция
=

```
python3 main.py
``` 
Запускает программу по поиску вакансий.

```
predict_rub_salary_hh
```
Ищет вакансии на сайте HH.ru.

```
predict_rub_salary_sj
``` 
Ищет вакансии на сайте SuperJob.ru.


Примеры запуска скриптов
=

```
$ python3 main.py
```
Запускает программу по поиску вакансий и отрисовывает их в таблицы.


