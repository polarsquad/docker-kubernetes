# DOCKER DEMO

## Pull an image

`docker pull hello-world`

## Run Hello World image

`docker run hello-world`

## Show images

`docker ps -a`

## Delete the exited container

`docker rm <container name>`

## Run container and clean up automatically

`docker run --rm hello-world`

## Build an image from a Dockerfile

`docker build -t hello_http .`

## Create a network

`docker network create -d bridge app`

`docker network ls`

## Create a volume for Redis

`docker volume create redis`

## Create a Redis instance in the new network

`docker run --rm --name redis-server --network app --mount 'type=volume,src=redis,dst=/data' -d redis`

## Run the app, attach it to app network and connect to Redis

`docker run --rm -d --name app -p 8080:8080 -e REDIS=redis-server --network app hello_http`

Curl or browser to http://localhost:8080/helloworld

## Check the network

`docker network inspect app`

You can see what containers are attached to the network

## Stop and recreate Redis to show persistence

`docker stop redis-server`

Curl or browser to http://localhost:8080/helloworld

`docker run --rm -d --name app -p 8080:8080 -e REDIS=redis-server --network app hello_http`

## Clean up afterwards

`docker network rm app`
`docker volume rm redis
