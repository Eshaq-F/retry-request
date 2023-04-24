# Retry Request Project

This is a sample project that demonstrates how to use Celery in a Dockerized Python environment. It includes a Celery task that retries a failing request with exponentially increasing delay between retries, and a Python script that calls the Celery task.

## Installation

To use this project, you'll need to have Docker and Docker Compose installed on your machine.

1. Clone this repository:

&emsp;&emsp;`git clone https://github.com/Eshaq-F/retry-request.git`

2. Navigate to the project directory:

&emsp;&emsp;`cd retry-request`


3. Build the Docker image:

&emsp;&emsp;`docker build -t my_celery_project .`



## Usage

To run the Celery worker and the Python script that calls the Celery task, use the following command:


&emsp;`docker-compose up -d`


This will start the Docker containers in detached mode. You can then check the logs of the containers with the following command:

&emsp;`docker-compose logs -f`


This will show the logs of the Celery worker and the Python script that calls the Celery task.

## Configuration

You can configure the Celery task by modifying the `tasks.py` file. Specifically, you can change the maximum number of retries by changing the `max_retries` argument in the `retry_request` task. You can also change the base delay between retries by changing the `countdown` argument in the `self.retry()` method.


-----

## Conclusion

That's it! You now have a Dockerized Python Celery project that demonstrates how to retry failing requests with exponentially increasing delay between retries. Feel free to modify the project to suit your needs, and don't hesitate to reach out if you have any questions.
