# API для Yatube

**_Учебный проект._**

## Описание:
Yatube - социальная сеть для публикации дневников. Позволяет публиковать посты, комментировать посты, добавлять в группу, осуществлять подписку на авторов.
Для аутентификации используется JWT-токен.

## Стек технологий
Python3, Django 3, Django REST Framework, SQLite3, Simple JWT.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/devlili/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Создание суперпользователя
Выполнить команду и следовать инструкциям:
```
python3 manage.py createsuperuser
```
После создания супепользователя можно использовать данные учетной записи для страницы администрирования - http://127.0.0.1:8000/admin/

## Документация к API

 После запуска dev-сервера документация к API доступна по адресу:
 http://127.0.0.1:8000/redoc/


## Примеры запросов

### Публикация и получение постов

Request: ```[GET] http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=1```

Response:

```json
{
    "count": 3,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 2,
            "author": "string",
            "text": "string",
            "pub_date": "2023-04-18T13:41:19.546891Z",
            "image": null,
            "group": null
        },
        {
            "id": 1,
            "author": "string",
            "text": "string",
            "pub_date": "2023-04-18T13:39:26.793732Z",
            "image": null,
            "group": null
        }
    ]
}
```

Request: ```[POST] http://127.0.0.1:8000/api/v1/posts/```

Request body:

```json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Response:

```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2023-04-18T13:39:26.793732Z",
    "image": "string",
    "group": 0
}
```

### Публикация и получение комментариев к постам

Request: ```[GET] http://127.0.0.1:8000/api/v1/posts/1/comments/```

Response:

```json
[
    {
        "id": 1,
        "author": "string",
        "text": "string",
        "created": "2023-04-18T13:46:48.550123Z",
        "post": 1
    }
]
```

Request: ```[POST] http://127.0.0.1:8000/api/v1/posts/1/comments/```

Request body:

```json
{
    "text": "string"
}
```

Response:

```json
{
    "id": 1,
    "author": "string",
    "text": "string",
    "created": "2023-04-18T13:46:48.550123Z",
    "post": 1
}
```

### Подписка на авторов

Request: ```[GET] http://127.0.0.1:8000/api/v1/follow/```

Response:

```json
[
    {
        "user": "string",
        "following": "string"
    }
]
```

Request: ```[POST] http://127.0.0.1:8000/api/v1/follow/```

Request body:

```json
{
    "following": "string"
}
```

Response:

```json
{
    "user": "string",
    "following": "string"
}
```


## Автор

Лилия Альмухаметова
