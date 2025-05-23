# 🚀 FastAPI Queue Manager with Celery & Redis

A minimal REST API built with **FastAPI**, **Celery**, and **Redis** to demonstrate background task processing and queue monitoring with dockerized environment.

---

## Features

- Submit tasks via REST API
- Process tasks asynchronously using Celery
- Monitor queues using Flower
- Redis as broker and result backend
- Dockerized setup for easy start

---

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Celery](https://docs.celeryq.dev/)
- [Redis](https://redis.io/)
- [Flower](https://flower.readthedocs.io/en/latest/)
- Docker + Docker Compose

---

## Setup Instructions

1. Clone the Repository

```bash
$ git clone https://github.com/your-username/fastapi-queue-monitor.git
$ cd fastapi-queue-monitor
$ docker-compose up --build
```
##  Access the App
• API Docs: http://localhost:8000/docs
• Flower (Task Monitor): http://localhost:5555