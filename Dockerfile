FROM python:3.9.2

LABEL Maintainer="Brian Smigielski"

WORKDIR /home/pi/repos/stas_seatherstation

COPY bme_readings_influxdb.pu ./

CMD ["python", "bme_readings_influxdb.py"]
