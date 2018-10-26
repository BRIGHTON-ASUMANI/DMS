from django.conf.urls import url
from . import views, africa
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url('^$',views.home,name='home'),
    url('login/',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('change_password/',views.change_password, name='change_password'),
    url('africa/',africa.sms, name='sms'),
    url( r'^profile/$' , views.profile , name='profile' ),
    url( r'pro/(?P<pk>[0-9]+)/$' , views.dump, name='dump' ),
    url( r'prof/(?P<pk>[0-9]+)/$' , views.ProfileUpdate.as_view( ) , name='profile-update' ) ,
    url( r'profile/(?P<pk>[0-9]+)/delete/$' , views.ProfileDelete.as_view( ) , name='profile-delete' ) ,
    url( r'^create/$' , views.create , name='create' ),
    url('edit/',views.edit, name='edit'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
