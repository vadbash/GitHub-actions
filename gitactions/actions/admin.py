from django.contrib import admin
from .models import UserList, Register, WorkerList

class UserListAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'password', 'registration_date')

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'email', 'password', 'registration_date')

class WorkerListAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'password', 'registration_date')

admin.site.register(UserList, UserListAdmin)
admin.site.register(Register, RegisterAdmin)
admin.site.register(WorkerList, WorkerListAdmin)