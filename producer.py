import time
from pulsar import Client

client = Client("pulsar://localhost:6650")  # Pulsar service URL

# Dictionary to store producers for each topic dynamically
PRODUCERS = {}

def publish_message_to_multiple_topics(topics):
    for topic in topics:
        producer = client.create_producer(topic)
        producer.send(f"Message sent to {topic}".encode("utf-8"))
        producer.close()
    client.close()
    

def produce_messages():
    topics = {"my-topic-" + str(i) for i in range(1,1000)}

    # Example usage
    publish_message_to_multiple_topics(topics)


if __name__ == "__main__":
    t1 = time.time()
    produce_messages()
    t2 = time.time()    

    print(t2-t1) # 0.6846809387207031