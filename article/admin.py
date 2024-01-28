from django.contrib import admin
from .models import (
    Article,
    Category,
    Tag,
    Commentary,
    Content,
    Author
)
# Register your models here.


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "slug", 'created_date', 'author']
    readonly_fields = ['slug', ]
    search_fields = ['title', ]
    filter_horizontal = ['tag']
    inlines = [ContentInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']
    search_fields = ['name', ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']