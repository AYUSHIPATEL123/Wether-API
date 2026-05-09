from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name','last_name','email','is_active')
    list_filter = ('last_name','is_active','is_superuser')
    list_display_links = ('username',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user')
    list_filter = ('id','user')
    list_display_links = ('id','user')

