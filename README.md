## nginx-gunicorn-flask

This repository contains files necessary for building a Docker image of
Nginx + Gunicorn + Flask.


### Base Docker Image

* [ubuntu:12.04](https://registry.hub.docker.com/_/ubuntu/)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/danriti/nginx-gunicorn-flask/) from public [Docker Hub Registry](https://registry.hub.docker.com/):

```bash
docker pull danriti/nginx-gunicorn-flask
```


### Usage

```bash
docker run -d -p 80:80 danriti/nginx-gunicorn-flask
```

After few seconds, open `http://<host>` to see the Flask app.
