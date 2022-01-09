from django.contrib.auth.decorators import login_required
from django.urls import include, path
from testapp import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
]
