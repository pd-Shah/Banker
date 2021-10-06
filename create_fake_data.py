import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Banker.settings')
django.setup()

from branch.models import Branch
from user.models import User
from django.contrib.auth.models import Group
from faker import Faker
from account.models import Account

NUMBER_OF_CUSTOMERS = 10
faker = Faker()


def create_branch():
    tehran = Branch.objects.create(title="Tehran",
                                   branch_manager=User.objects.filter(national_code="tehran manager", ).first())
    tehran.save()

    damavand = Branch.objects.create(title="Damavand",
                                     branch_manager=User.objects.filter(national_code="damavand manager").first())
    damavand.save()

    shiraz = Branch.objects.create(title="Shiraz",
                                   branch_manager=User.objects.filter(national_code="shiraz manager").first())
    shiraz.save()


def create_branch_manager():
    group = Group.objects.filter(name="branch manager").first()

    tehran_manager = User.objects.create(
        national_code="tehran manager",
        phone_number="09226255415",
        password="password"
    )
    tehran_manager.save()
    tehran_manager.groups.add(group)

    damavand_manager = User.objects.create(
        national_code="damavand manager",
        phone_number="091254454221",
        password="password"
    )
    damavand_manager.save()
    damavand_manager.groups.add(group)

    shiraz_manager = User.objects.create(
        national_code="shiraz manager",
        phone_number="09113586455",
        password="password"
    )
    shiraz_manager.save()
    shiraz_manager.groups.add(group)


def create_customer():
    for _ in range(NUMBER_OF_CUSTOMERS):
        obj = User.objects.create(
            national_code=faker.random_int(min=11111, max=99999),
            phone_number=faker.random_int(min=11111, max=99999),
            password=faker.name(),
        )
        obj.save()


def create_manager():
    manager = User.objects.create(
        national_code="dsa",
        phone_number="dsa",
        password="dsa"
    )
    manager.save()
    group = Group.objects.filter(name="manager").first()
    manager.groups.add(group)


def create_group():
    manager = Group.objects.create(name="manager")
    manager.save()

    branch_manager = Group.objects.create(name="branch manager")
    branch_manager.save()


def create_account():
    for user_id in range(NUMBER_OF_CUSTOMERS):
        branch_id = faker.random_int(min=1, max=Branch.objects.count())
        try:
            account = Account.objects.create(user_id=user_id, branch_id=branch_id)
            account.save()
        except:
            pass


if __name__ == "__main__":
    create_customer()
    create_group()
    create_branch_manager()
    create_branch()
    create_manager()
    create_account()
