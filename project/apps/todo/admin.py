from django.contrib import admin
from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'complete')

admin.site.register(Todo, TodoAdmin)
