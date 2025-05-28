# gcloud ml speech operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/speech/operations/describe](https://cloud.google.com/sdk/gcloud/reference/ml/speech/operations/describe)*

**NAME**

: **gcloud ml speech operations describe - get description of a long-running speech recognition operation**

**SYNOPSIS**

: **`gcloud ml speech operations describe` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/ml/speech/operations/describe#OPERATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/speech/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get information about a long-running speech recognition operation.

**EXAMPLES**

: To fetch details for the operation '12345':

```
gcloud ml speech operations describe 12345
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The ID of the operation to describe. This represents a
Cloud resource.
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

: This command uses the `speech/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/speech-to-text/docs/quickstart-protocol](https://cloud.google.com/speech-to-text/docs/quickstart-protocol)

**NOTES**

: These variants are also available:

```
gcloud alpha ml speech operations describe
```

```
gcloud beta ml speech operations describe
```