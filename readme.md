# Bookstore Application

Это простое веб-приложение для управления книжным магазином, написанное на Python с использованием Flask. Приложение позволяет добавлять, удалять и получать информацию о книгах.

  ### <div style="color:darkred"> **Дописан только модуль `sqlite_storage.py`  весь остальной код проекта остался неизменным.**</div>


## Структура проекта
    
    bookstore/
    │
    ├── app/
    │   ├── application/
    │   │   └── book_service.py  # Логика работы с книгами
    │   ├── context.py            # Контекст приложения
    │   ├── domain/
    │   │   └── book.py           # Модель книги
    │   ├── infra/
    │   │   ├── storage/
    │   │   │   ├── mem_storage.py     # Хранение книг в памяти
    │   │   │   └── sqlite_storage.py   # Хранение книг в SQLite
    │   └── views/
    │       └── book.py           # Вьюхи для работы с книгами
    │
    ├── requirements.txt           # Зависимости проекта
    └── README.md                  # Документация проекта
    

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш_репозиторий.git
   cd bookstore
   ```

2. Установка виртуального окружения:
    ```bash
    python -m venv .venv 
    ```

3. Запуск виртуального окружения:
      
    На macOS/Linux:

    ``` bash
    source .venv/bin/activate
      ```


    На Windows:
    ``` bash
    .venv/scripts/activate 
    ```
4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
5. Запуск приложения
      ``` bash
      python app/bookstore.py
      ```

Приложение будет доступно по адресу http://127.0.0.1:5000/books  
## Использование

### URL и запросы
1. Получить все книги

    Метод: `GET`

    URL: `/books/`

    ***Пример запроса:***

    ```bash
    curl http://127.0.0.1:5000/books/
    ```
2. Добавить книгу

    Метод: `POST`

    URL: `/books/`

    ***Тело запроса:***
    ``` json
    {
    "title": "Название книги",
    "description": "Описание книги",
    "publish_year": 2021,
    "pages_count": 300,
    "created_at":"" 
    }  
    ```
    ***<div style="color:blue; background-color:white "> поле `created_at` указываем, но оставляем пустым, оно будет заполнено автоматически при добавлении книги. </div>***
    
    ***Пример запроса:***
    ``` bash
    curl -X POST http://127.0.0.1:5000/books/ -H "Content-Type: application/json" -d '{"title": "Название книги", "description": "Описание книги", "publish_year": 2021, "pages_count": 300,"created_at": ""}'
    ```
3. Удалить книгу

    Метод: `DELETE`

    URL: `/books/<id>`

    ***Пример запроса:***
    ``` bash
    curl -X DELETE http://127.0.0.1:5000/books/1
    ```


