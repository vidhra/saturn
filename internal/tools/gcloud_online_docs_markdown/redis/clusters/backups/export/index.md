# gcloud redis clusters backups export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export)*

**NAME**

: **gcloud redis clusters backups export - export a Redis cluster backup to a Google Cloud Storage bucket**

**SYNOPSIS**

: **`gcloud redis clusters backups export` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export#BACKUP)` : `[--backup-collection](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export#--backup-collection)`=`BACKUP_COLLECTION` `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export#--region)`=`REGION`) `[--gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export#--gcs-bucket)`=`GCS_BUCKET` [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command exports a Redis cluster backup to a Google Cloud Storage bucket. A
new folder will be created in the bucket with the backup name. And the backup
files will be stored in the folder.

**EXAMPLES**

: To export a backup with name `my-backup` under backup collection
`my-collection` in `us-central` region to
`my-bucket` Google Cloud Storage bucket, run:

```
gcloud redis clusters backups export my-backup --backup-collection=my-collection --region=us-central1 --bucket-name=my-bucket
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Arguments and flags that specify the Redis backup you want to
export. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP`**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `backup` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--backup-collection**:
The name of the Redis cluster backup collection.
To set the `backup-collection` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--backup-collection` on the command line.

**--region**:
The name of the Redis region of the backup. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**REQUIRED FLAGS**

: **--gcs-bucket**:
The name of the Google Cloud Storage bucket to export the backup to.

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

: This command uses the `redis/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/memorystore/docs/redis/](https://cloud.google.com/memorystore/docs/redis/)

**NOTES**

: These variants are also available:

```
gcloud alpha redis clusters backups export
```

```
gcloud beta redis clusters backups export
```