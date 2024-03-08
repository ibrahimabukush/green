from django.urls import path
from . import views
urlpatterns = [
  path('home',views.home,name='home'),
  path('signnup',views.signup_page,name='signnup'),
  path('contact',views.contact,name='contact'),
  path('login/',views.LoginPage,name='login'),
  path('logout/',views.Logout_user,name='logout'),

]