from django.contrib import admin
from .models import BotUser,FeedBack,Profile
# Register your models here.

@admin.register(Profile)
class UserDetail(admin.ModelAdmin):
    list_display = ('name','phone')

@admin.register(BotUser)
class UserDetail(admin.ModelAdmin):
    list_display = ('name','prompt')

@admin.register(FeedBack)
class UserDetail(admin.ModelAdmin):
    list_display = ('name','gender')