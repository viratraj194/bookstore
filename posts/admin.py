from django.contrib import admin

from .models import Category, PostPoem

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','user', 'created_at')
    search_fields = ('category_name', 'user__user_name')


class PostPoemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('post_title',)}
    list_display = ('post_title', 'category','user', 'updated_at')
    search_fields = ('post_title', 'category__category_name','user__user_name')
    


admin.site.register(Category, CategoryAdmin)
admin.site.register(PostPoem,PostPoemAdmin)