# gcloud services disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/disable](https://cloud.google.com/sdk/gcloud/reference/services/disable)*

**NAME**

: **gcloud services disable - disable a service for consumption for a project**

**SYNOPSIS**

: **`gcloud services disable` [`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/services/disable#SERVICE)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/disable#--async)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/services/disable#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command disables one or more previously-enabled services for consumption.
To see a list of the enabled services for a project, run:

```
gcloud services list
```

More information on listing services can be found at: [https://cloud.google.com/service-usage/docs/list-services](https://cloud.google.com/service-usage/docs/list-services)
and on disabling a service at: [https://cloud.google.com/service-usage/docs/enable-disable](https://cloud.google.com/service-usage/docs/enable-disable)

**EXAMPLES**

: To disable a service called `my-consumed-service` for the active
project, run:

```
gcloud services disable my-consumed-service
```

To run the same command asynchronously (non-blocking), run:

```
gcloud services disable my-consumed-service --async
```

**POSITIONAL ARGUMENTS**

: **[`SERVICE` …]**:
The name of the service(s) to disable.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--force**:
If specified, the disable call will proceed even if there are enabled services
which depend on the service to be disabled or disable the service used in last
30 days or was enabled in recent 3 days. Forcing the call means that the
services which depend on the service to be disabled will also be disabled.

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

: This variant is also available:

```
gcloud beta services disable
```