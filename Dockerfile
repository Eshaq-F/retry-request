FROM python:3.4

ADD . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt

RUN celery worker -A vgang_job.app.app -l info --pool solo
RUN echo Hello
CMD ["python3", "main.py"]