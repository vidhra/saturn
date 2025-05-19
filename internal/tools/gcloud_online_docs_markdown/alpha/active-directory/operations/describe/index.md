# gcloud alpha active-directory operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/operations/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/operations/describe)*

**NAME**

: **gcloud alpha active-directory operations describe - describe a Managed Microsoft AD operation**

**SYNOPSIS**

: **`gcloud alpha active-directory operations describe` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/operations/describe#OPERATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a Managed Microsoft AD operation given a valid
operation name.
This command can fail for the following reasons:

- The operation specified does not exist.
- The active account does not have permission to access the given operation.

**EXAMPLES**

: The following command describes an operation called
`operation-1484002552235-425b144f8c3f8-81aa4b49-0830d1e9`:

```
gcloud alpha active-directory operations describe operation-1484002552235-425b144f8c3f8-81aa4b49-0830d1e9
```

**POSITIONAL ARGUMENTS**

: **Operation resource - Name of the Managed Microsoft AD operation you want to
describe. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud active-directory operations describe
```

```
gcloud beta active-directory operations describe
```