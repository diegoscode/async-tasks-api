from celery import Celery

celery = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/0",  # 👈 Agora usando Redis apenas para backend
)

from app import tasks
