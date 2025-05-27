# gcloud container operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/operations/wait](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait)*

**NAME**

: **gcloud container operations wait - poll an operation for completion**

**SYNOPSIS**

: **`gcloud container operations wait` `[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait#OPERATION_ID)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Poll an operation for completion.

**EXAMPLES**

: To poll an operation for completion, run:

```
gcloud container operations wait sample-operation-id
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_ID`**:
The operation id to poll.

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
gcloud alpha container operations wait
```

```
gcloud beta container operations wait
```