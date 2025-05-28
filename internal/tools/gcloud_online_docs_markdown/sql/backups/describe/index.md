# gcloud sql backups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe)*

**NAME**

: **gcloud sql backups describe - retrieves information about a backup**

**SYNOPSIS**

: **`gcloud sql backups describe` `[ID](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe#ID)` [`[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe#INSTANCE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieves information about a backup.

**POSITIONAL ARGUMENTS**

: **`ID`**:
The ID of the backup run. To find the ID, run the following command: $ [gcloud sql backups list](https://cloud.google.com/sdk/gcloud/reference/sql/backups/list) -i
{instance}.Or, the NAME of the backup. To find the NAME, run the following
command: $ [gcloud sql backups
list](https://cloud.google.com/sdk/gcloud/reference/sql/backups/list) --filter=instance:{instance}

**FLAGS**

: **--instance**:
Cloud SQL instance ID.

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
gcloud alpha sql backups describe
```

```
gcloud beta sql backups describe
```