import requests
from django.conf import settings


class StripeAPIClient:

    def __init__(self, amount, product_name, currency='rub'):
        self.api_key = settings.STRIPE_API_KEY
        self.amount = amount
        self.product_name = product_name
        self.currency = currency
        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def create_product(self):
        product_data = {'name': self.product_name}
        product_response = requests.post(
            'https://api.stripe.com/v1/products',
            headers=self.headers,
            data=product_data
        ).json()
        product_id = product_response.get('id')
        return product_id

    def create_price(self):
        price_data = {
            'unit_amount': self.amount * 100,
            'currency': self.currency,
            'product': self.create_product()
        }
        price_response = requests.post(
            'https://api.stripe.com/v1/prices',
            headers=self.headers,
            data=price_data
        ).json()
        price_id = price_response.get('id')
        return price_id

    def create_session(self):
        session_data = {
            'payment_method_types[]': 'card',
            'line_items[0][price]': self.create_price(),
            'line_items[0][quantity]': 1,
            'mode': 'payment',
            'success_url': 'https://example.com/success'
        }
        session_response = requests.post(
            'https://api.stripe.com/v1/checkout/sessions',
            headers=self.headers,
            data=session_data
        ).json()
        payment_url = session_response.get('url')
        return payment_url

    @staticmethod
    def check_payment_status(payment_id):
        url = f'https://api.stripe.com/v1/checkout/sessions/{payment_id}'
        headers = {'Authorization': f'Bearer {settings.STRIPE_API_KEY}'}
        check_response = requests.get(
            url=url,
            headers=headers
        ).json()
        payment_status = check_response.get('payment_status')
        return payment_status == 'paid'
