from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from pizzaria.providers.rabbitmq import RabbitMQ
from json import loads
from pizzaria.models import Order


def callback(ch, method, properties, body) -> None:
    try:
        print(body.decode())
        data = loads(body.decode())
        order = Order.objects.get(id=data["order"]["id"])
        order.status = 2
        order.save()
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"[CallbackError]: {e}")


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        rabbitmq = RabbitMQ()
        try:
            rabbitmq.connect()
            rabbitmq.consumer(queue="order", callback=callback)
        except Exception as e:
            rabbitmq.disconnect()
            raise CommandError(e)
