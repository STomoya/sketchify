FROM python:3.7
RUN apt update -y && \
    apt upgrade -y && \
    apt install -y \
    libgl1-mesa-glx
COPY ./docker/requirements.txt requirements.txt
RUN pip --default-timeout=100 install -r requirements.txt