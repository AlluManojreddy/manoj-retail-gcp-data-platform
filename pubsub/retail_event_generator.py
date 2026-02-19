import json
import time
import random
from google.cloud import pubsub_v1

project_id = "manoj_gcp_45"
topic_id = "retail-stream-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

while True:
    payload = {
        "order_id": random.randint(1000, 9999),
        "customer_id": random.randint(1, 500),
        "amount": random.randint(100, 2000),
        "owner": "Manoj"
    }

    publisher.publish(topic_path, json.dumps(payload).encode("utf-8"))
    print("Event Sent:", payload)
    time.sleep(2)
