from django.contrib import admin
from my_to_do_list_app.models import ToDoList

# It is used for register our model for visualize our table in django admin panel 

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'descripton', 'created_at')

    list_display_links = ('title',)

    readonly_fields = ('created_at',)

    ordering = ('-id',)