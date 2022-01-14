from django.contrib.auth.decorators import login_required
from django.urls import include, path
from testapp import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.About.as_view(), name="about"),
    path('new/', views.BlogCreateView.as_view(), name='post_new'),
]
