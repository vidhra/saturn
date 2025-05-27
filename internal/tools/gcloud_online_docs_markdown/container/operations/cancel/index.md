# gcloud container operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel)*

**NAME**

: **gcloud container operations cancel - cancel a running operation**

**SYNOPSIS**

: **`gcloud container operations cancel` `[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel#OPERATION_ID)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel a running operation.
Cancel is a best-effort method for aborting a running operation. Operations that
have already completed can not be cancelled. If the operation has passed the
"point of no-return", cancel will have no effect.
An example of "point of no-return" in the context of Upgrade operations would be
if all the nodes have been upgraded but the operation hasn't been marked as
complete.

**EXAMPLES**

: To cancel an operation, run:

```
gcloud container operations cancel sample-operation-id
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_ID`**:
The operation id to cancel.

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
gcloud alpha container operations cancel
```

```
gcloud beta container operations cancel
```