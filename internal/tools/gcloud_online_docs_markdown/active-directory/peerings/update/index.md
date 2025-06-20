# gcloud active-directory peerings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update](https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update)*

**NAME**

: **gcloud active-directory peerings update - update a Managed Microsoft Active Directory domain peering**

**SYNOPSIS**

: **`gcloud active-directory peerings update` `[PEERING](https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update#PEERING)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/active-directory/peerings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Managed Microsoft Active Directory (AD) domain peering.
This command can fail for the following reasons:

- The active account does not have permission to access the given AD domain.

**EXAMPLES**

: The following command updates an AD domain peering
``my-peering`` with the label
``l1`` and
``l2``

```
gcloud active-directory peerings update my-peering --update-labels=l1=1,l2=2
```

**POSITIONAL ARGUMENTS**

: **Peering resource - Name of the managed Managed Microsoft AD domain you want to
delete. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `peering` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PEERING`**:
ID of the peering or fully qualified identifier for the peering.
To set the `peering` attribute:

- provide the argument `peering` on the command line.**

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

: This command uses the `managedidentities/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: These variants are also available:

```
gcloud alpha active-directory peerings update
```

```
gcloud beta active-directory peerings update
```