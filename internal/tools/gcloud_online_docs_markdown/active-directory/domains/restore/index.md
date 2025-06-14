# gcloud active-directory domains restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/restore](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/restore)*

**NAME**

: **gcloud active-directory domains restore - restore a domain from the specified backup**

**SYNOPSIS**

: **`gcloud active-directory domains restore` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/restore#DOMAIN)` `[--backup](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/restore#--backup)`=`BACKUP` [`[--async](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/restore#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restore a Managed Microsoft AD domain to a previous point in time when the
backup was taken.
This command can fail for the following reasons:

- The specified domain doesn't exist.
- The specified backup doesn't exist.
- The active account doesn't have permission to restore the specified domain.

**EXAMPLES**

: To restore the domain `my-domain.com` from backup
`my-backup`, run:

```
gcloud active-directory domains restore my-domain.com --backup=my-backup --async
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the Managed Microsoft AD domain you want to restore.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `domain` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DOMAIN`**:
ID of the domain or fully qualified identifier for the domain.
To set the `domain` attribute:

- provide the argument `domain` on the command line.**

**REQUIRED FLAGS**

: **--backup**:
Name of the domain backup from which you want to restore the Managed Microsoft
AD domain.

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

: This command uses the `managedidentities/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: These variants are also available:

```
gcloud alpha active-directory domains restore
```

```
gcloud beta active-directory domains restore
```