# Producer (Sender)
import pika

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='hello')

    # Send a message
    channel.basic_publish(exchange='', routing_key='hello', body='Hello, World!')
    print(" [x] Sent 'Hello, World!'")

    connection.close()

# Consumer (Receiver)
def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='hello')

    # Callback function to process messages
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # Consume messages from the queue
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Run the producer and consumer in separate processes or terminals