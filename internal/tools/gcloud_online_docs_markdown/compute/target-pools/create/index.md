# gcloud compute target-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create)*

**NAME**

: **gcloud compute target-pools create - define a load-balanced pool of virtual machine instances**

**SYNOPSIS**

: **`gcloud compute target-pools create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#NAME)` [`[--backup-pool](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#--backup-pool)`=`BACKUP_POOL`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#--description)`=`DESCRIPTION`] [`[--failover-ratio](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#--failover-ratio)`=`FAILOVER_RATIO`] [`[--health-check](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#--health-check)`=`HEALTH_CHECK`] [`[--http-health-check](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#--http-health-check)`=`HTTP_HEALTH_CHECK`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#--region)`=`REGION`] [`[--session-affinity](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#--session-affinity)`=`SESSION_AFFINITY`; default="NONE"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-pools create` is used to create a target pool.
A target pool resource defines a group of instances that can receive incoming
traffic from forwarding rules. When a forwarding rule directs traffic to a
target pool, Compute Engine picks an instance from the target pool based on a
hash of the source and destination IP addresses and ports. For more information
on load balancing, see [https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/](https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/)
To add instances to a target pool, use 'gcloud compute target-pools
add-instances'.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the target pool.

**FLAGS**

: **--backup-pool**:
Together with ``--failover-ratio``, this flag
defines the fallback behavior of the target pool (primary pool) to be created by
this command. If the ratio of the healthy instances in the primary pool is at or
below the specified ``--failover-ratio value``,
then traffic arriving at the load-balanced IP address will be directed to the
backup pool. If this flag is provided, then
``--failover-ratio`` is required.

**--description**:
An optional description of this target pool.

**--failover-ratio**:
Together with ``--backup-pool``, defines the
fallback behavior of the target pool (primary pool) to be created by this
command. If the ratio of the healthy instances in the primary pool is at or
below this number, traffic arriving at the load-balanced IP address will be
directed to the backup pool. For example, if 0.4 is chosen as the failover
ratio, then traffic will fail over to the backup pool if more than 40% of the
instances become unhealthy. If not set, the traffic will be directed the
instances in this pool in the ``force`` mode,
where traffic will be spread to the healthy instances with the best effort, or
to all instances when no instance is healthy. If this flag is provided, then
``--backup-pool`` is required.

**--health-check**:
DEPRECATED, use --http-health-check. Specifies an HTTP health check resource to
use to determine the health of instances in this pool. If no health check is
specified, traffic will be sent to all instances in this target pool as if the
instances were healthy, but the health status of this pool will appear as
unhealthy as a warning that this target pool does not have a health check.

**--http-health-check**:
Specifies an HTTP health check resource to use to determine the health of
instances in this pool. If no health check is specified, traffic will be sent to
all instances in this target pool as if the instances were healthy, but the
health status of this pool will appear as unhealthy as a warning that this
target pool does not have a health check.

**--region**:
Region of the target pool to create. If not specified, you might be prompted to
select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--session-affinity**:
The type of session affinity to use. Supports both TCP and UDP.
`SESSION_AFFINITY` must be one of:

**`CLIENT_IP`**:
Route requests to instances based on the hash of the client's IP address.

**`CLIENT_IP_PROTO`**:
Connections from the same client IP with the same IP protocol will go to the
same VM in the pool while that VM remains healthy.

**`NONE`**:
Session affinity is disabled.

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
gcloud alpha compute target-pools create
```

```
gcloud beta compute target-pools create
```