# gcloud compute health-checks create http2  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2)*

**NAME**

: **gcloud compute health-checks create http2 - create a HTTP2 health check to monitor load balanced instances**

**SYNOPSIS**

: **`gcloud compute health-checks create http2` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--check-interval)`=`CHECK_INTERVAL`; default="5s"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--description)`=`DESCRIPTION`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--enable-logging)`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--healthy-threshold)`=`HEALTHY_THRESHOLD`; default=2] [`[--host](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--host)`=`HOST`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--proxy-header)`=`PROXY_HEADER`; default="NONE"] [`[--request-path](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--request-path)`=`REQUEST_PATH`; default="/"] [`[--response](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--response)`=`RESPONSE`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--timeout)`=`TIMEOUT`; default="5s"] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`; default=2] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--region)`=`REGION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--port)`=`PORT`; default=80 `[--port-name](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--port-name)`=`PORT_NAME` `[--use-serving-port](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#--use-serving-port)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http2#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute health-checks create http2` is used to create a
non-legacy health check using the HTTP/2 protocol. You can use this health check
for Google Cloud load balancers or for managed instance group autohealing. For
more information, see the health checks overview at: [https://cloud.google.com/load-balancing/docs/health-check-concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)

**EXAMPLES**

: To create a HTTP2 health check with default options, run:

```
gcloud compute health-checks create http2 my-health-check-name
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the HTTP2 health check to create.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
The default value is ``5s``. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--description**:
An optional string description for the HTTP2 health check.

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
gcloud alpha compute health-checks create http2
```

```
gcloud beta compute health-checks create http2
```