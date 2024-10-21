Установка и запуск (для запуска необходим python3.9, pip)

1. Клонирование проекта https://github.com/AnnaKrom/testweek.git, либо скачивание zip
2. Создание виртуального окружения python -m venv venv
3. Активаниця аиртуального окружения 
для Windows: venv\Scripts\activate
для Linux/Mac: source venv/bin/activate
4. pip install -r requirements.txt
5. Запуск сервера uvicorn main:app --reload
