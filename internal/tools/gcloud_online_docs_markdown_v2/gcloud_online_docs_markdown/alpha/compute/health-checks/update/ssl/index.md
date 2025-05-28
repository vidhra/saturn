# gcloud alpha compute health-checks update ssl  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl)*

**NAME**

: **gcloud alpha compute health-checks update ssl - update a SSL health check**

**SYNOPSIS**

: **`gcloud alpha compute health-checks update ssl` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--check-interval)`=`CHECK_INTERVAL`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--description)`=`DESCRIPTION`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--enable-logging)`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--healthy-threshold)`=`HEALTHY_THRESHOLD`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--proxy-header)`=`PROXY_HEADER`] [`[--request](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--request)`=`REQUEST`] [`[--response](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--response)`=`RESPONSE`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--timeout)`=`TIMEOUT`] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--region)`=`REGION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--port)`=`PORT` `[--port-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--port-name)`=`PORT_NAME` `[--use-serving-port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#--use-serving-port)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/ssl#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute health-checks update ssl`
is used to update an existing SSL health check. Only arguments passed in will be
updated on the health check. Other attributes will remain unaffected.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the SSL health check to update.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--description**:
A textual description for the SSL health check. Pass in an empty string to
unset.

**--enable-logging**:
Enable logging of health check probe results to Stackdriver. Logging is disabled
by default.
Use --no-enable-logging to disable logging.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy.

**--proxy-header**:
The type of proxy protocol header to be sent to the backend.
`PROXY_HEADER` must be one of:

**`NONE`**:
No proxy header is added.

**`PROXY_V1`**:
Adds the header "PROXY UNKNOWN\r\n".

**--request**:
An optional string of up to 1024 characters to send once the health check TCP
connection has been established. The health checker then looks for a reply of
the string provided in the `--response` field.
If `--response` is not configured, the health checker does not wait
for a response and regards the probe as successful if the TCP or SSL handshake
was successful.
Setting this to an empty string will clear any existing request value.

**--response**:
An optional string of up to 1024 characters that the health checker expects to
receive from the instance. If the response is not received exactly, the health
check probe fails. If `--response` is configured, but not
`--request`, the health checker will wait for a response anyway.
Unless your system automatically sends out a message in response to a successful
handshake, only configure `--response` to match an explicit
`--request`. Setting this to an empty string will clear any existing
response value.

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
gcloud compute health-checks update ssl
```

```
gcloud beta compute health-checks update ssl
```