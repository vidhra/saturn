# gcloud filestore instances restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore)*

**NAME**

: **gcloud filestore instances restore - restore a Filestore instance from a backup**

**SYNOPSIS**

: **`gcloud filestore instances restore` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore#INSTANCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore#--zone)`=`ZONE`) `[--file-share](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore#--file-share)`=`FILE_SHARE` `[--source-backup](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore#--source-backup)`=`SOURCE_BACKUP` `[--source-backup-region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore#--source-backup-region)`=`SOURCE_BACKUP_REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restore an existing Filestore instance from an existing backup.

**EXAMPLES**

: The following command restores an instance named 'my-instance' with a fileshare
named 'vol1' in the zone europe-west3-a from a backup named 'my-backup' in the
region europe-west3.

```
gcloud filestore instances restore my-instance --zone=europe-west3-a --file-share=vol1 --source-backup=my-backup --source-backup-region=europe-west3
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Filestore instance to
restore. The arguments in this group can be used to specify the attributes of
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

**--zone**:
The zone of the Filestore instance.
To set the `zone` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- set the property `filestore/zone`.**

**REQUIRED FLAGS**

: **--file-share**:
File share to restore from the backup.

**--source-backup**:
Name of the Filestore backup to restore from.

**--source-backup-region**:
Region of the Filestore backup to restore from.

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

: These variants are also available:

```
gcloud alpha filestore instances restore
```

```
gcloud beta filestore instances restore
```