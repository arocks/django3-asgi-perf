FROM python:3.8-alpine as builder

RUN apk --no-cache add g++ zeromq-dev libffi-dev git
COPY . /src
WORKDIR /src
RUN pip install --no-cache-dir git+https://github.com/locustio/locust.git@0.13.5#egg=locustio

FROM python:3.8-alpine

RUN apk --no-cache add zeromq && adduser -s /bin/false -D locust
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/locust /usr/local/bin/locust
COPY docker_start.sh docker_start.sh
RUN chmod +x docker_start.sh

EXPOSE 8089 5557 5558 80

USER locust
CMD ["./docker_start.sh"]
