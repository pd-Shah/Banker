# from django.contrib.auth.models import Group
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from Banker.settings.groups import CUSTOMER
# from user.models import User
#
#
# @receiver(post_save, sender=User)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#         customer_group = Group.objects.filter(name=CUSTOMER).first()
#         instance.groups.add(customer_group)
