from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import *

@admin.register(User)
class UserAdmin(ModelAdmin):
    pass