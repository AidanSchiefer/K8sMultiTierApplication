# K8sMultiTierApplication

## Overview

This project (starting out) is a basic "Learning Kubernetes" project along with understanding some system design. This project mimics deploying a
multi-tier application by deploying different images pulled from Docker for the Frontend, API layer, and Backend. This project aims to be a good practice for writing YAML
deployment files, practicing using the kubectl command, using Docker and Docker images, and get a better understanding of how Kubernetes may be used at a higher level when mixed with
different tech stacks. 

*Note:* This project will be an ongoing endeavor with new features and updates being made to it.

### Outline of the Environment

Instead of deploying a single, complicated application, this project aims to build a simple three-tier application environment:

```
Namespace: test-lab

         |
         V

Frontend Pod: nginx

         |
         V

API Pod: BusyBox

         |
         V

Backend Pod: PostgreSQL
```

### Future Development Plans

* Replace the BusyBox deployment with a custom Python or GO API layer for interacting dynamically with the Postgres backend (IN PROGRESS)
* Update the frontend to be a custom JavaScript website that will interact with the API layer to get data from the backend
* Set up GitHub Actions CI/CD Pipeline to automatically catch errors and re-deploy the cluster every push
* Fully flesh out the project to be an imitation of a VMware vSphere or RedHat OpenShift UI/functionality. Spinning up "VMs" will be image deployments

## Creating the Project Structure

When creating this project, the following structure was used. For these instructions, minikube and Docker have already been installed, and the minikube cluster
has already been deployed.

Create a project directory:

``` bash
mkdir k8s-3tier-lab
cd k8s-3tier-lab
```

Create the necessary files:

``` bash
touch namespace.yaml
touch postgres.yaml
touch postgres-service.yaml
touch busybox.yaml
touch nginx.yaml
```

## Creating the Project Namespace

After spinning up the local minikube cluster, the first step is to use the `namespace.yaml` file to create the project namespace. This can be done using:

``` bash
kubectl apply -f namespace.yaml
```

The following command can be used to verify the namespace was created successfully:

``` bash
kubectl get ns
```

## Deploying a PostgreSQL Backend

Now that the projects namespace has been created, the PostgreSQL backend must be deployed using the `postgres.yaml` file. This can be done using:

``` Bash
kubectl apply -f postgres.yaml
```

The following command can be used to verify the Postgres deployment was created sucessfully:

``` bash
kubectl get pods -n test-lab
```

## Creating a PostgreSQL Service

Since pods can come and go, having an actual service deployed allows the cluster to have stable networking even if pods go down

The PostgreSQL service must be deployed using the `postgres-service.yaml` file. This can be done using:

``` Bash
kubectl apply -f postgres-service.yaml
```

The following command can be used to verify the Postgres Service was created successfully:

``` Bash
kubectl get svc -n test-lab
```

## Testing PostgreSQL Connectivity with BusyBox

The next step in building this Multi-Tier appliation is creating the API connector between the backend and the frontend. To start, this will be done using 
a BusyBox Pod.

The BusyBox Pod must be deployed using the `busybox.yaml` file. This can be done using:

``` Bash
kubectl apply -f busybox.yaml
```

The following command can be used to verify the BusyBox Pod was created successfully:

``` Bash
kubectl get pods -n test-lab
```

## Entering the BusyBox Pod

You can open up a shell CLI inside the BusyBox Pod using the following command:

``` Bash
kubectl exec -it busybox -n test-lab -- sh
```

Inside the BusyBox Pod, you can test the DNS connection using the following command:

``` Bash
nslookup postgres
```

## Deploying the Nginx Frontend

Now that the backend and the API layer have been deployed, all that is left is to deploy the nginx frontend

The nginx deployment must be deployed using the `nginx.yaml` file. This can be done using:

``` Bash
kubectl apply -f nginx.yaml
```

The following command can be used to verify the nginx deployment was created successfully:

``` Bash
kubectl get deployment -n test-lab
```

## Creating the Custom Python API Layer

This part of the project is currently being developed. The goal is to use FastAPI to be able to communicate with the Postgres DB. 