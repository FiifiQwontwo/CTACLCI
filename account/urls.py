from django.urls import path
from .views import *

urlpatterns = [

    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('mouse/', register_user, name='sign_up'),
    path('edit_mouse/', edit_user, name='edit_accounts'),
    path('mouse_edit/', change_password, name='reset_password'),

]
