# API для социальной сети

## Описание

API для социальной сети, в которой реализованы следующие возможности:

- Публикация записей
- Комментирование записей
- Подписка на авторов

## Стек технологий

- Python 3.11
- Django 3.2
- Django REST Framework
- JWT Authentication

## Запуск проекта

1. Клонировать репозиторий
2. Создать и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
source venv/Scripts/activate  # для Windows
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Применить миграции:

```bash
python manage.py migrate
```

5. Создать суперпользователя:

```bash
python manage.py createsuperuser
```

6. Запустить сервер:

```bash
python manage.py runserver
```

## API Endpoints

### Аутентификация

- `POST /api/v1/token/` - получение JWT токена
- `POST /api/v1/token/refresh/` - обновление JWT токена

### Посты

- `GET /api/v1/posts/` - список всех постов
- `POST /api/v1/posts/` - создание нового поста
- `GET /api/v1/posts/{id}/` - получение поста по ID
- `PUT /api/v1/posts/{id}/` - обновление поста
- `PATCH /api/v1/posts/{id}/` - частичное обновление поста
- `DELETE /api/v1/posts/{id}/` - удаление поста

### Группы

- `GET /api/v1/groups/` - список всех групп
- `GET /api/v1/groups/{id}/` - получение группы по ID

### Комментарии

- `GET /api/v1/posts/{post_id}/comments/` - список комментариев к посту
- `POST /api/v1/posts/{post_id}/comments/` - создание комментария
- `GET /api/v1/posts/{post_id}/comments/{id}/` - получение комментария
- `PUT /api/v1/posts/{post_id}/comments/{id}/` - обновление комментария
- `PATCH /api/v1/posts/{post_id}/comments/{id}/` - частичное обновление комментария
- `DELETE /api/v1/posts/{post_id}/comments/{id}/` - удаление комментария

## Аутентификация

API использует JWT-аутентификацию. Для доступа к защищенным эндпоинтам необходимо:

1. Получить токен через `/api/v1/token/`
2. Использовать токен в заголовке запроса: `Authorization: Bearer <token>`
