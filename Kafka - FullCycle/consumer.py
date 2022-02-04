from ensurepip import bootstrap
from kafka import KafkaConsumer
import json


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        group_id="consumer-group-a"
    )
    print("STARTING THE CONSUMER")

    for msg in consumer:
        # deserializing the data with json loads
        print("REGISTERED USER = {}".format(json.loads(msg.value)))

