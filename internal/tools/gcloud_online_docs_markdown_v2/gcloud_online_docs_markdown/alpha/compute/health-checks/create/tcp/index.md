# gcloud alpha compute health-checks create tcp  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp)*

**NAME**

: **gcloud alpha compute health-checks create tcp - create a TCP health check to monitor load balanced instances**

**SYNOPSIS**

: **`gcloud alpha compute health-checks create tcp` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--check-interval)`=`CHECK_INTERVAL`; default="5s"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--description)`=`DESCRIPTION`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--enable-logging)`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--healthy-threshold)`=`HEALTHY_THRESHOLD`; default=2] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--proxy-header)`=`PROXY_HEADER`; default="NONE"] [`[--request](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--request)`=`REQUEST`] [`[--response](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--response)`=`RESPONSE`] [`[--source-regions](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--source-regions)`=`REGION`,…,[…]] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--timeout)`=`TIMEOUT`; default="5s"] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`; default=2] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--region)`=`REGION`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--port)`=`PORT`; default=80 `[--port-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--port-name)`=`PORT_NAME` `[--use-serving-port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#--use-serving-port)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute health-checks create tcp`
is used to create a non-legacy health check using the TCP protocol. You can use
this health check for Google Cloud load balancers or for managed instance group
autohealing. For more information, see the health checks overview at: [https://cloud.google.com/load-balancing/docs/health-check-concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the TCP health check to create.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
The default value is ``5s``. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--description**:
An optional string description for the TCP health check.

**--enable-logging**:
Enable logging of health check probe results to Stackdriver. Logging is disabled
by default.
Use --no-enable-logging to disable logging.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy. The default is 2.

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

**--response**:
An optional string of up to 1024 characters that the health checker expects to
receive from the instance. If the response is not received exactly, the health
check probe fails. If `--response` is configured, but not
`--request`, the health checker will wait for a response anyway.
Unless your system automatically sends out a message in response to a successful
handshake, only configure `--response` to match an explicit
`--request`.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute health-checks create tcp
```

```
gcloud beta compute health-checks create tcp
```