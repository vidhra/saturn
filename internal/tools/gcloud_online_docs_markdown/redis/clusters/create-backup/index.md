# gcloud redis clusters create-backup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup)*

**NAME**

: **gcloud redis clusters create-backup - create a backup of a Redis cluster**

**SYNOPSIS**

: **`gcloud redis clusters create-backup` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup#--async)`] [`[--backup-id](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup#--backup-id)`=`BACKUP_ID`] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup#--ttl)`=`TTL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a backup of a Redis cluster. The backup can be used to seed a new cluster
or exported to a Google Cloud Storage bucket.
The created backup will be added into the backup collection associated with the
cluster. Describe the cluster to get the backup collection name.

**POSITIONAL ARGUMENTS**

: **Cluster resource - Arguments and flags that specify the Memorystore Redis
cluster to create a backup for. The arguments in this group can be used to
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

**--region**:
The name of the Redis region of the cluster. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--backup-id**:
The ID of the backup.

**--ttl**:
The time to live for the backup. The backup will be deleted automatically after
the TTL is reached. For example, "10d" for 10 days. The minimum value is 1 day.
If not specified, the default value is 100 years.

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
gcloud alpha redis clusters create-backup
```

```
gcloud beta redis clusters create-backup
```