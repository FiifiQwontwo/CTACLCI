from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.register_user, name='signup'),
    path('update-profile/', views.edit_user, name='update profile'),
    path('update-password/', views.change_password, name='change password'),

]
