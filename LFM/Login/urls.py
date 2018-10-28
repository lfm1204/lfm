"""LFM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Login import views
from django.conf.urls import url

app_name = '[Login]'
urlpatterns = [
    url(r'^$',views.loginPage),
    url(r'^login/',views.login,name="toLogin"),
    url(r'^retrievePassword/',views.retrievePassword,name="retrievePassword"),
    url(r'^register/',views.register,name="register"),
    url(r'^changePassword/',views.changePassword,name="changePassword"),
]

