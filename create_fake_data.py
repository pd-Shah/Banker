import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Banker.settings')
django.setup()

from branch.models import Branch


def create_branch():
    Branch.objects.create()


if __name__ == "__main__":
    pass
