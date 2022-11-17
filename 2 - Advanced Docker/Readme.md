# Advanced Docker subjects

## Optimizing Docker images

There is a Dockerfile in this directory and a Python app called app.py. We'll use this for figuring out how to optimize our image size.

First run `docker build -t myapp .` and `docker images myapp`. If you want you can try running the app as well with `docker run --rm -d --name myapp -p 3000:3000 myapp`

Now, the Dockerfile is far from optimal. See what you can do about removing clutter from the image. The key is to create small layers. You should be able to get the image down to around 130 MB.

You should also switch to a non-root user. You should add this line `groupadd -g 999 appuser && seradd -r -u 999 -g appuser appuser` to the Dockerfile. You'll need to switch to the new user and group as well. You can use `USER` for that.

## Docker multistage build

Let's use the Dockerfile and app code that's stored in training_demo/dockerDemo/

Switch to the directory and run `docker build -t hello_http .` in the directory containing the Dockerfile and the code.

You can then run the app with the Redis server created earlier.

`docker run --rm -d --name app -p 8080:8080 -e REDIS=redis-server --network app hello_http`

Use curl or browser to reach your app at http://localhost:8080/helloworld

Stop your app with `docker stop`.

## Docker Compose

Create a docker-compose.yaml file with the following content:

```yaml
version: '3'
services:
  redis:
    image: redis
    networks:
      - exercise
  myapp:
    build: .
    ports:
      - "8080:8080"
    environment:
      REDIS: redis
    networks:
      - exercise
    volumes:
      - redis_data:/data
networks:
  exercise:
    name: exercise
    driver: bridge
volumes:
  redis_data:
```

Run `docker-compose up` to build the container and run the stack.

You can then reach your app with curl or browser at http://localhost:8080/helloworld

## .devcontainers

## Finishing up

`docker network rm app`
`docker volume rm redis`

and

`docker-compose rm`