# gcloud endpoints services delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/services/delete](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/delete)*

**NAME**

: **gcloud endpoints services delete - deletes a service from Google Service Management**

**SYNOPSIS**

: **`gcloud endpoints services delete` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/delete#SERVICE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Services that are deleted will be retained in the system for 30 days. If a
deleted service is still within this retention window, it can be undeleted with
the undelete command.

**EXAMPLES**

: To delete a service named `my-service`, run:

```
gcloud endpoints services delete my-service
```

To run the same command asynchronously (non-blocking), run:

```
gcloud endpoints services delete my-service --async
```

**POSITIONAL ARGUMENTS**

: **`SERVICE`**:
The name of the service to delete.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha endpoints services delete
```

```
gcloud beta endpoints services delete
```