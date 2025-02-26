# 🛋️ Website Online Furniture Store

## 📌 Описание
Это веб-приложение для онлайн-магазина мебели, разработанное на Django. Проект предоставляет пользователям возможность просматривать каталог товаров, добавлять их в корзину и оформлять заказы. 🏡🛒

Онлайн-магазин мебели ориентирован на удобство использования, предлагая интуитивно понятный интерфейс и удобную навигацию. В каталоге представлены различные категории товаров, а также фильтры для удобного поиска нужной мебели. 💺🛏️

## ✨ Функционал
- 🔑 Регистрация и авторизация пользователей
- 📖 Просмотр каталога товаров
- 🔍 Фильтрация и поиск товаров
- ➕ Добавление товаров в корзину
- 🛍️ Оформление заказа
- ⚙️ Админ-панель для управления товарами и заказами

## 🛠️ Технологии
- 🐍 Python
- 🎯 Django
- 🗄️ PostgreSQL
- 🌐 HTML, CSS

## 📸 Скриншоты
![image](https://github.com/user-attachments/assets/680dbc14-264d-44f9-a83c-fc66c545ffda)

![image](https://github.com/user-attachments/assets/97ab483f-b067-4aef-90fb-9d7054f5231b)

![image](https://github.com/user-attachments/assets/80688060-65d6-47f9-892b-1d30375f7fc1)

![image](https://github.com/user-attachments/assets/64656285-6907-49b7-9997-9b1c41daf5c3)

![image](https://github.com/user-attachments/assets/6b3983e4-cf8a-4b83-94cf-64c0a8a83d9b)

![image](https://github.com/user-attachments/assets/15a9e3db-6fc6-465a-807e-3c47fa39c991)

![image](https://github.com/user-attachments/assets/bd26af26-3516-41b0-a2a8-bbeb3d1880a6)








## 🚀 Установка и запуск
### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/Gojo-Sator0/Website-online-furniture-store-.git
cd Website-online-furniture-store-
```

### 2️⃣ Установка зависимостей
Рекомендуется использовать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

### 3️⃣ Настройка базы данных
В файле `settings.py` укажите настройки PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Примените миграции:
```bash
python manage.py migrate
```

### 4️⃣ Запуск проекта
```bash
python manage.py runserver
```
Проект будет доступен по адресу: `http://127.0.0.1:8000/` 

## 🎯 Развертывание
Проект можно развернуть на сервере с использованием Gunicorn и Nginx. 📡 Если требуется помощь с деплоем, смотри документацию Django по развертыванию.

