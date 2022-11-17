# Docker Basics

## Docker Hub

Go to https://hub.docker.com/ and search for images. Try to find something interesting

You can look at other public registries as well, eg. https://gcr.io or https://gallery.ecr.aws.

For example, MySQL has an image available at Docker Hub https://hub.docker.com/_/mysql

Usually the official, well supported images have instructions on how to run the container. MySQL is
one of the better documented ones.

## Docker Pull

Now pull one of the images that caught your eye. Use the `docker pull` command.

## Docker Run

Now that you've got the image stored locally try running it. Use `docker run`. You don't have to pull the image before running it, Docker automatically 
pulls it for you, though. Depending on the image you've chosen you might need to specify some parameters. Docker images take their configuration either as environment variables or configuration files that are mounted in the running container.

You can use options like `-it`, `--rm` and `-d` to manage how the container is running in your terminal. Experiment with those a bit. The `--rm` flag especially is a good option, especially when you're trying things out and figuring the configuration for a particular image. It automatically deletes the container once the process has exited.

For example:
`docker run -it --rm -e MYSQL_ROOT_PASSWORD=test --name mysql mysql:latest`

Or with local filesystem used for mounting the data:
`docker run --name some-mysql -v /my/own/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest`

## Handling Docker images and containers

Run `docker ps -a` to see what containers are on your computer. The `-a` option will show all containers, even stopped ones. You can then use `docker rm` to delete any dangling images one by one.

Run `docker image ls` to see what images are stored locally.

## Docker volumes

You can use v

`docker volume create redis`

`docker volume ls`

## Docker networks

`docker network create -d bridge app`

`docker network ls`

## Use the network and volume to run a container

`docker run --rm --name redis-server --network app --mount 'type=volume,src=redis,dst=/data' -d redis`



