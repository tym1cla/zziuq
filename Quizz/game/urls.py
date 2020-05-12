from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url('', views.indexView, name="home"),
    url('dashboard/', views.dashboardView, name="dashboard"),
    url('login/', LoginView.as_view(), name="login_url"),
    url('register/', views.registerView, name="register_url"),
    url('logout/', LogoutView.as_view(next_page='dashboard'),name="logout_url"),
]
