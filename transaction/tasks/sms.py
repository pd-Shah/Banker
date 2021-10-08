from celery import (
    shared_task,
    )


@shared_task
def send_sms(number, content="Long content"):

    """
        send your sms here
    """

    print(
        f'sms send {number}, {content}'
    )