import os
import pika
from types import FunctionType


class RabbitMQ:
    def __init__(
        self,
        username=os.environ["RABBITMQ_DEFAULT_USER"],
        password=os.environ["RABBITMQ_DEFAULT_PASS"],
        host=os.environ["RABBITMQ_HOST"],
    ) -> None:
        self.username = username
        self.password = password
        self.host = host

    def connect(self) -> None:
        self.credentials = pika.PlainCredentials(
            username=self.username, password=self.password
        )
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, credentials=self.credentials)
        )

    def send_to_queue(self, queue, message, routing_key, durable=True) -> None:
        channel = self.connection.channel()
        channel.queue_declare(queue=queue, durable=durable)

        channel.basic_publish(
            exchange="",
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    def consumer(
        self,
        queue: str,
        callback: FunctionType,
        durable: bool = True,
        prefecth_count: int = 1,
    ) -> None:
        channel = self.connection.channel()
        channel.queue_declare(queue=queue, durable=durable)
        channel.basic_qos(prefetch_count=prefecth_count)
        channel.basic_consume(queue=queue, on_message_callback=callback)
        channel.start_consuming()

    def disconnect(self) -> None:
        self.connection.close()
