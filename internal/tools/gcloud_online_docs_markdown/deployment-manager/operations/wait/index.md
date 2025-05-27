# gcloud deployment-manager operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/wait](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/wait)*

**NAME**

: **gcloud deployment-manager operations wait - wait for all operations specified to complete before returning**

**SYNOPSIS**

: **`gcloud deployment-manager operations wait` `[OPERATION_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/wait#OPERATION_NAME)` [`[OPERATION_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/wait#OPERATION_NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Polls until all operations have finished, then prints the resulting operations
along with any operation errors.

**EXAMPLES**

: To poll until an operation has completed, run:

```
gcloud deployment-manager operations wait operation-name
```

To poll until several operations have all completed, run:

```
gcloud deployment-manager operations wait operation-one operation-two operation-three
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_NAME` [`OPERATION_NAME` …]**:
Operation name.

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
gcloud alpha deployment-manager operations wait
```

```
gcloud beta deployment-manager operations wait
```