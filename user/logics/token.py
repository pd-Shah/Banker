from rest_framework.authtoken.models import Token

from Banker.settings.permissions import TOKEN_CAN_CREATE_ALLOWED


def create_token(user, ):
    token, created = Token.objects.get_or_create(user=user)

    group_set = {g.name for g in user.groups.all()}
    if len(group_set.intersection(TOKEN_CAN_CREATE_ALLOWED)):
        return token

    if hasattr(user, "account"):
        if user.account.is_active:
            return token

    return False
