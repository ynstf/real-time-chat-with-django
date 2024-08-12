from django.contrib import admin
import chat.models as models
# Register your models here.

admin.site.register(models.ChatRoom)
admin.site.register(models.Message)