from django.urls import path
from . import views

app_name = "core"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("mainpage", views.login_request, name="mainpage"),
]
