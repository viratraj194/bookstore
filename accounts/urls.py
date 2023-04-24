from django.urls import path
from . import views

urlpatterns = [
    path('',views.account),
    path('registerUser',views.registerUser,name='registerUser'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('account/',views.account,name='account'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile_settings/',views.profile_settings,name='profile_settings'),
]
