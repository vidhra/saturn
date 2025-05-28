# gcloud endpoints services undelete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/services/undelete](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/undelete)*

**NAME**

: **gcloud endpoints services undelete - undeletes a service configuration that was previously deleted**

**SYNOPSIS**

: **`gcloud endpoints services undelete` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/undelete#SERVICE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/undelete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/undelete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Services that are deleted will be retained in the system for 30 days. If a
deleted service is still within this retention window, it can be undeleted with
this command.
Note that this means that this command will not be effective for service
configurations marked for deletion more than 30 days ago.

**EXAMPLES**

: To undelete a service named `my-service`, run:

```
gcloud endpoints services undelete my-service
```

To run the same command asynchronously (non-blocking), run:

```
gcloud endpoints services undelete my-service --async
```

**POSITIONAL ARGUMENTS**

: **`SERVICE`**:
The name of the service to undelete.

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
gcloud alpha endpoints services undelete
```

```
gcloud beta endpoints services undelete
```