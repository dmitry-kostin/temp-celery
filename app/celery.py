from celery import Celery
from config import celeryconfig

app = Celery('app')

app.config_from_object(celeryconfig)

if __name__ == '__main__':
    app.worker_main()