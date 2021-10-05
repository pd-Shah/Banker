from os import getenv

env_broker = getenv(
    "REDIS_URL",
    default="redis://redis:6379/0",
)

# SMS Confs URL
SMS_URL = "http://"

# Message broker url(Note that the type of the broker is not important)
BROKER_URL = env_broker
