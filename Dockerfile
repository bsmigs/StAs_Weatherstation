FROM python:latest

LABEL Maintainer="Brian Smigielski"

CMD ["python", "bme_readings_influxdb.py"]
