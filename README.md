## Запуск проекта

Есть два способа запустить проект: локально через виртуальное окружение или через Docker.

### Способ 1. Локальный запуск (venv)

1. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   # Для Linux/Mac:
   source venv/bin/activate
   # Для Windows:
   # venv\Scripts\activate
Установите зависимости:

bash
pip install -r requirements.txt
Перейдите в папку с проектом:

bash
cd web-edu
Примените миграции и запустите сервер:

bash
python manage.py migrate
python manage.py runserver
Проект будет доступен по адресу: http://localhost:8000

### Способ 2. Запуск через Docker Compose
Убедитесь, что у вас установлен и запущен Docker.

Находясь в корневой папке проекта (где лежит docker-compose.yml), соберите образ и запустите контейнер:

bash
docker compose up --build
Дождитесь окончания установки зависимостей и запуска сервера.

Проект будет доступен по адресу: http://localhost:8000
