# gcloud bigtable backups copy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy)*

**NAME**

: **gcloud bigtable backups copy - copy a Cloud Bigtable backup to a new backup**

**SYNOPSIS**

: **`gcloud bigtable backups copy` (`[--destination-backup](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--destination-backup)`=`DESTINATION_BACKUP` : `[--destination-cluster](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--destination-cluster)`=`DESTINATION_CLUSTER` `[--destination-instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--destination-instance)`=`DESTINATION_INSTANCE` `[--destination-project](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--destination-project)`=`DESTINATION_PROJECT`) (`[--expiration-date](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--expiration-date)`=`EXPIRATION_DATE`     | `[--retention-period](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--retention-period)`=`RETENTION_PERIOD`) (`[--source-backup](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--source-backup)`=`SOURCE_BACKUP` : `[--source-cluster](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--source-cluster)`=`SOURCE_CLUSTER` `[--source-instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--source-instance)`=`SOURCE_INSTANCE` `[--source-project](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--source-project)`=`SOURCE_PROJECT`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a copy of a Cloud Bigtable backup.

**EXAMPLES**

: To copy a backup within the same project, run:

```
gcloud bigtable backups copy --source-instance=SOURCE_INSTANCE --source-cluster=SOURCE_CLUSTER --source-backup=SOURCE_BACKUP --destination-instance=DESTINATION_INSTANCE --destination-cluster=DESTINATION_CLUSTER --destination-backup=DESTINATION_BACKUP --expiration-date=2023-09-01T10:49:41Z
```

To copy a backup to a different project, run:

```
gcloud bigtable backups copy --source-backup=projects/SOURCE_PROJECT/instances/SOURCE_INSTANCE/clusters/SOURCE_CLUSTER/backups/SOURCE_BACKUP --destination-backup=projects/DESTINATION_PROJECT/instances/DESTINATION_INSTANCE/clusters/DESTINATION_CLUSTER/backups/DESTINATION_BACKUP --expiration-date=2022-08-01T10:49:41Z
```

To set retention period and run asyncronously, run:

```
gcloud bigtable backups copy --source-backup=projects/SOURCE_PROJECT/instances/SOURCE_INSTANCE/clusters/SOURCE_CLUSTER/backups/SOURCE_BACKUP --destination-backup=projects/DESTINATION_PROJECT/instances/DESTINATION_INSTANCE/clusters/DESTINATION_CLUSTER/backups/DESTINATION_BACKUP --retention-period=2w --async
```

**REQUIRED FLAGS**

: **--destination-backup**

**--expiration-date**

**--source-backup**

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

**NOTES**

: These variants are also available:

```
gcloud alpha bigtable backups copy
```

```
gcloud beta bigtable backups copy
```