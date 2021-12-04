import os

from kafka import KafkaProducer
from json_utils import json_serializer


producer = KafkaProducer(bootstrap_servers=[os.environ.get('KAFKA_ADDRESS')],
                         value_serializer=json_serializer)


def send(message):
    producer.send("neuron-validator-topic", message)
