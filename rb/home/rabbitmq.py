import pika

def publish_message(message):
    params = pika.URLParameters('amqps://irjdveib:0jmHwHsIMK0lA9bMiHAZay0aP1Ok--LH@shrimp.rmq.cloudamqp.com/irjdveib')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare("my_queue")
    channel.basic_publish(exchange='',routing_key='my_queue',body=message)
    channel.close()