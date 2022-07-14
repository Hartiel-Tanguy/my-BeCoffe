"""becoffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from compte import views
from ping import views as ping_views
from compte import views as compte_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('compte/', include('compte.urls')),
    path('', views.hello, name='hello'),
    path('todo/', include('todo.urls')),
    path('ping', ping_views.ping),
    path('soir', ping_views.soir),
    path('chef', ping_views.chef, name='chef'),
    path('profile/<int:id>', compte_views.index_profile, name='profile'),
]

