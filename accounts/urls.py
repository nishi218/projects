from django.urls import path
from . import views
from django.contrib import admin
# from .models import room_id

# from django.contrib.auth.models import User
urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("call/", views.call, name="call"),
    path("checkview", views.checkview, name="checkview"),

    path("<str:room_name>/", views.room, name="room"),

    path("logout/", views.logout, name="logout"),
]
