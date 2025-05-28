# gcloud memorystore instances backup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup)*

**NAME**

: **gcloud memorystore instances backup - backup instances**

**SYNOPSIS**

: **`gcloud memorystore instances backup` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup#--async)`] [`[--backup-id](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup#--backup-id)`=`BACKUP_ID`] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup#--ttl)`=`TTL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: backup instances

**EXAMPLES**

: To backup all instances, run:

```
gcloud memorystore instances backup
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Instance resource name using the form:
`projects/{project_id}/locations/{location_id}/instances/{instance_id}`
where `location_id` refers to a Google Cloud region. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the instance resource.
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--backup-id**:
The id of the backup to be created. If not specified, the default value
([YYYYMMDDHHMMSS]`[Shortened Instance UID] is used.`

**--ttl**:
TTL for the backup to expire. Value range is 1 day to 100 years. If not
specified, the default value is 100 years.

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

: This command uses the `memorystore/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memorystore instances backup
```

```
gcloud beta memorystore instances backup
```