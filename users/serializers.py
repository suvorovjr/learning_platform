from rest_framework import serializers
from users.models import Payment, User
from users.services import StripeAPIClient


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class PaymentSerializer(serializers.ModelSerializer):
    payment_url = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    @staticmethod
    def get_payment_url(obj):
        amount = obj.paid_course.amount
        product_name = obj.paid_course.title
        api_client = StripeAPIClient(amount=amount, product_name=product_name)
        payment_url = api_client.create_session()
        stripe_payment_id = api_client.get_stripe_payment_id()
        obj.stripe_payment_id = stripe_payment_id
        obj.save()
        return payment_url
