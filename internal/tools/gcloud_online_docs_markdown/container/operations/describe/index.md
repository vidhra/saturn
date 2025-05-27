# gcloud container operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/operations/describe](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe)*

**NAME**

: **gcloud container operations describe - describe an operation**

**SYNOPSIS**

: **`gcloud container operations describe` `[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe#OPERATION_ID)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an operation.

**EXAMPLES**

: To describe an operation, run:

```
gcloud container operations describe sample-operation-id
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_ID`**:
The operation id to look up.

**FLAGS**

: **--location**

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
gcloud alpha container operations describe
```

```
gcloud beta container operations describe
```