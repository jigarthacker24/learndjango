from django.contrib import admin
from todoapp.models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo','is_complete','date_published']


admin.site.register(Todo, TodoAdmin)