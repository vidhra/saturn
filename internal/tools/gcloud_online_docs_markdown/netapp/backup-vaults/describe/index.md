# gcloud netapp backup-vaults describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/describe](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/describe)*

**NAME**

: **gcloud netapp backup-vaults describe - show metadata for a Cloud NetApp Volumes Backup Vault**

**SYNOPSIS**

: **`gcloud netapp backup-vaults describe` (`[BACKUP_VAULT](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/describe#BACKUP_VAULT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Backup Vault.

**EXAMPLES**

: The following command gets metadata using describe for a Backup Vault instance
named BACKUP_VAULT in the default netapp/location:

```
gcloud netapp backup-vaults describe BACKUP_VAULT
```

To get metadata on a Backup Vault named BACKUP_VAULT in a specified location,
run:

```
gcloud netapp backup-vaults describe BACKUP_VAULT --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Backup vault resource - The Backup Vault to describe. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backup_vault` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP_VAULT`**:
ID of the backup_vault or fully qualified identifier for the backup_vault.
To set the `backup_vault` attribute:

- provide the argument `backup_vault` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the backup_vault.
To set the `location` attribute:

- provide the argument `backup_vault` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

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

: This variant is also available:

```
gcloud beta netapp backup-vaults describe
```