FROM alpine:3.14

WORKDIR /opt/myapp

RUN apk update && \
    apk add python3 py3-pip && \
    pip install --no-cache Flask && \
    apk del py3-pip

COPY app.py .

CMD ["python3", "app.py"]