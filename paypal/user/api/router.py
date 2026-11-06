from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.api.views import RegisterView, UserMeView, UserUpdateView, UsersPublic, UserByIdPublic

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refreshToken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/me/', UserMeView.as_view()),
    path('user/update/', UserUpdateView.as_view()),
    path('users/get_all/', UsersPublic.as_view()),
    path('users/get_all/<int:user_id>/', UsersPublic.as_view()),
    path('users/get_by/<int:user_id>/', UserByIdPublic.as_view()),
]
