<p align="center">
	Docker setup for Locust.io load testing tool
</p>

***

Based on the official Dockerfile, this Docker setup starts from the alpine python base image for minimum size.

## Quick Start

If you are in a hurry, just follow these steps. 

1. Copy your `locustfile.py` to `tests/` directory
1. Open `docker-compose.yml` and change `LOCUSTFILE_PATH` to point to that test file
1. Run `docker-compose build`. This takes a while, so you can start sword-fighting now.
1. Run `docker-compose up -d`
1. Wait for a few seconds for the services to be up and running. Then open the app at http://localhost:8089

## Non-gui runs

``` bash
docker-compose run locust-standalone locust --host http://localhost -f tests/polls.py --no-web --clients 300 --hatch-rate 300 --run-time 10s --only-summary

docker-compose run locust-standalone locust --host http://localhost -f tests/polls.py --no-web --clients 100 --hatch-rate 100 --run-time 60s --only-summary --step-load --step-clients 100 --step-time 20s
```
