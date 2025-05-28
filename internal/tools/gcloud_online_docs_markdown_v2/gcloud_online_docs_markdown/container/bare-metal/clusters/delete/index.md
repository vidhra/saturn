# gcloud container bare-metal clusters delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete)*

**NAME**

: **gcloud container bare-metal clusters delete - delete an Anthos cluster on bare metal**

**SYNOPSIS**

: **`gcloud container bare-metal clusters delete` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#--location)`=`LOCATION`) [`[--allow-missing](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#--allow-missing)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#--async)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#--force)`] [`[--ignore-errors](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#--ignore-errors)`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an Anthos cluster on bare metal.

**EXAMPLES**

: To delete a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container bare-metal clusters delete my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to delete The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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

**--location**:
Google Cloud location for the cluster.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_bare_metal/location`.**

**FLAGS**

: **--allow-missing**:
If set, and the Bare Metal cluster is not found, the request will succeed but no
action will be taken.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--force**:
If set, the operation will also apply to the child node pools. This flag is
required if the cluster has any associated node pools.

**--ignore-errors**:
If set, the deletion of a bare metal user cluster resource will succeed even if
errors occur during deletion.

**--validate-only**:
If set, only validate the request, but do not actually perform the operation.

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
gcloud alpha container bare-metal clusters delete
```

```
gcloud beta container bare-metal clusters delete
```