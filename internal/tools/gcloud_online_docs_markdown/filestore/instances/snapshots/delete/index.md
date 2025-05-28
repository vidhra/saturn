# gcloud filestore instances snapshots delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete)*

**NAME**

: **gcloud filestore instances snapshots delete - delete a Filestore snapshot**

**SYNOPSIS**

: **`gcloud filestore instances snapshots delete` `[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete#SNAPSHOT)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete#--instance)`=`INSTANCE` (`[--instance-location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete#--instance-location)`=`INSTANCE_LOCATION`     | `[--instance-region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete#--instance-region)`=`INSTANCE_REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Filestore snapshot.
This command can fail for the following reasons:

- The snapshot or instance specified does not exist.
- The active account does not have permission to delete the given snapshot.

**EXAMPLES**

: To delete a snapshot named ``my-snapshot`` for
the instance ``my-instance`` from
``us-central1``, run:

```
gcloud filestore instances snapshots delete my-snapshot --instance=my-instance --instance-region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`SNAPSHOT`**:
Name of the Filestore snapshot to be deleted.

**REQUIRED FLAGS**

: **--instance**:
Name of the Filestore instance the snapshot belongs to.

**--instance-location**

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

: This command uses the `file/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/filestore/](https://cloud.google.com/filestore/)

**NOTES**

: This variant is also available:

```
gcloud beta filestore instances snapshots delete
```