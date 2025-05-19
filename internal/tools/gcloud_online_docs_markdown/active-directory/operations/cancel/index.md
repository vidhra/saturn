# gcloud active-directory operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/active-directory/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/active-directory/operations/cancel)*

**NAME**

: **gcloud active-directory operations cancel - cancel a Managed Microsoft AD operation**

**SYNOPSIS**

: **`gcloud active-directory operations cancel` `[NAME](https://cloud.google.com/sdk/gcloud/reference/active-directory/operations/cancel#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/active-directory/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel a Managed Microsoft AD operation.

**EXAMPLES**

: The following command cancels an operation called
`operation-1484002552235-425b144f8c3f8-81aa4b49-0830d1e9`:

```
gcloud active-directory operations cancel operation-1484002552235-425b144f8c3f8-81aa4b49-0830d1e9
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The operation name to cancel. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `NAME` on the command line.**

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

: These variants are also available:

```
gcloud alpha active-directory operations cancel
```

```
gcloud beta active-directory operations cancel
```