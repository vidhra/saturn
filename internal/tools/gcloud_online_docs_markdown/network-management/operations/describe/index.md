# gcloud network-management operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-management/operations/describe](https://cloud.google.com/sdk/gcloud/reference/network-management/operations/describe)*

**NAME**

: **gcloud network-management operations describe - describe a Network Management operation**

**SYNOPSIS**

: **`gcloud network-management operations describe` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/network-management/operations/describe#OPERATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-management/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Network Management operation given a valid operation name.

**EXAMPLES**

: The following command describes an operation called
`operation-12345`:

```
gcloud network-management operations describe operation-12345
```

**POSITIONAL ARGUMENTS**

: **Operation resource - Name of the Network Management operation you want to
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

: This command uses the `networkmanagement/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)

**NOTES**

: This variant is also available:

```
gcloud beta network-management operations describe
```