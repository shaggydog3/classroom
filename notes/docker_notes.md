# Notes on docker procedure

## Basics

Building a container:
```
docker build -t shaggydog/imagename .
```
Run a container (example with volumes and network):
```
docker run -it -v $(pwd):/code/ --network django-tutorial_default 3100b1af937a django-admin startproject mysite
```
See what's running (get the id of a container):
```
docker ps
```
exec into a container:
```
docker exec -it cc822b275270 sh
```
bring up a compose (to run in background, add -d):
```
docker-compose up
```
See what's running in compose:
```
docker-compose ps
```
running a command on a compose node:
```
docker-compose run web manage.py migrate
```
Pushing an image to a repository (in case of swarm could be push to swarm):
```
docker push shaggydog/multi-client
```

