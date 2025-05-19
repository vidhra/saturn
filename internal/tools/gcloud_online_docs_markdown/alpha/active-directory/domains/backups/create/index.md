# gcloud alpha active-directory domains backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/create](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/create)*

**NAME**

: **gcloud alpha active-directory domains backups create - create a Managed Microsoft AD domain backup**

**SYNOPSIS**

: **`gcloud alpha active-directory domains backups create` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/create#BACKUP)` : `[--domain](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/create#--domain)`=`DOMAIN`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Managed Microsoft AD domain backup with the
specified name using Google Cloud's Managed Service for Microsoft Active
Directory.
This command can fail for the following reasons:

- The specified domain doesn't exist.
- The specified domain is being created.
- A backup already exists with the same target domain name.
- The active account doesn't have permission to access the specified domain.
- The active account doesn't have permission to create AD domain backups.

**EXAMPLES**

: To create an AD domain backup named `my-backup` under domain
`my-domain.com`, run:

```
gcloud alpha active-directory domains backups create my-backup --domain=my-domain.com --project=my-proj --async
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Name of the Managed Microsoft AD domain backup you want to
create. The arguments in this group can be used to specify the attributes of
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

**--labels**:
List of label KEY=VALUE pairs to add.

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
gcloud active-directory domains backups create
```

```
gcloud beta active-directory domains backups create
```