from django.contrib import admin
from .models import Category, Product, Tag, Comments, News
# from django_summernote.admin import SummernoteModelAdmin



# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'model', 'year', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['model', 'year', 'available']
    prepopulated_fields = {'slug': ('name',)}

# class NewsAdmin(SummernoteModelAdmin):
#     """ Новости
#     """
#     list_display = ("title", "user", "created")
#     list_editable = ("user", )
#     search_fields = ["title", "user__username"]
#     list_filter = ("user", "created")
#     summer_note_fields = ('text_min', 'text')


class CommentAdmin(admin.ModelAdmin):
    """ Комментарии
    """
    list_display = ('user', 'product', 'created', 'moderation')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Tag)
