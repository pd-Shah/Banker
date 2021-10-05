from celery.schedules import crontab
from Banker.settings import BROKER_URL

CELERY_BROKER_URL = BROKER_URL
CELERY_RESULT_BACKEND = BROKER_URL
CELERY_CACHE_BACKEND = "default"

CELERY_QUEUES = (
    Queue("celery", Exchange("celery"), routing_key="default"),
    Queue("imn", Exchange("imn"), routing_key="default"),
)
# If time zones are active (USE_TZ = True) define your local
CELERY_TIMEZONE = "UTC"
# Let's make things happen
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
