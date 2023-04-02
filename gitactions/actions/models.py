from django.db import models

class UserList(models.Model):
    name = models.CharField('Name', max_length = 500)
    surname = models.CharField('Surname', max_length = 500)
    email = models.EmailField('Email', max_length = 500)
    password = models.CharField('Password', max_length = 500)
    registration_date = models.DateTimeField(auto_now_add=True)

class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

class Register(models.Model):
    name = models.CharField('Name', max_length = 500)
    description = models.CharField('Description', max_length = 500)
    email = models.EmailField('Email', max_length = 500)
    password = models.CharField('Password', max_length = 500)
    registration_date = models.DateTimeField(auto_now_add=True)

class Meta:
        verbose_name = "register"
        verbose_name_plural = "registers"

class WorkerList(models.Model):
    name = models.CharField('Name', max_length = 500)
    surname = models.CharField('Surname', max_length = 500)
    email = models.EmailField('Email', max_length = 500)
    password = models.CharField('Password', max_length = 500)
    registration_date = models.DateTimeField(auto_now_add=True)

class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"