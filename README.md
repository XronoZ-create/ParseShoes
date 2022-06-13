# ParseShoes
![enter image description here](https://user-images.githubusercontent.com/70958549/149662741-462df545-74a8-435c-b545-3d139a090ced.png)
Бот для парсинга [Basketshop](www.basketshop.ru). При появлении новой обуви указанного размера, отправляет сообщение в Telegram   


# Стек

 - Python 3.9
 - sqlalchemy
 - BeautifulSoup
 - python-telegram-bot
 - requests

## Quick Start

 1. `git clone https://github.com/XronoZ-create/ParseShoes.git`
 2. Настроить данные в файле config.py


## Структура проекта

    ├── README.md
    ├── config.py
    ├── run.py
    ├── tg_client
        ├── tg.py
    ├── platforms
        ├── basketshop
            ├── basketshop.py
    ├── database
        ├── database_method.py
        ├── db.py
        ├── db_models.py
