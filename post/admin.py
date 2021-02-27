from django.contrib import admin
from .models import Post, Category, Comments

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
        list_display = ('id', 'title', 'is_published')
        list_display_links = ('id', 'title')


admin.site.register(Post, PostAdmin)

admin.site.register(Comments)

