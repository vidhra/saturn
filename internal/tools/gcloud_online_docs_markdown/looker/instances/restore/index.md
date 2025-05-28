# gcloud looker instances restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore)*

**NAME**

: **gcloud looker instances restore - restore a Looker instance from a backup**

**SYNOPSIS**

: **`gcloud looker instances restore` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore#--region)`=`REGION`) `[--backup](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore#--backup)`=`BACKUP` [`[--async](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restore a Looker instance from a backup.
The Looker instance in which the backup is derived from will be restored to that
specific backup.
This command can fail for the following reasons:

- The instance specified does not exist.
- The backup specified does not exist.
- The active account does not have permission to access the given instance and
backups.

**EXAMPLES**

: To restore a backup with id of `7e504e66-c389-4d8d-bca7-f710c6d96567`
that belongs to an instance named `my-looker-instance`, in the region
`us-central1`, run:

```
gcloud looker instances restore my-looker-instance --backup="7e504e66-c389-4d8d-bca7-f710c6d96567" --region="us-central1" --async
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Looker instance you
want to describe. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
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

**--region**:
The name of the Looker region of the instance. Overrides the default
looker/region property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `looker/region`.**

**REQUIRED FLAGS**

: **--backup**:
The ID of the backup instance in the format
projects/{project}/locations/{location}/instances/{instance}/backups/{backup}

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

: This command uses the `looker/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/looker/docs/reference/rest/](https://cloud.google.com/looker/docs/reference/rest/)

**NOTES**

: This variant is also available:

```
gcloud alpha looker instances restore
```