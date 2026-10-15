import os
import json
import pika


class NotificationPublisher:
    def publish(self, phone: str, content: str):
        message = {
            "phone": phone,
            "content": content
        }

        credentials = pika.PlainCredentials(
            username=os.getenv("RABBITMQ_USERNAME"),
            password=os.getenv("RABBITMQ_PASSWORD")
        )
        connection_parameters = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST"),
            port=os.getenv("RABBITMQ_PORT"),
            virtual_host=os.getenv("RABBITMQ_VIRTUAL_HOST"),
            credentials=credentials
        )

        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()

        channel.exchange_declare(
            exchange="notification-exchange",
            exchange_type="direct",
            durable=True
        )

        channel.queue_declare(
            queue="notification-queue",
            durable=True
        )

        channel.queue_bind(
            queue="notification-queue",
            exchange="notification-exchange",
            routing_key="notification"
        )

        body = json.dumps(message).encode()

        channel.confirm_delivery()

        channel.basic_publish(
            exchange="notification-exchange",
            routing_key="notification",
            body=body
        )