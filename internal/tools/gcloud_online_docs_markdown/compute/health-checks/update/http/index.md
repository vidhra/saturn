# gcloud compute health-checks update http  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http)*

**NAME**

: **gcloud compute health-checks update http - update a HTTP health check**

**SYNOPSIS**

: **`gcloud compute health-checks update http` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--check-interval)`=`CHECK_INTERVAL`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--description)`=`DESCRIPTION`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--enable-logging)`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--healthy-threshold)`=`HEALTHY_THRESHOLD`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--host)`=`HOST`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--proxy-header)`=`PROXY_HEADER`] [`[--request-path](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--request-path)`=`REQUEST_PATH`] [`[--response](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--response)`=`RESPONSE`] [`[--source-regions](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--source-regions)`=`REGION`,…,[…]] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--timeout)`=`TIMEOUT`] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--region)`=`REGION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--port)`=`PORT` `[--port-name](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--port-name)`=`PORT_NAME` `[--use-serving-port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#--use-serving-port)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/http#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute health-checks update http` is used to update an
existing HTTP health check. Only arguments passed in will be updated on the
health check. Other attributes will remain unaffected.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the HTTP health check to update.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--description**:
A textual description for the HTTP health check. Pass in an empty string to
unset.

**--enable-logging**:
Enable logging of health check probe results to Stackdriver. Logging is disabled
by default.
Use --no-enable-logging to disable logging.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy.

**--host**:
The value of the host header used in this HTTP health check request. The host
header is empty by default. When empty, the health check will set the host
header to the IP address of the backend VM or endpoint. You can set the host
header to an empty value to return to this default behavior.

**--proxy-header**:
The type of proxy protocol header to be sent to the backend.
`PROXY_HEADER` must be one of:

**`NONE`**:
No proxy header is added.

**`PROXY_V1`**:
Adds the header "PROXY UNKNOWN\r\n".

**--request-path**:
The request path that this health check monitors. For example,
``/healthcheck``.

**--response**:
When empty, status code of the response determines health. When not empty,
presence of specified string in first 1024 characters of response body
determines health. Only ASCII characters allowed.

**--source-regions**:
Define the list of Google Cloud regions from which health checks are performed.
This option is supported only for global health checks that will be referenced
by DNS routing policies. If specified, the --check-interval field should be at
least 30 seconds. The --proxy-header and --request fields (for TCP health
checks) are not supported with this option.
If --source-regions is specified for a health check, then that health check
cannot be used by a backend service or by a managed instance group (for
autohealing).

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

: These variants are also available:

```
gcloud alpha compute health-checks update http
```

```
gcloud beta compute health-checks update http
```