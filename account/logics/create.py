from ..models import Account


def create_account(user_id, branch_id):
    account = Account.objects.create(user_id=user_id, branch_id=branch_id, balance=0)
    account.save()
