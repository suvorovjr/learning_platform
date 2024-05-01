from users.models import Payment
from users.services import StripeAPIClient


def check_paid(user_id, course_id):
    try:
        payment = Payment.objects.filter(user=user_id, paid_course=course_id).first()
        if payment.payment_status:
            return True
        else:
            payment_status = StripeAPIClient.check_payment_status(payment.stripe_payment_id)
            if payment_status == 'paid':
                payment.payment_status = True
                payment.save()
                return True
            else:
                return False
    except Payment.DoesNotExist:
        return False
