# gcloud filestore backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create)*

**NAME**

: **gcloud filestore backups create - create a Filestore backup**

**SYNOPSIS**

: **`gcloud filestore backups create` `[BACKUP](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#BACKUP)` `[--file-share](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--file-share)`=`FILE_SHARE` `[--instance](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--instance)`=`INSTANCE` `[--region](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--region)`=`REGION` (`[--instance-location](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--instance-location)`=`INSTANCE_LOCATION`     | `[--instance-zone](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--instance-zone)`=`INSTANCE_ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--description)`=`DESCRIPTION`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#--tags)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Filestore backup of an instance file share.
This command can fail for the following reasons:

- A backup with the same name already exists.
- The active account does not have permission to create backups.

**EXAMPLES**

: To create a backup with the name 'my-backup' and description 'My backup
description' in a particular region like 'us-central1' from an instance called
'my-instance' in 'us-central1-c' and the source file share called 'my-fs', run:

```
gcloud filestore backups create my-backup --instance=my-instance --file-share=my-fs --instance-zone=us-central1-c --region=us-central1 --description="My backup description"
```

**POSITIONAL ARGUMENTS**

: **`BACKUP`**:
Arguments and flags that specify the Filestore backup you want to create.

**REQUIRED FLAGS**

: **--file-share**:
File share name on the Filestore instance to backup.

**--instance**:
Share name of the Filestore instance you want to backup.

**--region**:
Region (e.g. us-central1) for the backup.

**--instance-location**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description for the backup. Limit: 2048 characters.

**--kms-key**:
CMEK for backup in the form of
`projects/{project}/locations/{location}/keyRings/{key-ring}/cryptoKeys/{crypto-key}`

**--labels**:
List of label KEY=VALUE pairs to add.

**--tags**:
List of tag KEY=VALUE pairs to add.

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
gcloud alpha filestore backups create
```

```
gcloud beta filestore backups create
```