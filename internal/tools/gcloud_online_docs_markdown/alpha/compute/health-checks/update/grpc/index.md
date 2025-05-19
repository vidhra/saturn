# gcloud alpha compute health-checks update grpc  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc)*

**NAME**

: **gcloud alpha compute health-checks update grpc - update a gRPC health check**

**SYNOPSIS**

: **`gcloud alpha compute health-checks update grpc` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--check-interval)`=`CHECK_INTERVAL`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--description)`=`DESCRIPTION`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--enable-logging)`] [`[--grpc-service-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--grpc-service-name)`=`GRPC_SERVICE_NAME`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--healthy-threshold)`=`HEALTHY_THRESHOLD`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--timeout)`=`TIMEOUT`] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--region)`=`REGION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--port)`=`PORT` `[--use-serving-port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#--use-serving-port)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/grpc#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute health-checks update grpc`
is used to update an existing gRPC health check. Only arguments passed in will
be updated on the health check. Other attributes will remain unaffected.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the gRPC health check to update.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--description**:
A textual description for the gRPC health check. Pass in an empty string to
unset.

**--enable-logging**:
Enable logging of health check probe results to Stackdriver. Logging is disabled
by default.
Use --no-enable-logging to disable logging.

**--grpc-service-name**:
An optional gRPC service name string of up to 1024 characters to include in the
gRPC health check request. Pass in an empty string to unset. Only ASCII
characters are allowed.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy.

**--timeout**:
If Google Compute Engine doesn't receive a healthy response from the instance by
the time specified by the value of this flag, the health check request is
considered a failure. For example, specifying
``10s`` will cause the check to wait for 10
seconds before considering the request a failure. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--unhealthy-threshold**:
The number of consecutive health check failures before a healthy instance is
marked as unhealthy.

**--global**

**--port**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute health-checks update grpc
```

```
gcloud beta compute health-checks update grpc
```