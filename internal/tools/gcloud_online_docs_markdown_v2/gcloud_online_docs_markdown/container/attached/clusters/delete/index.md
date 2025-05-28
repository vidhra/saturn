# gcloud container attached clusters delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete)*

**NAME**

: **gcloud container attached clusters delete - delete a registered AttachedCluster resource**

**SYNOPSIS**

: **`gcloud container attached clusters delete` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete#--location)`=`LOCATION`) [`[--allow-missing](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete#--allow-missing)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete#--async)`] [`[--ignore-errors](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete#--ignore-errors)`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a registered AttachedCluster resource.

**EXAMPLES**

: To delete an AttachedCluster resource named
``my-cluster`` managed in location
``us-west1``, run:

```
gcloud container attached clusters delete my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to delete. The arguments in this group can be used to
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
- set the property `container_attached/location`.**

**FLAGS**

: **--allow-missing**:
Allow idempotent deletion of cluster. The request will still succeed in case the
cluster does not exist.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--ignore-errors**:
Force delete an Attached cluster. Deletion of the Attached cluster will succeed
even if errors occur during deleting in-cluster resources. Using this parameter
may result in orphaned resources in the cluster.

**--validate-only**:
Validate the cluster to delete, but don't actually perform it.

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

: This variant is also available:

```
gcloud alpha container attached clusters delete
```