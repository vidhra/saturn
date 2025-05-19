# gcloud alpha backup-dr data-sources describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/data-sources/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/data-sources/describe)*

**NAME**

: **gcloud alpha backup-dr data-sources describe - show details of the data source**

**SYNOPSIS**

: **`gcloud alpha backup-dr data-sources describe` (`[DATA_SOURCE](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/data-sources/describe#DATA_SOURCE)` : `[--backup-vault](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/data-sources/describe#--backup-vault)`=`BACKUP_VAULT` `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/data-sources/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/data-sources/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Show all configuration data associated with the specified
data source.

**EXAMPLES**

: To view details for data source 'DATA_SOURCE', run:

```
gcloud alpha backup-dr data-sources describe DATA_SOURCE
```

**POSITIONAL ARGUMENTS**

: **Data source resource - Name of the data source to describe. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `data_source` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATA_SOURCE`**:
ID of the data_source or fully qualified identifier for the data_source.
To set the `data_source` attribute:

- provide the argument `data_source` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--backup-vault**:
The ID of the Backup Vault.
To set the `backup-vault` attribute:

- provide the argument `data_source` on the command line with a fully
specified name;
- provide the argument `--backup-vault` on the command line.

**--location**:
Location ID of the resource.
To set the `location` attribute:

- provide the argument `data_source` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `backupdr/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/backup-disaster-recovery](https://cloud.google.com/backup-disaster-recovery)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud backup-dr data-sources describe
```