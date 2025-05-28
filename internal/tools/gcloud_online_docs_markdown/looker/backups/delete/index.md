# gcloud looker backups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete](https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete)*

**NAME**

: **gcloud looker backups delete - delete a backup of a Looker instance**

**SYNOPSIS**

: **`gcloud looker backups delete` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete#BACKUP)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete#--instance)`=`INSTANCE` `[--region](https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/backups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a backup of a Looker instance.
This command can fail for the following reasons:

- The instance specified does not exist.
- The backup does not exist.
- The active account does not have permission to access the given instance.

**EXAMPLES**

: To delete a backup with ID `c24ad631-ad83-42f0-9f98-41e2b493263e` on
instance with name `my-looker-instance`, run:

```
gcloud looker backups delete c24ad631-ad83-42f0-9f98-41e2b493263e --instance='my-looker-instance'
```

**POSITIONAL ARGUMENTS**

: **Backup resource - The instance of the backup to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**--instance**:
The name of the Looker instance.
To set the `instance` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.

**--region**:
The name of the Looker region of the backup. Overrides the default looker/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `looker/region`.**

**FLAGS**

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
gcloud alpha looker backups delete
```