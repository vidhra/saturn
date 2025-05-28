# gcloud container  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container](https://cloud.google.com/sdk/gcloud/reference/container)*

**NAME**

: **gcloud container - deploy and manage clusters of machines for running containers**

**SYNOPSIS**

: **`gcloud container` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/container#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud container command group lets you create and manage Google Kubernetes
Engine containers and clusters.
Kubernetes Engine is a cluster manager and orchestration system for running your
Docker containers. Kubernetes Engine schedules your containers into the cluster
and manages them automatically based on requirements you define, such as CPU and
memory.
More information on Kubernetes Engine can be found here: [https://cloud.google.com/kubernetes-engine](https://cloud.google.com/kubernetes-engine)
and detailed documentation can be found here: [https://cloud.google.com/kubernetes-engine/docs/](https://cloud.google.com/kubernetes-engine/docs/)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[attached](https://cloud.google.com/sdk/gcloud/reference/container/attached)`**:
Manage Attached clusters for running containers.

**`[aws](https://cloud.google.com/sdk/gcloud/reference/container/aws)`**:
`(DEPRECATED)` Deploy and manage clusters of machines on AWS for
running containers.

**`[azure](https://cloud.google.com/sdk/gcloud/reference/container/azure)`**:
`(DEPRECATED)` Deploy and manage clusters of machines on Azure for
running containers.

**`[bare-metal](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal)`**:
Deploy and manage Anthos clusters on bare metal for running containers.

**`[binauthz](https://cloud.google.com/sdk/gcloud/reference/container/binauthz)`**:
Manage attestations for Binary Authorization on Google Cloud Platform.

**`[clusters](https://cloud.google.com/sdk/gcloud/reference/container/clusters)`**:
Deploy and teardown Google Kubernetes Engine clusters.

**`[fleet](https://cloud.google.com/sdk/gcloud/reference/container/fleet)`**:
Centrally manage features and services on all your Kubernetes clusters with
fleet.

**`[hub](https://cloud.google.com/sdk/gcloud/reference/container/hub)`**:
Centrally manage features and services on all your Kubernetes clusters with
fleet.

**`[images](https://cloud.google.com/sdk/gcloud/reference/container/images)`**:
List and manipulate Google Container Registry images.

**`[node-pools](https://cloud.google.com/sdk/gcloud/reference/container/node-pools)`**:
Create and delete operations for Google Kubernetes Engine node pools.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/container/operations)`**:
Get and list operations for Google Kubernetes Engine clusters.

**`[subnets](https://cloud.google.com/sdk/gcloud/reference/container/subnets)`**:
Manage subnets to be used by Google Kubernetes Engine clusters.

**`[vmware](https://cloud.google.com/sdk/gcloud/reference/container/vmware)`**:
Deploy and manage Anthos clusters on VMware for running containers.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[get-server-config](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config)`**:
Get Kubernetes Engine server config.

**NOTES**

: These variants are also available:

```
gcloud alpha container
```

```
gcloud beta container
```