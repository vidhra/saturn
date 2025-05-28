# gcloud filestore backups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/backups](https://cloud.google.com/sdk/gcloud/reference/filestore/backups)*

**NAME**

: **gcloud filestore backups - create and manage Filestore backups**

**SYNOPSIS**

: **`gcloud filestore backups` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/filestore/backups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/backups#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a backup with the name 'my-backup', run:

```
gcloud filestore backups create my-backup --region=Region
```

To delete a backup with the name 'my-backup', run:

```
gcloud filestore backups delete my-backup --region=Region
```

To display the details for an backup with the name 'my-backup', run:

```
gcloud filestore backups describe my-backup --region=Region
```

To list all the backups, run:

```
gcloud filestore backups list [--region=Region]
```

To set the label 'env' to 'prod' for an backup with the name 'my-backup', run:

```
gcloud filestore backups my-backup --update-labels=env=prod
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/create)`**:
Create a Filestore backup.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/delete)`**:
Delete a Filestore backup.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/describe)`**:
Describe a Filestore backup.

**`[list](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/list)`**:
List Filestore backups.

**`[update](https://cloud.google.com/sdk/gcloud/reference/filestore/backups/update)`**:
Update a Filestore backup.

**NOTES**

: These variants are also available:

```
gcloud alpha filestore backups
```

```
gcloud beta filestore backups
```