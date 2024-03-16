from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentListAPIView
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('view/<int:pk>/', UserRetrieveAPIView.as_view(), name='view'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='delete'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment-list'),
]
