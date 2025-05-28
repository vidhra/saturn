# gcloud redis clusters detach-secondaries  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries)*

**NAME**

: **gcloud redis clusters detach-secondaries - detach one or more secondary clusters from the primary cluster**

**SYNOPSIS**

: **`gcloud redis clusters detach-secondaries` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries#--region)`=`REGION`) `[--clusters-to-detach](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries#--clusters-to-detach)`=`CLUSTERS_TO_DETACH` [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Detach one or more secondary clusters from the primary cluster.
After detachment, the secondary clusters become independent clusters, i.e. they
stop replicating from the primary cluster and will now accept both read and
write requests.
This command is only supported on primary clusters.

**EXAMPLES**

: To detach the secondary clusters `my-secondary-cluster1` and
`my-secondary-cluster2` from the primary cluster
`my-primary-cluster`, run:

```
gcloud redis clusters detach-secondaries my-primary-cluster --region=us-central1 --clusters-to-detach=projects/my-project/locations/us-east1/clusters/my-secondary-cluster1,projects/my-project/locations/asia-east1/clusters/my-secondary-cluster2
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Arguments and flags that specify the Memorystore Redis
cluster you want to update. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
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
The name of the Redis region of the cluster. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**REQUIRED FLAGS**

: **--clusters-to-detach**:
Comma separated list of secondary clusters to detach from the primary cluster.
Each element in the list should be in the format:
`projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID`.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**API REFERENCE**

: This command uses the `redis/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/memorystore/docs/redis/](https://cloud.google.com/memorystore/docs/redis/)

**NOTES**

: These variants are also available:

```
gcloud alpha redis clusters detach-secondaries
```

```
gcloud beta redis clusters detach-secondaries
```