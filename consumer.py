import pulsar
import re
import time
from itertools import cycle

from admin import list_topics

client = pulsar.Client('pulsar://localhost:6650')
batch_policy = pulsar.ConsumerBatchReceivePolicy(max_num_message=100, max_num_bytes=-1, timeout_ms=1)
topics = list_topics(r'^persistent://public/default/my-topic-.*')

consumers = (
    client.subscribe(
        topic,
        subscription_name=f'{topic}-subscription',
        initial_position=pulsar.InitialPosition.Earliest,
        consumer_type=pulsar.ConsumerType.KeyShared,  # Shared subscription mode
        receiver_queue_size=100,
        batch_receive_policy=batch_policy
    ) for topic in topics
)

consumer_iterator = cycle(consumers)

def run_consumers(consumer_iterator):
    try:
        while True:
            consumer = next(consumer_iterator)
            batch = consumer.batch_receive()

            if len(batch) > 0:
                print(f'{batch[0].topic_name()}: {len(batch)} messages')

                for msg in batch:
                    try:
                        consumer.acknowledge(msg)
                    except Exception as e:
                        print(e)
                        consumer.negative_acknowledge(msg)
    finally:
        for consumer in consumer_iterator:
            consumer.close()
        client.close()

run_consumers(consumer_iterator)
