# gcloud filestore instances snapshots create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create)*

**NAME**

: **gcloud filestore instances snapshots create - create a Filestore snapshot**

**SYNOPSIS**

: **`gcloud filestore instances snapshots create` `[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#SNAPSHOT)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#--instance)`=`INSTANCE` (`[--instance-location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#--instance-location)`=`INSTANCE_LOCATION`     | `[--instance-region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#--instance-region)`=`INSTANCE_REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Filestore snapshot of an instance.
This command can fail for the following reasons:

- A snapshot with the same name already exists.
- The active account does not have permission to create snapshots.
- Maximum number of snapshots for the instance has been reached.
- The service tier of the instance does not support snapshots.

**EXAMPLES**

: To create a snapshot with the name
``my-snapshot`` for an instance named
``my-instance`` that's located in
``us-central1``, run:

```
gcloud filestore instances snapshots create my-snapshot --instance=my-instance --instance-region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`SNAPSHOT`**:
Name of the Filestore snapshot to be created.

**REQUIRED FLAGS**

: **--instance**:
Name of the Filestore instance that you want to create a snapshot of.

**--instance-location**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the snapshot. Limit: 2048 characters.

**--labels**:
List of label KEY=VALUE pairs to add.

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
gcloud beta filestore instances snapshots create
```