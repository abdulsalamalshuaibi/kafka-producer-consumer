import uuid
import json
from confluent_kafka import Producer

from config.producer_config import producer_config

producer = Producer(producer_config)

order = {
    "order_id": str(uuid.uuid4()),
    "user_id": "mohammed",
    "product": "Sokany",
    "quantity": 10,
}

order_json = json.dumps(order)
print(order_json)


def delivery_report(err, msg):
    if err:
        print(f"❌ delivery failed: {err}")
    else:
        print(f"🟢 delivery succeed: {msg.value().decode('utf-8')}")
        print(f"🟢 delivery to {msg.topic()} :partition {msg.partition()} : at offset {msg.offset()}")


producer.produce(
    topic="orders",
    value=order_json,
    callback=delivery_report
)

producer.flush()
