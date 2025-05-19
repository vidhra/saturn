# gcloud compute health-checks create http  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http)*

**NAME**

: **gcloud compute health-checks create http - create a HTTP health check to monitor load balanced instances**

**SYNOPSIS**

: **`gcloud compute health-checks create http` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--check-interval)`=`CHECK_INTERVAL`; default="5s"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--description)`=`DESCRIPTION`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--enable-logging)`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--healthy-threshold)`=`HEALTHY_THRESHOLD`; default=2] [`[--host](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--host)`=`HOST`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--proxy-header)`=`PROXY_HEADER`; default="NONE"] [`[--request-path](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--request-path)`=`REQUEST_PATH`; default="/"] [`[--response](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--response)`=`RESPONSE`] [`[--source-regions](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--source-regions)`=`REGION`,…,[…]] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--timeout)`=`TIMEOUT`; default="5s"] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`; default=2] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--region)`=`REGION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--port)`=`PORT`; default=80 `[--port-name](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--port-name)`=`PORT_NAME` `[--use-serving-port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#--use-serving-port)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute health-checks create http` is used to create a
non-legacy health check using the HTTP protocol. You can use this health check
for Google Cloud load balancers or for managed instance group autohealing. For
more information, see the health checks overview at: [https://cloud.google.com/load-balancing/docs/health-check-concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the HTTP health check to create.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
The default value is ``5s``. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--description**:
An optional string description for the HTTP health check.

**--enable-logging**:
Enable logging of health check probe results to Stackdriver. Logging is disabled
by default.
Use --no-enable-logging to disable logging.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy. The default is 2.

**--host**:
The value of the host header used for the health check. If unspecified, Google
Cloud sets the host header to the IP address of the load balancer's forwarding
rule.

**--proxy-header**:
The type of proxy protocol header to be sent to the backend.
`PROXY_HEADER` must be one of:

**`NONE`**:
No proxy header is added.

**`PROXY_V1`**:
Adds the header "PROXY UNKNOWN\r\n".

**--request-path**:
The request path that this health check monitors. For example,
``/healthcheck``. The default value is
``/´´.

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
gcloud alpha compute health-checks create http
```

```
gcloud beta compute health-checks create http
```