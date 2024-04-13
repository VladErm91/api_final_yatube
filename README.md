# Проект социальной сети на Django

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) 
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 

RESTful API для проекта социальной веб сети
Веб-сайт, где каждый может поделиться постом, оставить свой комментарий, подписаться на друга или вступить в группу.

С помощью этого API-интерфейса могут работать мобильное приложение либо чат-бот. 
Также с его помощью возможна передача данных другим приложениям.

## Технологии применявшиеся в создании проекта
Python,
Django,
Django REST Framework

## Иструкция по запуску
### 1)Клонировать репозиторий выполнив команды в терминале:
git clone https://github.com/VladErm91/api_final_yatube.git
cd api_final_yatube

### 2)Создание окружения
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt

### 3)Сделать миграции и сформировать бд
python3 manage.py makemigrations
python3 manage.py migrate

### 4)Запустить проект
python3 manage.py runserver


## Над проектом работал
Ермолаев Влад
