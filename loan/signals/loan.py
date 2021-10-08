from django.db.models.signals import post_save
from django.dispatch import receiver

from loan.models import Loan
#
#
# @receiver(post_save, sender=Loan)
# def tell_about_the_transaction(sender, instance, created, **kwargs):
#     pass