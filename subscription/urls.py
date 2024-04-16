from django.urls import path
from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionAPIView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('', SubscriptionAPIView.as_view(), name='subscription'),
]
