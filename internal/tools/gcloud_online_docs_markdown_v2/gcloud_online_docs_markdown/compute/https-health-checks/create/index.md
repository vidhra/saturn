# gcloud compute https-health-checks create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create)*

**NAME**

: **gcloud compute https-health-checks create - create a legacy HTTPS health check**

**SYNOPSIS**

: **`gcloud compute https-health-checks create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#NAME)` [`[--check-interval](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--check-interval)`=`CHECK_INTERVAL`; default="5s"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--description)`=`DESCRIPTION`] [`[--healthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--healthy-threshold)`=`HEALTHY_THRESHOLD`; default=2] [`[--host](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--host)`=`HOST`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--port)`=`PORT`; default=443] [`[--request-path](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--request-path)`=`REQUEST_PATH`; default="/"] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--timeout)`=`TIMEOUT`; default="5s"] [`[--unhealthy-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#--unhealthy-threshold)`=`UNHEALTHY_THRESHOLD`; default=2] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Though you can use legacy HTTPS health checks in certain Google Cloud Platform
load balancing configurations and for managed instance group autohealing, you
should consider a non-legacy HTTPS health check created with `health-checks
create https` instead.
For more information about the differences between legacy and non-legacy health
checks see: [https://cloud.google.com/load-balancing/docs/health-check-concepts#category_and_protocol](https://cloud.google.com/load-balancing/docs/health-check-concepts#category_and_protocol)
For information about what type of health check to use for a particular load
balancer, see: [https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide](https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the HTTPS health check to create.

**FLAGS**

: **--check-interval**:
How often to perform a health check for an instance. For example, specifying
``10s`` will run the check every 10 seconds.
The default value is ``5s``. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--description**:
An optional, textual description for the HTTPS health check.

**--healthy-threshold**:
The number of consecutive successful health checks before an unhealthy instance
is marked as healthy. The default is 2.

**--host**:
The value of the host header used in this HTTPS health check request. By
default, this is empty and Compute Engine automatically sets the host header in
health requests to the same external IP address as the forwarding rule
associated with the target pool.

**--port**:
The TCP port number that this health check monitors. The default value is 443.

**--request-path**:
The request path that this health check monitors. For example,
``/healthcheck``. The default value is
``/´´.

**--timeout**:
If Compute Engine doesn't receive an HTTPS 200 response from the instance by the
time specified by the value of this flag, the health check request is considered
a failure. For example, specifying ``10s`` will
cause the check to wait for 10 seconds before considering the request a failure.
The default value is ``5s``. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--unhealthy-threshold**:
The number of consecutive health check failures before a healthy instance is
marked as unhealthy. The default is 2.

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
gcloud alpha compute https-health-checks create
```

```
gcloud beta compute https-health-checks create
```