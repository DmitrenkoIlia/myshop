from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order

@shared_task
def order_created_task(order_id):
    """
    Завдання для відправки email-сповіщення при успішному створенні замовлення.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Замовлення № {order.id}'
    message = f'Ви успішно оформили замовлення.\n' \
              f'Номер вашого замовлення: {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent