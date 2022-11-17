# Using registries

Docker push can be used to upload images. If you have a Docker Hub account you can use that for this and following exercises. Otherwise you can use europe-north1-docker.pkg.dev/tuomaspal-sandbox/training

You'll need to retag your image to use the new registry. Use `docker image ls` to find the current tag or use the image id.

```sh
➜  ~ docker image ls                                                 (arn:aws:eks:eu-west-1:120392301094:cluster/training/default)
REPOSITORY                                                                      TAG            IMAGE ID       CREATED          SIZE
temp_myapp                                                                      latest         73c8e2f8447f   31 minutes ago   27.2MB
```

Tag your image:
```sh
docker tag 73c8e2f8447f europe-north1-docker.pkg.dev/tuomaspal-sandbox/training/myapp_tuomas:latest
```

Make sure to use your name or other unique identifier for the image. You can then push it to the registry like so:
```sh
docker push europe-north1-docker.pkg.dev/tuomaspal-sandbox/training/myapp_tuomas:latest
```

If you have a Google account you can use the web interface of this registry as well.