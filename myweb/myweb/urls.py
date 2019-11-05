"""mobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mobilesite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('index_m.html', views.index_m,name='index_m'),
    path('index_m/', views.index_m,name='index_m'),
    path('today/', views.today_m,name='today'),
    path('area.html', views.area,name='area'),
    path('person.html', views.person,name='person'),
    path('post/<int:numms>', views.post_data,name='post_data'),
    path('post2/<int:numms>', views.post_data_2,name='Data_2Info'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_URL)
