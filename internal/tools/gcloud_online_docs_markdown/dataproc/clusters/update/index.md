# gcloud dataproc clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update)*

**NAME**

: **gcloud dataproc clusters update - update labels and/or the number of worker nodes in a cluster**

**SYNOPSIS**

: **`gcloud dataproc clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--async)`] [`[--graceful-decommission-timeout](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--graceful-decommission-timeout)`=`GRACEFUL_DECOMMISSION_TIMEOUT`] [`[--min-secondary-worker-fraction](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--min-secondary-worker-fraction)`=`MIN_SECONDARY_WORKER_FRACTION`] [`[--num-secondary-workers](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--num-secondary-workers)`=`NUM_SECONDARY_WORKERS`] [`[--num-workers](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--num-workers)`=`NUM_WORKERS`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--autoscaling-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--autoscaling-policy)`=`AUTOSCALING_POLICY`     | `[--disable-autoscaling](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--disable-autoscaling)`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--remove-labels)`=[`KEY`,…]] [`[--delete-expiration-time](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--delete-expiration-time)`=`DELETE_EXPIRATION_TIME`     | `[--delete-max-age](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--delete-max-age)`=`DELETE_MAX_AGE`     | `[--no-delete-max-age](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--delete-max-age)`     | `[--expiration-time](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--expiration-time)`=`EXPIRATION_TIME`     | `[--max-age](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--max-age)`=`MAX_AGE`     | `[--no-max-age](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--max-age)`] [`[--delete-max-idle](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--delete-max-idle)`=`DELETE_MAX_IDLE`     | `[--no-delete-max-idle](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--delete-max-idle)`     | `[--max-idle](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--max-idle)`=`MAX_IDLE`     | `[--no-max-idle](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--max-idle)`] [`[--stop-expiration-time](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--stop-expiration-time)`=`STOP_EXPIRATION_TIME`     | `[--stop-max-age](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--stop-max-age)`=`STOP_MAX_AGE`     | `[--no-stop-max-age](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--stop-max-age)`] [`[--stop-max-idle](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--stop-max-idle)`=`STOP_MAX_IDLE`     | `[--no-stop-max-idle](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#--stop-max-idle)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the number of worker nodes and/or the labels in a cluster.

**EXAMPLES**

: To resize a cluster, run:

```
gcloud dataproc clusters update my-cluster --region=us-central1 --num-workers=5
```

To change the number preemptible workers in a cluster, run:

```
gcloud dataproc clusters update my-cluster --region=us-central1 --num-preemptible-workers=5
```

To add the label 'customer=acme' to a cluster, run:

```
gcloud dataproc clusters update my-cluster --region=us-central1 --update-labels=customer=acme
```

To update the label 'customer=ackme' to 'customer=acme', run:

```
gcloud dataproc clusters update my-cluster --region=us-central1 --update-labels=customer=acme
```

To remove the label whose key is 'customer', run:

```
gcloud dataproc clusters update my-cluster --region=us-central1 --remove-labels=customer
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - The name of the cluster to update. The arguments in this
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--graceful-decommission-timeout**:
The graceful decommission timeout for decommissioning Node Managers in the
cluster, used when removing nodes. Graceful decommissioning allows removing
nodes from the cluster without interrupting jobs in progress. Timeout specifies
how long to wait for jobs in progress to finish before forcefully removing nodes
(and potentially interrupting jobs). Timeout defaults to 0 if not set (for
forceful decommission), and the maximum allowed timeout is 1 day. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--min-secondary-worker-fraction**:
Minimum fraction of new secondary worker nodes added in a scale up update
operation, required to update the cluster. If it is not met, cluster updation
will rollback the addition of secondary workers. Must be a decimal value between
0 and 1. Defaults to 0.0001.

**--num-secondary-workers**:
The new number of secondary worker nodes in the cluster.

**--num-workers**:
The new number of worker nodes in the cluster.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**At most one of these can be specified:

**Autoscaling policy resource - The autoscaling policy to use. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--autoscaling-policy` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--autoscaling-policy` on the command line with
a fully specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.

**--autoscaling-policy**:
ID of the autoscaling policy or fully qualified identifier for the autoscaling
policy.
To set the `autoscaling_policy` attribute:

- provide the argument `--autoscaling-policy` on the command line.**

**--disable-autoscaling**:
Disable autoscaling, if it is enabled. This is an alias for passing the empty
string to --autoscaling-policy'.**

**--clear-labels**

**--delete-expiration-time**

**--delete-max-idle**

**--stop-expiration-time**

**--stop-max-idle**

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
gcloud alpha dataproc clusters update
```

```
gcloud beta dataproc clusters update
```