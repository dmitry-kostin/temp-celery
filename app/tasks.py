from .celery import app
import time


@app.task(autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 1})
def add(a, b):
    time.sleep(2)
    return a + b
