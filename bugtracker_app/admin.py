from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bugtracker_app.models import CustomUser, Ticket

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display =['position'] 

admin.site.register(Ticket)
admin.site.register(CustomUser, UserAdmin)