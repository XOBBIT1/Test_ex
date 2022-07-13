from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('shorten', views.shorten_post, name='shorten_post'),
    path('shorten/<str:url>', views.shorten, name='shorten'),
    path('<str:url_hash>', views.redirect_hash, name='redirect'),
]
