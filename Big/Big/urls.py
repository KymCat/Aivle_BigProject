# big urls

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.login.urls')),
    
    # 메인 --
    path('main/', views.main, name = 'main'),
    path('main/workLog/',include('apps.workLog.urls'))
]
