# gcloud alloydb backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create)*

**NAME**

: **gcloud alloydb backups create - creates a new AlloyDB backup within a given project**

**SYNOPSIS**

: **`gcloud alloydb backups create` `[BACKUP](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#BACKUP)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--region)`=`REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--async)`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--tags)`=[`KEY`=`VALUE`,…]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new AlloyDB backup within a given project.

**EXAMPLES**

: To create a new backup, run:

```
gcloud alloydb backups create my-backup --cluster=my-cluster --region=us-central1
```

To create a new cross-region backup, run:

```
gcloud alloydb backups create projects/my-project/locations/us-west1/backups/my-backup --cluster=my-cluster --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`BACKUP`**:
The AlloyDB backup to create. This must either be the backup ID (myBackup) or
the full backup path
(projects/myProject/locations/us-central1/backups/myBackup). In the first case,
the project and location are assumed to be the same as the cluster being backed
up. The second form can be used to create cross-region and cross-project
backups.

**REQUIRED FLAGS**

: **--cluster**:
AlloyDB cluster ID

**--region**:
The region of the cluster to backup.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--tags**:
List of tags KEY=VALUE pairs to bind. Each item must be expressed as
`<tag-key-namespaced-name>=<tag-value-short-name>`.
Example: `123/environment=production,123/costCenter=marketing`

**--kms-key**

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
gcloud alpha alloydb backups create
```

```
gcloud beta alloydb backups create
```