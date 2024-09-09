import pika

# RabbitMQ'ya bağlan
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Mesajların gönderileceği bir kuyruk oluştur
channel.queue_declare(queue='hello')

# Mesaj gönder
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Merhaba, RabbitMQ!')

print(" [x] Mesaj gönderildi: 'Merhaba, RabbitMQ!'")

# Bağlantıyı kapat
connection.close()
