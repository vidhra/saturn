# gcloud compute health-checks create grpc  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc)*

**NAME**

: **gcloud compute health-checks create grpc - create a gRPC health check to monitor load balanced instances**

**SYNOPSIS**

: **`gcloud compute health-checks create grpc` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--check-interval)`=`CHECK_INTERVAL`; default="5s"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--description)`=`DESCRIPTION`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--enable-logging)`] [`[--grpc-service-name](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--grpc-service-name)`=`GRPC_SERVICE_NAME`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--healthy-threshold)`=`HEALTHY_THRESHOLD`; default=2] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--timeout)`=`TIMEOUT`; default="5s"] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`; default=2] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--region)`=`REGION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--port)`=`PORT` `[--use-serving-port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#--use-serving-port)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/grpc#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute health-checks create grpc` is used to create a
non-legacy health check using the gRPC protocol. You can use this health check
for Google Cloud load balancers or for managed instance group autohealing. For
more information, see the health checks overview at: [https://cloud.google.com/load-balancing/docs/health-check-concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the gRPC health check to create.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
The default value is ``5s``. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--description**:
An optional string description for the gRPC health check.

**--enable-logging**:
Enable logging of health check probe results to Stackdriver. Logging is disabled
by default.
Use --no-enable-logging to disable logging.

**--grpc-service-name**:
An optional gRPC service name string of up to 1024 characters to include in the
gRPC health check request. Only ASCII characters are allowed.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy. The default is 2.

**--timeout**:
If Google Compute Engine doesn't receive a healthy response from the instance by
the time specified by the value of this flag, the health check request is
considered a failure. For example, specifying
``10s`` will cause the check to wait for 10
seconds before considering the request a failure. The default value is
``5s``. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--unhealthy-threshold**:
The number of consecutive health check failures before a healthy instance is
marked as unhealthy. The default is 2.

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

: These variants are also available:

```
gcloud alpha compute health-checks create grpc
```

```
gcloud beta compute health-checks create grpc
```