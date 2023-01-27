from . import views
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('access_token/', include('djoser.urls.jwt')),
    path("login", views.login_view), 
    path("logout", views.logout_view)
]
