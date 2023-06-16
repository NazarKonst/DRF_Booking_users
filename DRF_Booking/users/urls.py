from django.urls import path, include
from .views import RegisterView, LoginView, ProfileUpdateView, ProfileViewSet


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<str:username>/', ProfileViewSet.as_view({'get': 'list'}), name='profile-list'),
]