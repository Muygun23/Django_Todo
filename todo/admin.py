from django.contrib import admin
from .models import Todo, Category, Tag



class CategoryTodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'is_active',
    ]
    list_display_links = [
        'pk',
        'title',
    ]


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'category',
        'title',
        'is_active',
        # 'ceated_at',
        # 'updated_at',
    ]
    list_display_links = [
        'pk',
        'category',
        'title',
    ]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryTodoAdmin)
admin.site.register(Tag)