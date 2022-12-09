FROM ubuntu:20.04

WORKDIR /opt/myapp

RUN apt-get update && apt-get install -y python3 python3-pip \ 
&& pip3 install --no-cache Flask \
&& apt-get remove -y python3-pip \
&& apt-get autoremove -y \
&& rm -rf /var/lib/apt/lists/* 

RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
USER appuser

COPY --chown=appuser:appuser app.py .

CMD ["python3", "app.py"]