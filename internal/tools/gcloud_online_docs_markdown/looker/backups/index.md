# gcloud looker backups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/backups](https://cloud.google.com/sdk/gcloud/reference/looker/backups)*

**NAME**

: **gcloud looker backups - manage Looker instances**

**SYNOPSIS**

: **`gcloud looker backups` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/looker/backups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/backups#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a backup of an instance with the name `my-looker-instance`
and in the region `us-central1`, run:

```
gcloud looker backups create --instance='my-looker-instance --region=us-central1'
```

To delete a backup with the name `looker-backup` that is a backup of
an instance with the name `my-looker-instance` and in the region
`us-central1`, run:

```
gcloud looker backups delete looker-backup --instance=my-looker-instance --region=us-central1
```

To display the details for a backup with the name `looker-backup`
that is a backup of an instance with the name `my-looker-instance`
and in the region `us-central1`, run:

```
gcloud looker backups describe looker-backup --instance=my-looker-instance --region=us-central1
```

To list all backups of an instance with the name `my-looker-instance`
and in the region `us-central1`, run:

```
gcloud looker backups list --instance=my-looker-instance --region=us-central1
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/looker/backups/create)`**:
Create a backup of a Looker instance.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete)`**:
Delete a backup of a Looker instance.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/looker/backups/describe)`**:
Show metadata of a backup for a Looker instance.

**`[list](https://cloud.google.com/sdk/gcloud/reference/looker/backups/list)`**:
List backups of a Looker instance.

**NOTES**

: This variant is also available:

```
gcloud alpha looker backups
```