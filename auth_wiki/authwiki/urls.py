from django.db import router
from rest_framework.routers import DefaultRouter
from .views import RegisterView
from django.urls import path, include
from . import views



router = DefaultRouter()
# router.register(r'register', RegisterView, basename='register')

urlpatterns = [
        path('', views.home, name='home'),
        path('community', views.community, name='community'),
        path('contact-us', views.contact_us, name='contact-us'),
        path('post', views.post, name='post'),  
        path('landing', views.landing, name='landing'),
        path('authenticated', views.authenticated, name='authenticated'),
        path('unauthenticated', views.unauthenticated, name='unauthenticated'),
        path('error', views.error, name='error'),
        path('errorland', views.error_land, name='errorland'),
        path('individual', views.individual, name='individual'),
        path('search_error', views.search_error, name='search_error'),
        path('login/', views.loginPage, name='login'),
        path('register', views.registerPage, name='register')
] 