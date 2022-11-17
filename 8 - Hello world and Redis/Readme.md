# Multiple services

Now we want to connect apps to each other. Let's use the image we built earlier and create manifest files for it and a Redis service. You might want to delete your deployments, services and ingresses before starting with these exercises.

## Redis

Might be a good idea to start with Redis. We'll skip creating a PersistentVolume which would be used for persisting the data. All we care about is getting a Redis to respond to our queries. There is a redis-deployment.yaml in this directory. You'll need to create a service to match it. There is a redis-service.yaml file in the same directory. You'll need to edit it to complete the service. 

Tip: Redis uses port 6379 for traffic