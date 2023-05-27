from django.urls import path
from . import views

urlpatterns = [
   path('add_posts/',views.add_posts,name='add_posts'),
   path('add_posts/add_poem_category',views.add_poem_category,name='add_poem_category'),
   path('add_posts/add_poem_category/edit_category/<int:pk>/',views.edit_category,name='edit_category'),
   path('add_posts/add_poem_category/delete_category/<int:pk>/',views.delete_category,name='delete_category'),

   path('add_posts/post_poem',views.post_poem,name='post_poem'),
   path('add_posts/post_poem_edit/<int:pk>/',views.post_poem_edit,name='post_poem_edit'),
   path('add_posts/post_poem_delete/<int:pk>/',views.post_poem_delete,name='post_poem_delete'),
   path('poem_details/<slug:poem_slug>/',views.poem_details,name='poem_details'),
   
   path('list_poems/',views.list_poems,name='list_poems'),
   path('list_storys/',views.list_storys,name='list_storys'),
   
   path('add_posts/post_story/',views.post_story,name='post_story'),
   path('add_posts/post_story_edit/<int:pk>/',views.post_story_edit,name='post_story_edit'),
   path('add_posts/post_story_delete/<int:pk>/',views.post_story_delete,name='post_story_delete'),
   path('story_details/<slug:story_slug>/',views.story_details,name='story_details'),

   path("all_category/",views.all_category, name="all_category"),
     path('category/<int:pk>/',views.category_detail, name='category_detail'),
]
