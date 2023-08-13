from django.urls import path
from .views import home, signup, user_login, profile, user_logout, pass_change, set_password

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('passchange/', pass_change, name='passchange'),
    path('setpassword/', set_password, name='setpassword'),
]
