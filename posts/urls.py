from django.urls import path
from . import views

urlpatterns = [
   path('add_posts/',views.add_posts,name='add_posts'),
   path('add_posts/add_poem_category',views.add_poem_category,name='add_poem_category'),
   path('add_posts/add_poem_category/edit_category/<int:pk>/',views.edit_category,name='edit_category'),
   path('add_posts/add_poem_category/delete_category/<int:pk>/',views.delete_category,name='delete_category'),

   path('post_poem',views.post_poem,name='post_poem'),
   
]
