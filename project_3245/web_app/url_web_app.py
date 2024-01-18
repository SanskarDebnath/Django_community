from django.contrib import admin
from django.urls import path
from web_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index_function, name='Landing_Page'),
    path('about', views.about_function, name='About page'),
    path ('community',views.community_function, name='Community Page'),
    path ('latest_project', views.latest_project, name='latest projects'),
    path ('signup', views.signup_view, name='signup'),
    path ('signin', views.signin, name = 'signin')
]