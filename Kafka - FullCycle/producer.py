from atexit import register
from kafka import KafkaProducer
import json
from data import get_registered_user
import time

# the finallity of this producer is to send the data to the topic that will be partioned

# instancing the KafkaProducer to generate the data
def json_serializer(data):
    return json.dumps(data).encode("utf-8")


# local host is the broker address
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=json_serializer)


# everytime this registered loop is working, will be getting a new registered user
if __name__ == "__main__":
    while 1==1:
        # everytime this is working (the registered loop) this will be sent to Kafka
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4) # every 4 seconds it will publish a record