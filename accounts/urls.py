from django.urls import path
from . import views

urlpatterns = [
    path('',views.account),
    path('registerUser',views.registerUser,name='registerUser'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('account/',views.account,name='account'),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password',views.reset_password,name='reset_password'),

    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile_settings/',views.profile_settings,name='profile_settings'),
]
