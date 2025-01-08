FROM python:3.13.1-alpine3.21
COPY ./client.py /usr/src/app/client.py
COPY ./requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "client.py"]