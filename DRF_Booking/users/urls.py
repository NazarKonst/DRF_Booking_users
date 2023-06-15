from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView

# router = DefaultRouter()
# router.register(r'posts', PostViewSet)
#
# router.register('users', AuthorViewSet, basename='users')
# router.register('book', BookViewSet, basename='book')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('', include(router.urls))
]