from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentListAPIView
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('view/', UserRetrieveAPIView.as_view(), name='view'),
    path('update/', UserUpdateAPIView.as_view(), name='update'),
    path('delete/', UserDestroyAPIView.as_view(), name='delete'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment-list'),
]
