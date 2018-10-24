from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.home,name='home'),
    url('login/',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('change_password/',views.change_password, name='change_password'),
]
