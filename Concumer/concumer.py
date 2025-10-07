import json

from confluent_kafka import Consumer

from config.consumer_config import consumer_config

consumer = Consumer(consumer_config)

consumer.subscribe(['orders'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(msg.error())
            continue

        value = msg.value().decode('utf-8')

        order = json.loads(value)

        print(f'📦 Received order {order['quantity']} x {order["product"]} from {order["user_id"]}')

except:
    consumer.close()
