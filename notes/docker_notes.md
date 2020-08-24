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

Exec into a container:
```
docker exec -it cc822b275270 sh
```

Pushing an image to a repository (in case of swarm could be push to swarm):
```
docker push shaggydog/multi-client
```

List images
```
docker images
```

List networks
```
docker network ls
```

## Docker Compose

Bring up a compose (to run in background, add -d):
```
docker-compose up
```

See what's running in compose:
```
docker-compose ps
```

Running a command on a compose node:
```
docker-compose run web manage.py migrate
```

Bringing down a running compose:
```
docker-compose down
```

## Swarming

Taken from: https://docs.docker.com/engine/swarm/stack-deploy/

Switching to swarm mode:
```
docker swarm init
```

Creating a local registry (swarm needs a registry, you can use a local one, or use docker hub); creates a container that acts as a registry.
```
docker service create --name registry --publish published=5000,target=5000 registry:2
```

Check that the registry is running (should say 1/1 under REPLICAS):
```
docker service ls
```

Check it's working with curl:
```
curl http://localhost:5000/v2/
```


## Kubernetes with minikube

Start minikube:
```
minikube start
```

Check the status of kubernetes:
```
kubectl cluster-info
```

Show the nodes that can be used:
```
kubectl get nodes
```

Create deployment:
```
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

### basic kubernetes troubleshooting commands:
kubectl get - list resources
kubectl describe - show detailed information about a resource
kubectl logs - print the logs from a container in a pod
kubectl exec - execute a command on a container in a pod

Proxy access to the kubernetes cluster (runs in foreground, use a different terminal window/tab):
```
kubectl proxy
```

Access logs from the container:
```
kubectl logs $POD_NAME
```

Execute commands on the container:
```
kubectl exec $POD_NAME
```

Get a bash session on a container
```
kubectl exec -ti $POD_NAME bash
```


