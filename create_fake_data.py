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
    )
    tehran_manager.set_password("pass")
    tehran_manager.save()
    tehran_manager.groups.add(group)

    damavand_manager = User.objects.create(
        national_code="damavand manager",
        phone_number="091254454221",
    )
    damavand_manager.set_password("pass")
    damavand_manager.save()
    damavand_manager.groups.add(group)

    shiraz_manager = User.objects.create(
        national_code="shiraz manager",
        phone_number="09113586455",
    )
    shiraz_manager.set_password("pass")
    shiraz_manager.save()
    shiraz_manager.groups.add(group)


def create_customer():
    faker = Faker()
    for _ in range(NUMBER_OF_CUSTOMERS):
        obj = User.objects.create(
            national_code=faker.random_int(min=11111, max=99999),
            phone_number=faker.random_int(min=11111, max=99999),
        )

        obj.set_password("pass")
        obj.save()


def create_manager():
    manager = User.objects.create(national_code="dsa", phone_number="dsa")
    manager.set_password("pass")
    manager.save()
    group = Group.objects.filter(name="manager").first()
    manager.groups.add(group)


def create_group():
    manager = Group.objects.create(name="manager")
    manager.save()

    branch_manager = Group.objects.create(name="branch manager")
    branch_manager.save()


def create_account():
    faker = Faker()
    for user_id in range(NUMBER_OF_CUSTOMERS):
        branch_id = faker.random_int(min=1, max=Branch.objects.count())
        try:
            account = Account.objects.create(user_id=user_id, branch_id=branch_id,
                                             balance=faker.random_int(min=0, max=99999))
            account.save()
        except:
            pass


def create_specials():
    banker_user = User.objects.create(
        national_code="banker",
        phone_number="banker",
    )

    banker_user.set_password("banker")
    banker_user.save()

    banker_branch = Branch.objects.create(title="banker",
                                          branch_manager=User.objects.filter(national_code="banker", ).first())
    banker_branch.save()

    Bank = Account.objects.create(user=banker_user, branch=banker_branch, balance=99999999)
    Bank.save()


if __name__ == "__main__":
    create_customer()
    create_group()
    create_branch_manager()
    create_branch()
    create_manager()
    create_account()
    create_specials()
