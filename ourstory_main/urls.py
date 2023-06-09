from django.conf.urls.static import static
from . import settings
from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/', include('accounts.urls')),
    path('posts/',include('posts.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
