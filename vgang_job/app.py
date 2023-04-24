from os import environ, path
from celery import Celery
import requests


app = Celery(broker=environ['BROKER_URL'], backend=environ['RESULT_BACKEND'])
max_retry = int(environ.get('max_retry', 5))


@app.task(bind=True, max_retries=max_retry, track_started=True)
def retry_request(self, url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('Request fail with status: ' + str(response.status_code))

        return response.json()
    except Exception as e:
        countdown = 2 ** self.request.retries
        self.retry(countdown=countdown, exc=e)
