# Exposing the app

## Before we start

Let's make sure that the echo-server is alive and well. Let's use port-forward to check.
Run `kubectl port-forward deployment/demo 8080:8080`. You can now reach one of the pods from your localhost on port 8080.

## Services

## Ingresses