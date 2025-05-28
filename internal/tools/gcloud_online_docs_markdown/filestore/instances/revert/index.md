# gcloud filestore instances revert  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/revert](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/revert)*

**NAME**

: **gcloud filestore instances revert - revert a Filestore instance**

**SYNOPSIS**

: **`gcloud filestore instances revert` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/revert#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/revert#--location)`=`LOCATION`) `[--target-snapshot](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/revert#--target-snapshot)`=`TARGET_SNAPSHOT` [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/revert#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/revert#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Revert a Filestore instance to the target snapshot.
This command can fail for the following reasons:

- The target snapshot does not exist.
- The active account does not have permission to revert the instance.
- The service tier of the instance does not support the operation.

**EXAMPLES**

: To revert an instance with the name
``my-instance`` that's located in
``us-central1`` to the target snapshot named
``my-snapshot`` , run:

```
gcloud filestore instances revert my-instance --target-snapshot=my-snapshot --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Filestore instance to
revert. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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
The location of the Filestore instance.
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `filestore/location`.**

**REQUIRED FLAGS**

: **--target-snapshot**:
Name of the Filestore snapshot to revert to.

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
gcloud beta filestore instances revert
```