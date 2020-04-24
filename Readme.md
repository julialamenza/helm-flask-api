# Helm Chart to deploy a Flask API dockerized.

### I use Kubectl and minikube for make this works


##### Follow this guide if you dont have docker and kubernetes installed in your computer (Mac OS)



#### - Docker

```

brew install docker
```


**or**

```

Download Docker for mac from the url : https://download.docker.com/mac/stable/Docker.dmg
```


**check your docker version**

```
docker version
```


#### Kubernetes (Kubectl)

```
brew install kubectl
```


**or**


- Download the latest release:

```
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
To download a specific version, replace the $(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt) portion of the command with the specific version.
```

```
For example, to download version v1.18.0 on macOS, type:

```

```
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/darwin/amd64/kubectl
```



- Make the kubectl binary executable.

```
chmod +x ./kubectl
```

- Move the binary in to your PATH.

```
sudo mv ./kubectl /usr/local/bin/kubectl
```



**check your kubectl version**

```
kubectl version --client
```



### Helm

```
brew install helm
```


**or**

```
Download your version - https://github.com/helm/helm/releases
```


Unpack it

```
tar -zxvf helm-v3.0.0-linux-amd6
```


Find the helm binary in the unpacked directory, and move it to its desired destination

```
mv linux-amd64/helm /usr/local/bin/helm
```

**check helm version**

```
helm version
```



### Start kubectl 

- Start Minikube and create a cluster:

```
minikube start
```

### clone this repository

```
git clone https://github.com/julialamenza/helm-flask-api.git
```

- go to the folder

```
cd helm-flask-api/
```



### Install your helm

```
helm install ./helm-chart --generate-name
```

### check your minikube service

```
minikube service list
````
You are going to see your helm chart <name> in a list with a **TargetPort** and **URL**
Use this url and acess it in your browser or using **curl**

````
curl <url>

````

Remember your app route exist in ```/ready``` and ```/will``` so in path **"/"** you will see a **Not Found** error

**- If you wanna know more about your pod use this command**

````
kubectl describe pod <your pod name>
````
**- You can check your endpoints using this**

````
kubectl -n <namespace> get endpoints
`````

For more information check Kubernetes documentation -> https://kubernetes.io/docs/home/
