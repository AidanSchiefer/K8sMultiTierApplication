# K8sMultiTierApplication

## Overview

This project (starting out) is a basic "Learning Kubernetes" project along with understanding some system design. This project mimics deploying a
multi-tier application by deploying different images for the Frontend, API layer, and Backend. This project aims to be a good practice for writing YAML
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