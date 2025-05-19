# gcloud alpha compute instance-groups managed set-autohealing  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing)*

**NAME**

: **gcloud alpha compute instance-groups managed set-autohealing - set autohealing policy for managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed set-autohealing` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#NAME)` [`[--initial-delay](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#--initial-delay)`=`INITIAL_DELAY`] [`[--health-check](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#--health-check)`=`HEALTH_CHECK`     | `[--http-health-check](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#--http-health-check)`=`HTTP_HEALTH_CHECK`     | `[--https-health-check](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#--https-health-check)`=`HTTPS_HEALTH_CHECK`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `(DEPRECATED)` Set autohealing policy for
managed instance group.
This command is deprecated and will not be promoted to GA. Please use
`gcloud beta instance-groups managed update` instead.
`gcloud alpha compute instance-groups managed set-autohealing`
updates the autohealing policy for an existing managed instance group.
If health check is specified, the resulting autohealing policy will be triggered
by the health-check signal i.e. the autohealing action (RECREATE) on an instance
will be performed if the health-check signals that the instance is UNHEALTHY. If
no health check is specified, the resulting autohealing policy will be triggered
by instance's status i.e. the autohealing action (RECREATE) on an instance will
be performed if the instance.status is not RUNNING.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**FLAGS**

: **--initial-delay**:
Specifies the number of seconds that a new VM takes to initialize and run its
startup script. During a VM's initial delay period, the MIG ignores unsuccessful
health checks because the VM might be in the startup process. This prevents the
MIG from prematurely recreating a VM. If the health check receives a healthy
response during the initial delay, it indicates that the startup process is
complete and the VM is ready. The value of initial delay must be between 0 and
3600 seconds. The default value is 0. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--health-check**

**--region**

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
allowlist. This variant is also available:

```
gcloud beta compute instance-groups managed set-autohealing
```