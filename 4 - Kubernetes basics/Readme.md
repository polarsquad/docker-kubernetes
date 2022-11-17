# Basics and connecting

## Kubectl commands

* get
* describe
* create
* delete
* apply
* explain

More can be found at https://kubernetes.io/docs/reference/kubectl/cheatsheet/

## Kubectl connection, namespaces and contexts

Make sure that your connection is working with `kubectl cluster-info`. 

Get a list of contexts by running `kubectl config get-contexts`

You should see your cluster connection and the namespace listed. 

## First app

Copy the first_manifest.yaml from training_demo/kubernetesDemo/ and edit it a bit.

Find this bit and edit it:
```yaml
spec:
  rules:
  - host: tr-tuomas-palosaari-polarsquad-com.k8s.polarsquad.training
    http:
```

Change the first part of host to match your own namespace you got in the previous steps. They should follow the format of `tr-firstname-lastname-mylab-fi`. 

Then you can run `kubectl apply -f first_manifest.yaml`. You can then reach a demo application in a few moments at `tr-firstname-lastname-mylab-fi.k8s.polarsquad.training`.

Get a list of resources the manifest created by running `kubectl get all`. 

You can run `kubectl get pods` or `kubectl rollout status deployment/hello-world-app` to see what's happening with the app.

Other resources you might find interesting are:
* ingress
* service
* secret 
* configmap

You can use `kubectl get` to see these and many others.

If you want to see the deployment manifest you can use `kubectl get deployment/hello-world-app -o yaml`.