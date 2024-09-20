# Приложение для хранилища данных, в котором пользователи смогут загружать данные на сервер

# Стек: python, Django, djangorestframework, MySQL, ORM, HTML

# Серверная часть:
  Реализован API c помощью DjangoREST framework для следующих действий (Маршрут http://127.0.0.1:8000/api/allfileslist/):
- POST загрузка файла на сервер.
- GET скачивание файла с сервера.

![image](https://github.com/user-attachments/assets/b186688c-ee5c-43fd-b4d5-9e203fef79ef)

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

1. Скачивание проекта с GitHub.
-  Копируем URL страницы репозитория, например: https://github.com/KAIIIAPA/cloud_files.git
2. В командной строке выполните следующую команду для клонирования репозитория: git clone https://github.com/username/reponame.git
3. Перейдите в папку, которую вы скачали, используя команду:

Bash

cd reponame

5. Проверьте наличие всех необходимых файлов и директорий внутри скачанного репозитория.

### Запуск сервера

Предположим, что скачанный репозиторий содержит проект Django. Чтобы запустить сервер, выполните следующие шаги:

1. Войдите в виртуальное окружение, если оно используется в проекте (например, source venv/bin/activate).
2. Убедитесь, что установлены все необходимые зависимости, используя pip. Это может быть сделано автоматически при клонировании репозитория или вручную, если в файле requirements.txt есть список зависимостей.
3. Перейдите к корневой директории проекта и запустите команду:

Bash

python manage.py runserver

Сервер будет запущен на локальном хосте по адресу http://127.0.0.1:8000.
