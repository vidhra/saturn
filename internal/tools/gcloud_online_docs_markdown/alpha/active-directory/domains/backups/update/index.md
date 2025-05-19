# gcloud alpha active-directory domains backups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update)*

**NAME**

: **gcloud alpha active-directory domains backups update - update a Managed Microsoft AD domain backup**

**SYNOPSIS**

: **`gcloud alpha active-directory domains backups update` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update#BACKUP)` : `[--domain](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update#--domain)`=`DOMAIN`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Managed Microsoft AD domain backup.

- The specified backup doesn't exist.
- The active account doesn't have permission to access the specified domain.
- The active account doesn't have permission to access the specified domain
backup.

**EXAMPLES**

: To update an AD domain backup `my-backup` under domain
```
`projects/my-proj/locations/global/domains/my-domain.com` with the labels `l1` and `l2`, run:
```

```
gcloud alpha active-directory domains backups update projects/my-proj/locations/global/domains/my-domain.com/backups/my-backup --update-labels=l1=1,l2=2
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Name of the Managed Microsoft AD domain backup you want to
update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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

**--domain**:
The fully-qualified domain name of the Microsoft Active Directory domain.
To set the `domain` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--domain` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

: This command uses the `managedidentities/v1alpha1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud active-directory domains backups update
```

```
gcloud beta active-directory domains backups update
```