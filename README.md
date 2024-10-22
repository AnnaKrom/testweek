Установка и запуск (для запуска необходим python3.9, pip)

1. Клонирование проекта https://github.com/AnnaKrom/testweek.git, либо скачивание zip
2. Создание виртуального окружения python -m venv venv
3. Активаниця аиртуального окружения 
для Windows: venv\Scripts\activate
для Linux/Mac: source venv/bin/activate
4. pip install -r requirements.txt
5. Запуск сервера uvicorn main:app --reload


Задача: Создать простой веб-сервис, который предоставляет RESTful API для управления 
товарами и категориями товаров

Используемые сущности:
Категория товара (ProductCategory):
Id (int) — уникальный идентификатор категории;
Name (string) — название категории;
Description (string) — описание категории (необязательно).
Товар (Product):
Id (int) — уникальный идентификатор товара;
Name (string) — название товара;
Description (string) — описание товара;
Price (decimal) — цена товара;
CategoryId (int) — идентификатор категории, к которой относится товар

Требования к функционалу API:
Реализовать для каждой сущности эндпоинты для типовых CRUD-операций и получения 
списка всех значений.
Общие требования:
* В качестве базы данных можно использовать InMemory, SQLite или любую другую на ваш 
выбор.
* Следовать принципам RESTful API.
* Обрабатывать возможные ошибки и возвращать соответствующие коды ответов HTTP.
* Код должен быть чистым и читаемым, с использованием принципов SOLID 
