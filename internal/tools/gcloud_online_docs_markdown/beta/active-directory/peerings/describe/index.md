# gcloud beta active-directory peerings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/describe](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/describe)*

**NAME**

: **gcloud beta active-directory peerings describe - describe a Managed Microsoft Active Directory domain peering**

**SYNOPSIS**

: **`gcloud beta active-directory peerings describe` `[PEERING](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/describe#PEERING)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Show metadata for a Managed Microsoft AD domain peering.
Displays all metadata associated with a Active Directory domain peering given a
valid domain peering name.
This command can fail for the following reasons:

- The specified domain peering does not exist.
- The active account does not have permission to access the given domain.

**EXAMPLES**

: The following command gets metadata for an AD domain peering with the name
``my-peering``.

```
gcloud beta active-directory peerings describe my-peering
```

**POSITIONAL ARGUMENTS**

: **Peering resource - Name of the Managed Microsoft AD domain peering you want to
describe. This represents a Cloud resource. (NOTE) Some attributes are not given
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

: This command uses the `managedidentities/v1beta1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud active-directory peerings describe
```

```
gcloud alpha active-directory peerings describe
```