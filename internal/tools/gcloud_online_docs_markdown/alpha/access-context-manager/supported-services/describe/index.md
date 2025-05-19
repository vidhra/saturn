# gcloud alpha access-context-manager supported-services describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services/describe)*

**NAME**

: **gcloud alpha access-context-manager supported-services describe - gets information about a VPC Service Controls Supported Service**

**SYNOPSIS**

: **`gcloud alpha access-context-manager supported-services describe` `[SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services/describe#SERVICE_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Get service information allowed in an access policy object.

**EXAMPLES**

: To get VPC Service Controls support information for
`bigquery.googleapis.com`, run:

```
gcloud alpha access-context-manager supported-services describe bigquery.googleapis.com
```

**POSITIONAL ARGUMENTS**

: **Supported service resource - VPC Service Controls supported service. This
represents a Cloud resource.
This must be specified.

**`SERVICE_NAME`**:
ID of the supported-service or fully qualified identifier for the
supported-service.
To set the `service_name` attribute:

- provide the argument `service_name` on the command line.**

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

: This command uses the `accesscontextmanager/v1alpha` API. The full
documentation for this API can be found at: [https://cloud.google.com/access-context-manager/docs/reference/rest/](https://cloud.google.com/access-context-manager/docs/reference/rest/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager supported-services describe
```

```
gcloud beta access-context-manager supported-services describe
```