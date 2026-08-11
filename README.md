# K8sMultiTierApplication

## Overview

This project (starting out) is a basic "Learning Kubernetes" project along with understanding some system design. This project mimics deploying a
multi-tier application by deploying different images for the Frontend, API layer, and Backend. This project aims to be a good practice for writing YAML
deployment files, practicing using the kubectl command, and get a better understanding of how Kubernetes may be used at a higher level when mixed with
different tech stacks. 

Note: This project will be an ongoing endeavor with new features and updates being made to it.

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