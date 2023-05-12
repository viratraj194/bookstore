from django.contrib import admin

from .models import Category, PostPoem,PostStory,PoemReviewRating

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','user', 'created_at')
    search_fields = ('category_name', 'user__user_name')


class PostPoemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'poem_slug': ('post_title',)}
    list_display = ('post_title', 'category','user', 'updated_at')
    search_fields = ('post_title', 'category__category_name','user__user_name')


class PostStoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'story_slug': ('story_title',)}
    list_display = ('story_title','category','user','updated_at')
    search_fields = ('story_title','category__category_name','user__user_name')
    

admin.site.register(PostStory,PostStoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostPoem,PostPoemAdmin)
admin.site.register(PoemReviewRating)