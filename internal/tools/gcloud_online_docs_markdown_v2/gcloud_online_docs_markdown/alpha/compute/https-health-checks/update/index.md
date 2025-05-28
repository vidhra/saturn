# gcloud alpha compute https-health-checks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update)*

**NAME**

: **gcloud alpha compute https-health-checks update - update a legacy HTTPS health check**

**SYNOPSIS**

: **`gcloud alpha compute https-health-checks update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--check-interval)`=`CHECK_INTERVAL`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--description)`=`DESCRIPTION`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--healthy-threshold)`=`HEALTHY_THRESHOLD`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--host)`=`HOST`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--port)`=`PORT`] [`[--request-path](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--request-path)`=`REQUEST_PATH`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--timeout)`=`TIMEOUT`] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute https-health-checks
update` is used to update an existing legacy HTTPS health check. Only
arguments passed in will be updated on the health check. Other attributes will
remain unaffected.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the HTTPS health check to update.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--description**:
A textual description for the HTTPS health check. Pass in an empty string to
unset.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy.

**--host**:
The value of the host header used in this HTTPS health check request. By
default, this is empty and Compute Engine automatically sets the host header in
health requests to the same external IP address as the forwarding rule
associated with the target pool. Setting this to an empty string will clear any
existing host value.

**--port**:
The TCP port number that this health check monitors.

**--request-path**:
The request path that this health check monitors. For example,
``/healthcheck``.

**--timeout**:
If Compute Engine doesn't receive an HTTPS 200 response from the instance by the
time specified by the value of this flag, the health check request is considered
a failure. For example, specifying ``10s`` will
cause the check to wait for 10 seconds before considering the request a failure.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--unhealthy-threshold**:
The number of consecutive health check failures before a healthy instance is
marked as unhealthy.

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
gcloud compute https-health-checks update
```

```
gcloud beta compute https-health-checks update
```