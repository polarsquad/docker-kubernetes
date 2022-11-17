# Kubernetes exercises
This repository contains some additional Kubernetes exercises, some of these manifest files are broken in some way, some are just missing configuration data or other important pieces.

You can use tools like kubeconform to catch some of the errors, but others will just produce deployments that are broken in some way, but can still be applied to your cluster and start running, but the connections between the resources don't work properly.

You could probably use tools like 'diff' to compare to the other exercises and catch the errors, but that wouldn't help with the learning process, would it?

## Module 4 - Running Individual Containers

The original exercise: https://exercises.polarsquad.training/kubernetes-for-developers/pods/

You'll find two manifest files in the directory. First one has broken syntax, so fix it. The second one is missing some information. Fill out the missing bits.

## Module 5- Running a Fleet of Containers

Original exercise: https://exercises.polarsquad.training/kubernetes-for-developers/deploy/

One deployment, many problems. You can start with tools like kubeval, but there are multiple things going wrong here.

## Module 6 - Configuring Applications

https://exercises.polarsquad.training/kubernetes-for-developers/config/

The intention is to mount the nginx.conf to an nginx deployment.

Something's off in the configuration maybe? Try to figure out where the problem is. 

## Module 7 - Exposing Apps using Ingress

https://exercises.polarsquad.training/kubernetes-for-developers/ingress/

This exercise has three files that need some work. You'll need to specify the hostname for the ingress like in the original exercise before you start making any additional changes.

## Module 8 - Create a working deployment from scratch

You should now have the tools to be able to create a working deployment on your own.

There's a simple Python app and a Dockerfile in the directory. Build the docker image, tag it and push it to a registry provided by the trainer. Pay attention to tagging.

Now create a deployment, service and an ingress for your app. You can use the examples from the exercises, but you should pay attention to the labels. Use more descriptive labels and names here. The hostname can be the same you already used in the exercises, but you should probably use a different path for this new app. You might need to create a rewrite rule as well. More on rewrites can be found here https://kubernetes.github.io/ingress-nginx/examples/rewrite/
