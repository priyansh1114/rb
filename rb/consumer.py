import pika

def callback(ch,mehtod,properties,body):
    print(ch,body,mehtod)


params = pika.URLParameters('amqps://irjdveib:0jmHwHsIMK0lA9bMiHAZay0aP1Ok--LH@shrimp.rmq.cloudamqp.com/irjdveib')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare('my_queue')
channel.basic_consume(queue='my_queue', on_message_callback=callback,auto_ack=True)
print("Consume redy to consume RabbitMQ")
channel.start_consuming()
