from django.urls import path
from . import views

urlpatterns = [
    path("start/", views.start,name='start'),
    path("",views.homepage, name='homepage'),
    path("signup/",views.signup,name='signup'),
    path("signin/",views.signin,name='signin')
]