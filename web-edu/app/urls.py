"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from questions import views as questions_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', questions_views.base, name="base"),
    path('ask/', questions_views.ask, name="ask"),
    path('hot/', questions_views.hot, name="hot"),
    path('tags/<str:tag>/', questions_views.tags, name="tags"),
    path('index/<int:question_id>/', questions_views.index, name="index"),

    path('login/', core_views.login, name="login"),
    path('signup/', core_views.signup, name="signup"),
    path('profile/', core_views.profile, name="profile"),
    path('logout/', core_views.logout, name="logout"),
]
