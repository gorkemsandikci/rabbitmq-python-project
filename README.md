# RabbitMQ Python Project

This project demonstrates a basic messaging system using RabbitMQ and Python. It includes two components:
- **Publisher**: Sends messages to a queue.
- **Consumer**: Receives and processes messages from the queue.

## Requirements

- Docker
- Python 3.x
- `pip3` for package management
- RabbitMQ

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/gorkemsandikci/rabbitmq-python-project.git
   cd rabbitmq-python-project
   ```
   
### 2. Set Up a Virtual Environment (Optional but Recommended)

    python3 -m venv venv
    source venv/bin/activate

### 3. Install Dependencies

Install pika (RabbitMQ client) using pip3:


    pip3 install pika


### 4. Run RabbitMQ with Docker

Start RabbitMQ using Docker:

    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

You can access RabbitMQ Management UI at http://localhost:15672. Default login:

    Username: guest
    Password: guest

## Running the Project

To send a message to the RabbitMQ queue, run the publisher:

    python3 publisher.py

To listen to messages from the RabbitMQ queue, open another terminal and run the consumer:

    python3 consumer.py

Once both scripts are running, you will see the message sent by the publisher appear in the consumer's terminal.

## License

This project is licensed under the MIT License.