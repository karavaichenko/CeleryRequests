from celery import Celery

CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'

app = Celery(
    'tasks', 
    broker=CELERY_BROKER_URL, 
    backend='rpc://',
    include=['tasks'])
