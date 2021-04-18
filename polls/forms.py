from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404, render
from django.db.models.query import QuerySet

choicess = (
    ('Йога', "Йога"),
    ("Стретчинг", "Стретчинг"),
    ("Акробатика", "Акробатика"),
)


class RegistForm(UserCreationForm):
    code = forms.CharField(label=(u"Код"), )
    username = forms.CharField(label=(u"Логин"))
    password1 = forms.CharField(widget=forms.PasswordInput, label=(u"Пароль"), )
    password2 = forms.CharField(widget=forms.PasswordInput, label=(u"Пароль"), )
    email = forms.EmailField(label=(u"Email"), )
    Name = forms.CharField(label=(u"Имя"))
    Surname = forms.CharField(label=(u"Фамилия"))
    Otchestvo = forms.CharField(label=(u"Отчество"))
    Phone = forms.CharField(label=(u"Телефон"))
    # photo = models. ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    name_class = forms.ChoiceField(choices=choicess, label=(u"Выберите"+" "+"направление"))


class EnterForm(forms.Form):
    username = forms.CharField(label=(u"Имя пользователя"), )
    password = forms.CharField(widget=forms.PasswordInput, label=(u"Пароль"), )



class EditSchedule(forms.Form):
    number = forms.CharField(label=(u"Номер ячейки (от 1 до 36 включительно)"), )
    class_name = forms.ChoiceField(choices=choicess, label=(u"Выберите направление"))
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), label=(u"Выберите преподавателя"))

    def __init__(self, *args, **kwargs):
        super(EditSchedule, self).__init__(*args, **kwargs)


class PhotoForm(forms.ModelForm):
    photo = forms.FileField(label=(u"Выберите фото"))
    class Meta:
        model = Photo
        fields = ['photo']

