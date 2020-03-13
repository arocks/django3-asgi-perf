# django3-asgi-perf

This is set of Django stacks on Docker to check the performance of running in WSGI and ASGI configurations. The Django application sitting in the `djangoapp` directory is based on the official [Polls tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/). Since it is mounted into the container, code changes will be automatically applied. All the customizable configuration variables are in the `config` directory.


