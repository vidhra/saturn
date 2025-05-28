# gcloud sql operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/operations/describe](https://cloud.google.com/sdk/gcloud/reference/sql/operations/describe)*

**NAME**

: **gcloud sql operations describe - retrieves information about a Cloud SQL instance operation**

**SYNOPSIS**

: **`gcloud sql operations describe` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/sql/operations/describe#OPERATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieves information about a Cloud SQL instance operation.

**EXAMPLES**

: To describe an operation with the name "prod-operation-id", run:

```
gcloud sql operations describe prod-operation-id
```

**POSITIONAL ARGUMENTS**

: **`OPERATION`**:
Name that uniquely identifies the operation.

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
gcloud alpha sql operations describe
```

```
gcloud beta sql operations describe
```