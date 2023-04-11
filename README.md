## Описание проекта: «API для Yatube»

*Yatube_API* создан для простого и удобного взаимодействия с базой данных проекта  *Yatube* .

## Стек технологий

* Python 3.9,
* Django 3.2,
* DRF,
* JWT + Djoser

## Установка

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Gennadyu-Umikashvili/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate

```

5. Создаем суперпользователя:

```
 python manage.py createsuperuser
```

6. Запустить проект:

```
python manage.py runserver
```

## Примеры запросов

```
Получение всех постов: GET /api/v1/posts/
```

```
Редактирование поста: PUT /api/v1/posts/{id}/
```

```
Добавление комментария: POST /api/v1/posts/{post_id}/comments/
```

```
Получение подписок пользователя: GET /api/v1/follow/
```

```
Получение списка групп: GET /api/v1/groups/
```

## Автор проекта: [Gennady Umikashvili](https://github.com/Gennady-Umikashvili)
