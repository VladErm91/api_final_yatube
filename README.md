# Проект Web-приложения социальной сети на Django

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) 
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 

RESTful API для проекта социальной веб сети
Веб-сайт, где каждый может поделиться постом, оставить свой комментарий, подписаться на друга или вступить в группу.

С помощью этого API-интерфейса могут работать мобильное приложение либо чат-бот. 
Также с его помощью возможна передача данных другим приложениям.

### Возможности сервиса:
- Регистрация и аутентификация пользователей.
- Пользователи могут быть администраторами, модераторами или обычными пользователями.
- Создание пользовательских групп.
- Подписка на пользователя или группу
- Обмен коментариями

### Технологии проекта:
- Python 3.9 либо выше
- Django
- Django REST Framework

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VladErm91/api_final_yatube.git
cd api_final_yatube
```
Создание окружения
```
python3 -m venv env
source env/bin/activate

python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Сделать миграции и сформировать бд
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Запуск проекта
```
python3 manage.py runserver
```

### Необходимые переменные среды (.env)
```
SECRET_KEY = ''
DEBUG = False
```

Автор: [VladErm91](https://github.com/VladErm91)
