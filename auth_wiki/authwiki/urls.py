from django.db import router
from rest_framework.routers import DefaultRouter
from .views import RegisterView



router = DefaultRouter()
# router.register(r'register', RegisterView, basename='register')


urlpatterns = [
    
] 