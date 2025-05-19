# gcloud container clusters upgrade  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade)*

**NAME**

: **gcloud container clusters upgrade - upgrade the Kubernetes version of an existing container cluster**

**SYNOPSIS**

: **`gcloud container clusters upgrade` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--async)`] [`[--cluster-version](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--cluster-version)`=`CLUSTER_VERSION`] [`[--image-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--image-type)`=`IMAGE_TYPE`] [`[--master](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--master)`] [`[--node-pool](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--node-pool)`=`NODE_POOL`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Upgrades the Kubernetes version of an existing container cluster.
This command upgrades the Kubernetes version of the `node pools` or
`master` of a cluster. Note that the Kubernetes version of the
cluster's `master` is also periodically upgraded automatically as new
releases are available.
If desired cluster version is omitted, `node pool` upgrades default
to the current `master` version and `master` upgrades
default to the default cluster version, which can be found in the server config.
`During node pool upgrades, nodes will be deleted and recreated.`
While persistent Kubernetes resources, such as Pods backed by replication
controllers, will be rescheduled onto new nodes, a small cluster may experience
a few minutes where there are insufficient nodes available to run all of the
scheduled Kubernetes resources.
`Please ensure that any data you wish to keep is stored on a
persistent` `disk before upgrading the cluster.` Ephemeral
Kubernetes resources--in particular, Pods without replication controllers--will
be lost, while persistent Kubernetes resources will get rescheduled.

**EXAMPLES**

: Upgrade the node pool `pool-1` of `sample-cluster` to the
Kubernetes version of the cluster's master.

```
gcloud container clusters upgrade sample-cluster --node-pool=pool-1
```

Upgrade the node pool `pool-1` of `sample-cluster` to
Kubernetes version 1.14.7-gke.14:

```
gcloud container clusters upgrade sample-cluster --node-pool=pool-1 --cluster-version="1.14.7-gke.14"
```

Upgrade the master of `sample-cluster` to the default cluster
version:

```
gcloud container clusters upgrade sample-cluster --master
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the cluster to upgrade.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster-version**:
The GKE release version to which to upgrade the cluster's node pools or master.
If desired cluster version is omitted, `node pool` upgrades default
to the current `master` version and `master` upgrades
default to the default cluster version, which can be found in the server config.
You can find the list of allowed versions for upgrades by running:

```
gcloud container get-server-config
```

**--image-type**:
The image type to use for the cluster/node pool. Defaults to server-specified.
Image Type specifies the base OS that the nodes in the cluster/node pool will
run on. If an image type is specified, that will be assigned to the cluster/node
pool and all future upgrades will use the specified image type. If it is not
specified the server will pick the default image type.
The default image type and the list of valid image types are available using the
following command.

```
gcloud container get-server-config
```

**--master**:
Upgrade the cluster's master. Node pools cannot be upgraded at the same time as
the master.

**--node-pool**:
The node pool to upgrade.

**--location**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha container clusters upgrade
```

```
gcloud beta container clusters upgrade
```