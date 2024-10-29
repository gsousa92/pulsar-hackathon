import asyncio
import random
import time
from pulsar.asyncio import Client
import logging

null_logger = logging.getLogger("null_logger")
null_logger.addHandler(logging.NullHandler())

# Total number of topics
TOPICS_COUNT = 25

# Number of messages per topic will be a random between the following min and max values
MAX_MESSAGE_PER_TOPIC = 5
MIN_MESSAGE_PER_TOPIC = 1

# specific number of messages generated to specific topics
CUSTOM_TOPICS = {
    "organization-1": 1000,
    "organization-10": 1000
}


async def send_message_to_topic(client, topic, message):
    producer = await client.create_producer(topic)
    try:
        await producer.send(message)
    finally:
        await producer.close()


async def produce_messages(topics):
    client = Client("pulsar://localhost:6650", logger=null_logger)
    tasks = []
    try:
        for topic in topics:
            if topic in CUSTOM_TOPICS:
                number_of_messages = CUSTOM_TOPICS[topic]
            else:
                number_of_messages = random.randint(MIN_MESSAGE_PER_TOPIC, MAX_MESSAGE_PER_TOPIC)

            for message in range(number_of_messages):
                message = f"Message sent to {topic}".encode("utf-8")
                tasks.append(send_message_to_topic(client, topic, message))

            print(f"Published {number_of_messages} to {topic}")

        await asyncio.gather(*tasks)
    finally:
        await client.close()

    return len(tasks) # return nr of sent messages

if __name__ == "__main__":
    topics = {"organization-" + str(i) for i in range(0, TOPICS_COUNT)}

    t1 = time.time()
    messages_sent_count = asyncio.run(produce_messages(topics))
    t2 = time.time()

    print(f"{messages_sent_count} messages sent.")
    print(f"Time taken: {t2 - t1:.2f} seconds")
