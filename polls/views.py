from django.core.checks import register
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, render, redirect

class MainView(View):
    def get(self, request):
        photos = Photo.objects.all
        form = PhotoForm()
        context = {'form': form, 'photos': photos}
        return render(request, 'main.html', {'context': context})


# class Gallery(View):
#     def get(self, request):
#         return render(request, 'gallery.html')

def schedule(request):
    user = User()
    if user.is_active:
        username = request.user.username
    teacher = Teacher.objects.all
    schedule = Schedule.objects.all

    if request.method == 'POST':
        form = EditSchedule(request.POST)
        # teach = Teacher.objects.filter(name_class='Йога').order_by('Surname')

        if form.is_valid():
            sch = Schedule()
            sch.number = request.POST.get('number')
            sch.name_class = request.POST.get('class_name')
            list_teacher = request.POST.get('teacher')
            sch.id_teacher_id = int(list_teacher)
            sch.time_class = 0
            sch.week_day = 0
            sch.save()
            context = {'schedule': schedule, 'teacher': teacher, 'username': username, 'form': form}
            return render(request, 'schedule.html', {'context': context})

    else:
        form = EditSchedule(request.POST)
    context = {'schedule': schedule, 'teacher': teacher, 'username': username, 'form': form}
    return render(request, 'schedule.html', {'context': context})
    # return render(request, 'schedule.html', {'schedule': schedule})


def regist(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)

        if form.is_valid() and request.POST.get('code') == '1234':
            teacher = Teacher()
            teacher.login = request.POST.get('login')
            teacher.password = request.POST.get('password')
            teacher.email = request.POST.get('email')
            teacher.code = request.POST.get('code')
            teacher.Name = request.POST.get('Name')
            teacher.Surname = request.POST.get('Surname')
            teacher.Otchestvo = request.POST.get('Otchestvo')
            teacher.Phone = request.POST.get('Phone')
            teacher.name_class = request.POST.get('name_class')
            teacher.save()
            user1 = form.save()
            user1.refresh_from_db()
            user1.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user1.username, password=my_password)
            login(request, user)
            # user = User()
            # user.username = request.POST.get('username')
            # user.password = request.POST.get('password1')
            # user.save()
        return render(request, 'main.html', {'form': form})
    else:
        form = RegistForm()
    return render(request, 'regist.html', {'form': form})


def enter(request):
    print("1")
    if request.method == 'POST':
        print("2")
        form = EnterForm(request.POST)
        if form.is_valid():
            print("3")
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                print("4")
                if user.is_active:
                    print("5")
                    login(request, user)
                    return render(request, 'main.html', {'form': form})
                else:
                    print("6")
                    return render(request, 'login.html', {'form': form})
            else:
                print("7")
                return render(request, 'login.html', {'form': form})
    else:
        print("8")
        form = EnterForm()
    return render(request, 'login.html', {'form': form})



def ulogout(request):
    logout(request)
    form = EnterForm()
    return render(request, 'main.html', {'form': form})


def PhotoUpload(request):
    user = User()
    if user.is_active:
        username = request.user.username
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        photos = Photo.objects.all
        context = {'form': form, 'username': username, 'photos': photos}
        if form.is_valid():
            form.save()
            return render(request, 'gallery.html', {'context': context})
    elif request.method != 'POST' and request.method != 'GET':
        form = PhotoForm()
        context = {'form': form, 'username': username}

    elif request.method == 'GET':
        # getting all the objects of hotel.
        photos = Photo.objects.all
        form = PhotoForm()
        context = {'form': form, 'username': username, 'photos': photos}
        return render(request, 'gallery.html', {'context': context})

    return render(request, 'gallery.html', {'context': context})

#
# def success(request):
#     return HttpResponse('successfully uploaded')

