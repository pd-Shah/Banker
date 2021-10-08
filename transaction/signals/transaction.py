from django.db.models.signals import post_save
from django.dispatch import receiver

from transaction.models import Transaction
from transaction.tasks import send_sms


@receiver(post_save, sender=Transaction)
def tell_about_the_transaction(sender, instance, created, **kwargs):
    if created:
        print(f'sending the msg with signal..')

        source = instance.source
        destination = instance.destination

        if source is not None:
            send_sms.delay(
                source.user.phone_number,
                # f'the value x{instance.value} as {type} has transitioned.',
            )

        if destination is not None:
            send_sms.delay(
                destination.user.phone_number,
                # f'the value x{instance.value} as {type} has transitioned.',
            )

        return 1
