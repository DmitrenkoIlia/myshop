from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order

@shared_task(bind=True)
def order_created(self, order_id):
    try:
        order = Order.objects.get(id=order_id)
        subject = f'Order nr. {order.id}'
        message = f'Dear {order.first_name},\n\nYour order ID is {order.id}.'
        send_mail(subject, message, 'admin@myshop.com', [order.email])
        return True
    except Exception as e:
        self.retry(exc=e, countdown=60)