# Section: Containers

### From CRW, build and push container

### From Windows machine

```
podman run --name simplecontainer -d -p 8080:8080 quay.io/mouimet/simplecontainer:v1
```
```
Invoke-RestMethod -Uri http://localhost:8080
```

### From Linux machine

```
podman run --name simplecontainer -d -p 8080:8080 quay.io/mouimet/simplecontainer:v1
```
```
curl http://localhost:8080
```

### Update the code with version 2, build and push

### Rerun on Linux and windows 

```
podman rm -f simplecontainer
podman run --name simplecontainer -d -p 8080:8080 quay.io/mouimet/simplecontainer:v2
```

```
curl http://localhost:8080
```
```
Invoke-RestMethod -Uri http://localhost:8080
```

# Section: Orchestration

### Explain and apply manifests on Kubernetes

```
oc apply -f manifests

```
### Access the App
```
curl https://simplecontainer.apps.hiybv6c8.eastus.aroapp.io
```

### Scale the App 

```
oc scale --replicas=5 deployment/simplecontainer
```

### Kill pods and look at resiliency


# Section: Operators

From Dev Console

- Click +Add
- Operator Backed
- Search for Kafka
- Create Kafka
- Let all the defaults
- Create

# Section: Develop with Openshift

From Dev Console

- Click +Add
- Import from Git  https://github.com/marouim/gestiontransaction.git
- Openshift will validate .NET 5
- Advanced Options
- - click: Show advanced Routing options
- - click Secure Route
- - TLS termination: Edge
- click Create

# Section: Hybrid Cloud


