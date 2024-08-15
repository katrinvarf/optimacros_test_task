# Тестовое задание для Junior+ Python Developer
Полное задание находится в файле [Task.md](Task.md)  
Версия Python 3.7  
Проект написан на основе веб-фреймворка [Bottle](https://www.bottlepy.org/docs/dev/index.html)
### Запуск проекта в Ubuntu 18.04.6 LTS
1. Откройте терминал
2. Склонируйте репозиторий к себе в каталог  
`git clone https://github.com/katrinvarf/optimacros_test_task.git`
3. Перейдите в папку проекта с помощью команды `cd`  
`cd optimacros_test_task`
4. Создайте виртуальное окружение  
`python3.7 -m venv venv`
5. Активируйте виртуальное окружение, используя команду  
`source venv/bin/activate`
6. Установите необходимые зависимости из файла `requirements.txt`  
`pip install -r requirements.txt`
7. Выполните команду с указанием вашего токена (API ключа) DaData  
`python3.7 application.py --token "название_токена"`
8. Откройте в браузере страницу http://localhost:8080/test_task/