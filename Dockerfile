FROM python:3.11.0-slim-bullseye as python-stage-0

RUN apt-get update  -y
RUN apt-get install -y  ffmpeg

FROM python-stage-0

RUN pip install  matplotlib==3.6.2

WORKDIR /bounce
CMD ["python", "bounce.py"]
