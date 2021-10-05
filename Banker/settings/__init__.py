from os import getenv

env = getenv("DJANGO_ENV", default="production")

if env == "production" or env == "testing":
    from .prod import *
elif env == "development":
    from .dev import *
