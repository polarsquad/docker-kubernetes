FROM ubuntu:20.04

WORKDIR /opt/myapp

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install --no-cache Flask

RUN apt-get remove -y python3-pip
RUN apt-get autoremove -y
RUN rm -rf /var/lib/apt/lists/*

COPY app.py .

CMD ["python3", "app.py"]