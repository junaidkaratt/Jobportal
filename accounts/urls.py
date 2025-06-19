from django.urls import path
from .views import RegisterUserView, ProtectedUserView, loginUserView, logoutUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', loginUserView.as_view(), name='login'),
    path('protected/', ProtectedUserView.as_view(), name='protected'),
    path('logout/', logoutUserView.as_view(), name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]