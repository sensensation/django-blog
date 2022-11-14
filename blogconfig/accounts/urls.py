from django.urls import path
from .views import Auth 

urlpatterns = [
    path('signup/', Auth.register_user, name='signup'),
    path('login/', Auth.login_user, name='login_page'),
    path('logout/', Auth.logout_user, name='logout'),
]