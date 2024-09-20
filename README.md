# Хранилище данных, в котором пользователи смогут загружать данные на сервер

# Стек: python, Django, djangorestframework, MySQL, ORM, HTML

# Серверная часть:
  Реализован API c помощью DjangoREST framework для следующих действий (Маршрут http://127.0.0.1:8000/api/allfileslist/):
- POST загрузка файла на сервер.
- GET скачивание файла с сервера.

![image](https://github.com/user-attachments/assets/24449db7-bb56-4d5f-af84-3d7641fef731)

  Дополнительно:
- Также установлено ограничение (permissions) к данным API по роли пользователя (доступ только у роли admin)

  Обычный пользователь:
![image](https://github.com/user-attachments/assets/43e6bb01-ebcb-4829-b9b1-6948f87faf88)
  Админ:
![image](https://github.com/user-attachments/assets/8f33f2df-7602-4416-8c61-61e3faaffc81)
  
- Реализована авторизация и аутентификация пользователя в DjangoREST framework
![image](https://github.com/user-attachments/assets/f2fbfdb2-d1dc-4f01-8357-52a584acaa19)

  ![image](https://github.com/user-attachments/assets/22fe675b-03ae-45e1-ad21-cf720fa22bb1)

# Клиентская часть (Маршрут http://127.0.0.1:8000/), реализован следующий функционал:
- Авторизация пользователя:

![image](https://github.com/user-attachments/assets/9f1d682b-3f4f-4a3c-970a-5e4c72a76fbb)
 
- Регистрация пользователя:

![image](https://github.com/user-attachments/assets/a6b0aaeb-c6f7-4949-b9f6-1e87dc11d74c)
  
- При авторизациии вам получите отображение загруженных файлов с возможностью скачивать, удалять имеющие файлы добавлять новые файлы:

![image](https://github.com/user-attachments/assets/48101541-5ce4-4c12-9620-af02a2e5c90f)

-  Дополнительно у администратора приложения расширенный функционал с возможностью перехода в панель Администратора и панель APIFiles:

![image](https://github.com/user-attachments/assets/e05ee5b8-2bae-471e-ab19-cd8458dcbfa4)

# Инструкция по установке проекта:

Инструкция ориентирована на операционную систему windows и утилиту git bash.
Для прочих инструментов используйте аналоги команд для вашего окружения.

Клонируйте репозиторий и перейдите в него в командной строке: git clone https://github.com/KAIIIAPA/cloud_files.git

Установите и активируйте виртуальное окружение: 
  - python -m venv venv
  - source venv/Scripts/activate

Установите зависимости из файла requirements.txt:
  - pip install -r requirements.txt
    
В папке с файлом manage.py выполните миграции:
  - python manage.py migrate

Создайте суперюзера, зайдите в админку:
  - python manage.py createsuperuser
    
В папке с файлом manage.py запустите сервер, выполнив команду:
  - python manage.py runserver

Сервер будет запущен на локальном хосте по адресу http://127.0.0.1:8000.
