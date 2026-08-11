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