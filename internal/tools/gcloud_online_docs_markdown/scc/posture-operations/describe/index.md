# gcloud scc posture-operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/posture-operations/describe](https://cloud.google.com/sdk/gcloud/reference/scc/posture-operations/describe)*

**NAME**

: **gcloud scc posture-operations describe - describe a Cloud Security Command Center posture long running operation**

**SYNOPSIS**

: **`gcloud scc posture-operations describe` `[OPERATION_NAME](https://cloud.google.com/sdk/gcloud/reference/scc/posture-operations/describe#OPERATION_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/posture-operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Security Command Center (SCC) posture long running operation.

**EXAMPLES**

: To return long running operation status for operation
(operation-1694515698847-605272e4bcd7c-f93dade6-067467ae) of parent
organizations/123/locations/global, run:

```
gcloud scc posture-operations describe organizations/123/locations/global/operations/operation-1694515698847-605272e4bcd7c-f93dade6-067467ae
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_NAME`**:
Relative resource name of the operation, of the format:
organizations/<organizationID>/locations/<location>/operations/<operationID>.

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

: This command uses the `securityposture/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: This variant is also available:

```
gcloud alpha scc posture-operations describe
```