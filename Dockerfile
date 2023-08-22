FROM python:3.10.6-buster

ARG GID=1000
ARG UID=1000

RUN groupadd -o -g $GID docker \
    && useradd -o -m -u $UID -g $GID -s /bin/bash docker

WORKDIR /app
COPY --chown=docker:docker src /app

ENV PYTHONPATH=$PYTHONPATH:/app
ENV APP_BASE=/app/

RUN apt-get update \
    && apt-get install -y libpcre3 libpcre3-dev socat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip --disable-pip-version-check install -r requirements.txt

USER docker

CMD ["python3", "app.py"]
