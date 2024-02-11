from django.contrib import admin
from .models import (
    Category,
    Tag,
    Article,
    Content,
    Author,
    Comment
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


class ContentInlineAdmin(admin.StackedInline):
    model = Content
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ContentInlineAdmin, )
    list_display = ('id', 'author', 'category', 'modified_date', 'created_date')
    readonly_fields = ('slug', 'modified_date', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('title', )
    list_filter = ('category', 'tags')
    autocomplete_fields = ('author', 'category')
    filter_horizontal = ('tags', )
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'top_level_parent_id', 'created_date')
    search_fields = ('name',)
    readonly_fields = ('created_date', )
    autocomplete_fields = ('author', )

