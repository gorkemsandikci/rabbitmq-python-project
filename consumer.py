import pika

# RabbitMQ'ya bağlan
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Mesajların alınacağı kuyruk
channel.queue_declare(queue='hello')

# Mesajları işleme fonksiyonu
def callback(ch, method, properties, body):
    print(f" [x] Alınan mesaj: {body.decode()}")

# Mesajları kuyruktan al ve işleme fonksiyonuna yönlendir
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Mesajlar bekleniyor. Çıkmak için CTRL+C.')

# Mesajları sürekli dinle
channel.start_consuming()
