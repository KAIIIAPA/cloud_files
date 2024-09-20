from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Allfiles
from .serializers import AllfilesSerializer


# Create your views here.


def main_page(request):
    info = {}
    # Если метод запроса POST
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/menu/')
        else:
            info['message'] = 'Вы ввели Логин/Пароль неправильно попробуйте войти еще раз'
            return render(request, 'main_page.html', context=info)
    # Иначе метод запроса GET
    else:
        return render(request, 'main_page.html')


def registration(request):
    info = {}
    len_info = len(info)
    info['len_info'] = len_info
    users_list = set()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        email = request.POST.get('email')
        users = User.objects.all()
        for user in users:
            users_list.add(user.username)
        if username in users_list:
            info['message'] = 'Такой пользователь уже существует'
            return render(request, 'registration.html', context=info)
        elif repeat_password != password:
            info['message'] = 'Пароли не совпадают'
            return render(request, 'registration.html', context=info)
        else:
            info['message'] = 'Поздравляю вы зарегистрированы, теперь можете авторизоваться'
            user = User.objects.create_user(username=username, password=password, email=email)
            return render(request, 'main_page.html', context=info)
    else:
        return render(request, 'registration.html')


def menu(request):
    context = {}
    # Проверка авторизации пользователя
    if request.user.is_authenticated:
        context['user'] = request.user
        if request.method == 'POST':
            file = request.FILES.get('file')
            if file is None:
                context['message'] = 'Вставьте файл'
                files = Allfiles.objects.filter(creator=request.user).order_by('-created_at')
                context['files'] = files
                return render(request, 'notes.html', context=context)
            else:
                Allfiles.objects.create(file=file, creator=request.user)
                context['message'] = 'Файл добавлен'
                files = Allfiles.objects.filter(creator=request.user).order_by('-created_at')
                context['files'] = files
                return render(request, 'notes.html', context=context)
        else:
            files = Allfiles.objects.filter(creator=request.user).order_by('-created_at')
            context['files'] = files
            return render(request, 'notes.html', context=context)
    else:
        context['user'] = None
        return render(request, 'notes.html', context=context)


def del_not(request, id):
    id_file = id
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            Allfiles.objects.filter(id=id_file).delete()
            context['message'] = 'Файл удалён'
            return render(request, 'del_not.html', context=context)
        else:
            files = Allfiles.objects.filter(id=id_file)
            context['files'] = files
            return render(request, 'del_not.html', context=context)
    else:
        context['message'] = 'Доступ запрещён, Авторизуйтесь!'
        return render(request, 'notes.html', context=context)


def logout_(request):
    logout(request)
    return render(request, 'logged_out.html')


class AllfilesAPIView(generics.ListCreateAPIView):
    queryset = Allfiles.objects.all()
    serializer_class = AllfilesSerializer
    permission_classes = (IsAdminUser, )

