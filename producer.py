import asyncio
import time
from pulsar.asyncio import Client


async def send_message_to_topic(client, topic, message):
    producer = await client.create_producer(topic)
    try:
        await producer.send(message)
    finally:
        await producer.close()


async def produce_messages(topics):
    client = Client("pulsar://localhost:6650")
    tasks = []
    try:
        for topic in topics:
            message = f"Message sent to {topic}".encode("utf-8")

            tasks.append(send_message_to_topic(client, topic, message))
        await asyncio.gather(*tasks)
    finally:
        await client.close()


if __name__ == "__main__":
    topics = {"my-topic-" + str(i) for i in range(1, 5000)}

    t1 = time.time()
    asyncio.run(produce_messages(topics))
    t2 = time.time()

    print(f"Time taken: {t2 - t1:.2f} seconds")
