FROM locustio/locust:latest

WORKDIR /mnt/locust

COPY locustfile.py /mnt/locust/locustfile.py

EXPOSE 8089

CMD ["--web-host", "0.0.0.0", "--web-port", "8089"]
