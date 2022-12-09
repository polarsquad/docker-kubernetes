# Exposing the app

## Before we start

Let's make sure that the echo-server is alive and well. Let's use port-forward to check.
Run `kubectl port-forward deployment/demo 8080:8080`. You can now reach one of the pods from your localhost on port 8080.

## Services

You'll need to create a new manifest file. Name it service.yaml and copy the following content there:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-service
  labels:
    app: demo
spec:
  selector:
    app: demo-pod
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
```

What this is does is map the port 8080 of your app to one service and one port 80. This is then accessible from within your namespace as a service called `demo` and within the cluster as `demo`. You can try this out by running a curl pod.

## Ingresses

You can then create an ingress for your service.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: demo-ingress
  labels:
    app: demo
spec:
  rules:
  - host: <namespace>.k8s.polarsquad.training
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: hello-http-service
            port:
              number: 80
```

Your nginx app would then be reachable through the url `http://<namespace>.k8s.polarsquad.training/`