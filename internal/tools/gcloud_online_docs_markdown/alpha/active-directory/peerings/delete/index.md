# gcloud alpha active-directory peerings delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/peerings/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/peerings/delete)*

**NAME**

: **gcloud alpha active-directory peerings delete - delete a Managed Microsoft Active Directory domain peering**

**SYNOPSIS**

: **`gcloud alpha active-directory peerings delete` `[PEERING](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/peerings/delete#PEERING)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/peerings/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/peerings/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete a Managed Microsoft Active Directory (AD) domain
peering.
This command can fail for the following reasons:

- The active account does not have permission to access the given AD domain.
- The domain peering is no longer existed.

**EXAMPLES**

: The following command deletes an AD domain peering with the name
``my-peering``.

```
gcloud alpha active-directory peerings delete my-peering
```

**POSITIONAL ARGUMENTS**

: **Peering resource - Name of the managed Managed Microsoft AD domain peering you
want to delete. This represents a Cloud resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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
gcloud active-directory peerings delete
```

```
gcloud beta active-directory peerings delete
```