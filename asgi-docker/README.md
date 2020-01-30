<p align="center">
	Docker setup for Django Polls app + Postgres + Uvicorn + Gunicorn + Nginx
</p>

***

This is a Django stack on Docker with focus on simplicity. The Django application sitting in the `djangoapp` directory is based on the official [Polls tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/). Since it is mounted into the container, code changes will be automatically applied. All the customizable configuration variables are in the `config` directory.

## Quick Start

If you are in a hurry, just follow these steps:

```bash
cp config/django/example.env config/django/.env
cp config/postgres/example.env config/postgres/.env
docker-compose up -d --build
docker-compose run djangoapp python manage.py migrate
docker-compose run djangoapp python manage.py collectstatic --no-input -v 2
```

Wait for a few seconds for the services to be up and running. Then open the app at http://localhost

## Common Tasks

### Shutting Down

``` bash
docker-compose down
```

### Load Initial Data

```bash
docker-compose run djangoapp /bin/sh -c "python manage.py flush; python manage.py migrate; python manage.py loaddata potter-fixture.json"
docker-compose run djangoapp python manage.py createsuperuser
```

### View Error Logs

If running in the project directory `wsgi-docker` then it is usually:

``` bash
docker logs wsgi-docker_nginx_1
docker logs wsgi-docker_djangoapp_1
```

## Cleanup

Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.

``` bash
docker system prune -f
docker system prune -f --volumes
```

## Production

In production, you might have to make many changes especially around security. It is recommended to create an application user as Docker containers will use the root user by default. The permissions can be restricted to that user. The docker image sizes can be reduced with multi-stage builds.

Refer code from [testdriven.io](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/), [rowdybeaver](https://github.com/rowdybeaver/sample-django-docker) and [Docker official docs](https://docs.docker.com/compose/production/) for details on the docker-compose production setup.

Note: typically you would use a cloud-based database than run a database like Postgres in a docker container ([why?](https://vsupalov.com/database-in-docker/) but some people have no issues) in production. Even more, if you have a popular app then you will need something like Docker Swarm or Kubernetes rather than Docker Compose to scale up.
