FROM python:3.10-alpine3.16

RUN pip install --upgrade pip
RUN pip3 install python3-tk
RUN apk add python3-tkinter

WORKDIR /app

# Generating a universally unique ID for the Container
RUN  dbus-uuidgen > /etc/machine-id

ENTRYPOINT ["python3", "main.py"]
