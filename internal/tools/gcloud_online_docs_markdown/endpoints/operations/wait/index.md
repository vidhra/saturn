# gcloud endpoints operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/wait](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/wait)*

**NAME**

: **gcloud endpoints operations wait - waits for an operation to complete**

**SYNOPSIS**

: **`gcloud endpoints operations wait` `[OPERATION](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/wait#OPERATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will block until an operation has been marked as complete.
Note that the `operations/` prefix of the operation name is optional
and may be omitted.

**EXAMPLES**

: To wait on an operation named
`operations/serviceConfigs.my-service.1` to complete, run:

```
gcloud endpoints operations wait serviceConfigs.my-service.1
```

**POSITIONAL ARGUMENTS**

: **`OPERATION`**:
The name of the operation on which to wait.

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
gcloud alpha endpoints operations wait
```

```
gcloud beta endpoints operations wait
```