# gcloud filestore instances snapshots describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe)*

**NAME**

: **gcloud filestore instances snapshots describe - display information about a Filestore snapshot**

**SYNOPSIS**

: **`gcloud filestore instances snapshots describe` `[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe#SNAPSHOT)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe#--instance)`=`INSTANCE` (`[--instance-location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe#--instance-location)`=`INSTANCE_LOCATION`     | `[--instance-region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe#--instance-region)`=`INSTANCE_REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Displays information about a Filestore snapshot given a valid snapshot name, as
well as instance name and instance region.
This command can fail for the following reasons:

- The snapshot or instance specified does not exist.
- The active account does not have permission to access the given snapshot.

**EXAMPLES**

: To display all information associated with a snapshot of the name
``my-snapshot`` for the instance
``my-instance`` from
``us-central1``, run:

```
gcloud filestore instances snapshots describe my-snapshot --instance=my-instance --instance-region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`SNAPSHOT`**:
Name of the Filestore snapshot to display information about.

**REQUIRED FLAGS**

: **--instance**:
Name of the Filestore instance the snapshot belongs to.

**--instance-location**

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
gcloud beta filestore instances snapshots describe
```