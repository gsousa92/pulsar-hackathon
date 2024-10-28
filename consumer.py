import pulsar
import re

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    re.compile('persistent://public/default/my-topic-.*'),
    subscription_name='my-sub',
    consumer_type=pulsar.ConsumerType.Shared,  # Shared subscription mode
    receiver_queue_size=10
)

def run_consumer(consumer):
    last_topic_message_count = 0
    last_topic = None

    try:
        while True:
            msg = consumer.receive()
            try:
                topic = msg.topic_name()

                if last_topic is None or last_topic == topic:
                    last_topic = topic
                    last_topic_message_count += 1
                else:
                    print_batch(last_topic, last_topic_message_count)
                    last_topic_message_count = 1

                last_topic = topic
                consumer.acknowledge(msg)
            except Exception as e:
                print(e)
                consumer.negative_acknowledge(msg)
    finally:
        if last_topic_message_count > 0:
            print_batch(last_topic, last_topic_message_count)

        consumer.close()
        client.close()

def print_batch(topic_name, message_count):
    print(f"{topic_name}: {message_count} messages")


run_consumer(consumer)
