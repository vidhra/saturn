# gcloud dataproc clusters gke create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create)*

**NAME**

: **gcloud dataproc clusters gke create - create a GKE-based virtual cluster**

**SYNOPSIS**

: **`gcloud dataproc clusters gke create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--region)`=`REGION`) `[--spark-engine-version](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--spark-engine-version)`=`SPARK_ENGINE_VERSION` (`[--gke-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--gke-cluster)`=`GKE_CLUSTER` : `[--gke-cluster-location](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--gke-cluster-location)`=`GKE_CLUSTER_LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--async)`] [`[--namespace](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--namespace)`=`NAMESPACE`] [`[--pools](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--pools)`=[`KEY`=`VALUE`[;`[VALUE](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#VALUE)`],…]] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--properties)`=[`PREFIX`:`[PROPERTY](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#PROPERTY)`=`VALUE`,…]] [`[--setup-workload-identity](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--setup-workload-identity)`] [`[--staging-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--staging-bucket)`=`STAGING_BUCKET`] [`[--history-server-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--history-server-cluster)`=`HISTORY_SERVER_CLUSTER` : `[--history-server-cluster-region](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--history-server-cluster-region)`=`HISTORY_SERVER_CLUSTER_REGION`] [`[--metastore-service](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--metastore-service)`=`METASTORE_SERVICE` : `[--metastore-service-location](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#--metastore-service-location)`=`METASTORE_SERVICE_LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a GKE-based virtual cluster.

**EXAMPLES**

: Create a Dataproc on GKE cluster in us-central1 on a GKE cluster in the same
project and region with default values:

```
gcloud dataproc clusters gke create my-cluster --region=us-central1 --gke-cluster=my-gke-cluster --spark-engine-version=latest --pools='name=dp,roles=default'
```

Create a Dataproc on GKE cluster in us-central1 on a GKE cluster in the same
project and zone us-central1-f with default values:

```
gcloud dataproc clusters gke create my-cluster --region=us-central1 --gke-cluster=my-gke-cluster --gke-cluster-location=us-central1-f --spark-engine-version=3.1 --pools='name=dp,roles=default'
```

Create a Dataproc on GKE cluster in us-central1 with machine type
'e2-standard-4', autoscaling 5-15 nodes per zone.

```
gcloud dataproc clusters gke create my-cluster --region='us-central1' --gke-cluster='projects/my-project/locations/us-central1/clusters/my-gke-cluster' --spark-engine-version=dataproc-1.5 --pools='name=dp-default,roles=default,machineType=e2-standard-4,min=5,max=15'
```

Create a Dataproc on GKE cluster in us-central1 with two distinct node pools.

```
gcloud dataproc clusters gke create my-cluster --region='us-central1' --gke-cluster='my-gke-cluster' --spark-engine-version='dataproc-2.0' --pools='name=dp-default,roles=default,machineType=e2-standard-4' --pools='name=workers,roles=spark-drivers;spark-executors,machineType=n2-standard-8
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - The name of the cluster to create. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Dataproc region for the cluster. Each Dataproc region constitutes an independent
resource namespace constrained to deploying instances into Compute Engine zones
inside the region. Overrides the default `dataproc/region` property
value for this command invocation.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**REQUIRED FLAGS**

: **--spark-engine-version**:
The version of the Spark engine to run on this cluster.

**Gke cluster resource - The GKE cluster to install the Dataproc cluster on. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--gke-cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--gke-cluster**:
ID of the gke-cluster or fully qualified identifier for the gke-cluster.
To set the `gke-cluster` attribute:

- provide the argument `--gke-cluster` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--gke-cluster-location**:
GKE region for the gke-cluster.
To set the `gke-cluster-location` attribute:

- provide the argument `--gke-cluster` on the command line with a fully
specified name;
- provide the argument `--gke-cluster-location` on the command line;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--namespace**:
The name of the Kubernetes namespace to deploy Dataproc system components in.
This namespace does not need to exist.

**--pools**:
Each `--pools` flag represents a GKE node pool associated with the
virtual cluster. It is comprised of a CSV in the form
`KEY=VALUE[;VALUE]`, where certain keys may have multiple values.
The following KEYs must be specified:

```
-----------------------------------------------------------------------------------------------------------
KEY    Type             Example                  Description
------ ---------------- ------------------------ ----------------------------------------------------------
name   string           `my-node-pool`          Name of the node pool.
```

```
roles  repeated string  `default;spark-driver`  Roles that this node pool should perform. Valid values are
                                                 `default`, `controller`, `spark-driver`, `spark-executor`.
-----------------------------------------------------------------------------------------------------------
```

The following KEYs may be specified:

```
----------------------------------------------------------------------------------------------------------------------------------------------------------------
KEY                Type             Example                                       Description
--------------- ---------------- --------------------------------------------- ---------------------------------------------------------------------------------
machineType        string           `n1-standard-8`                               Compute Engine machine type to use.
```

```
preemptible        boolean          `false`                                       If true, then this node pool uses preemptible VMs.
                                                                                  This cannot be true on the node pool with the `controllers` role
                                                                                  (or `default` role if `controllers` role is not specified).
```

```
localSsdCount      int              `2`                                           The number of local SSDs to attach to each node.
```

```
accelerator        repeated string  `nvidia-tesla-a100=1`                         Accelerators to attach to each node. In the format NAME=COUNT.
```

```
minCpuPlatform     string           `Intel Skylake`                               Minimum CPU platform for each node.
```

```
bootDiskKmsKey     string           `projects/project-id/locations/us-central1    The Customer Managed Encryption Key (CMEK) used to encrypt
                                    /keyRings/keyRing-name/cryptoKeys/key-name`   the boot disk attached to each node in the node pool.
```

```
locations          repeated string  `us-west1-a;us-west1-c`                       Zones within the location of the GKE cluster.
                                                                                  All `--pools` flags for a Dataproc cluster must have identical locations.
```

```
min                int              `0`                                           Minimum number of nodes per zone that this node pool can scale down to.
```

```
max                int              `10`                                          Maximum number of nodes per zone that this node pool can scale up to.
----------------------------------------------------------------------------------------------------------------------------------------------------------------
```

**--properties**:
Specifies configuration properties for installed packages, such as Spark.
Properties are mapped to configuration files by specifying a prefix, such as
"core:io.serializations".

**--setup-workload-identity**:
Sets up the GKE Workload Identity for your Dataproc on GKE cluster. Note that
running this requires elevated permissions as it will manipulate IAM policies on
the Google Service Accounts that will be used by your Dataproc on GKE cluster.

**--staging-bucket**:
The Cloud Storage bucket to use to stage job dependencies, miscellaneous config
files, and job driver console output when using this cluster.

**History server cluster resource - A Dataproc Cluster created as a History
Server, see [https://cloud.google.com/dataproc/docs/concepts/jobs/history-server](https://cloud.google.com/dataproc/docs/concepts/jobs/history-server)
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--history-server-cluster` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--history-server-cluster**:
ID of the history-server-cluster or fully qualified identifier for the
history-server-cluster.
To set the `history-server-cluster` attribute:

- provide the argument `--history-server-cluster` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--history-server-cluster-region**:
Compute Engine region for the history-server-cluster. It must be the same region
as the Dataproc cluster that is being created.
To set the `history-server-cluster-region` attribute:

- provide the argument `--history-server-cluster` on the command line
with a fully specified name;
- provide the argument `--history-server-cluster-region` on the command
line;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**Metastore service resource - Dataproc Metastore Service to be used as an
external metastore. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--metastore-service` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--metastore-service**:
ID of the metastore-service or fully qualified identifier for the
metastore-service.
To set the `metastore-service` attribute:

- provide the argument `--metastore-service` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--metastore-service-location**:
Dataproc Metastore location for the metastore-service.
To set the `metastore-service-location` attribute:

- provide the argument `--metastore-service` on the command line with a
fully specified name;
- provide the argument `--metastore-service-location` on the command
line;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

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
gcloud alpha dataproc clusters gke create
```

```
gcloud beta dataproc clusters gke create
```