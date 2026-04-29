from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name','last_name','email','is_active')
    list_filter = ('last_name','is_active','is_superuser')
    list_display_links = ('username',)
