# gcloud alpha compute instance-groups managed resize-requests create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create)*

**NAME**

: **gcloud alpha compute instance-groups managed resize-requests create - create a Compute Engine managed instance group resize request**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed resize-requests create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#NAME)` `[--resize-request](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#--resize-request)`=`RESIZE_REQUEST_NAME` (`[--instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#INSTANCE)`,…]     | `[--resize-by](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#--resize-by)`=`RESIZE_BY`) [`[--requested-run-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#--requested-run-duration)`=`REQUESTED_RUN_DURATION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a Compute Engine managed instance group resize
request.

**EXAMPLES**

: To create a resize request for a managed instance group, run the following
command:

```
gcloud alpha compute instance-groups managed resize-requests create my-mig --resize-request=resize-request-1 --resize-by=1 --requested-run-duration=3d1h30s
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--resize-request**:
The name of the resize request to create.

**--instances**

**OPTIONAL FLAGS**

: **--requested-run-duration**:
The time you need the requested VMs to run before being automatically deleted.
The value must be formatted as the number of days, hours, minutes, or seconds
followed by `d`, `h`, `m`, and `s`
respectively. For example, specify `30m` for a duration of 30 minutes
or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds. The value
must be between `10m` (10 minutes) and `7d` (7 days).

```
If you want the managed instance group to consume a reservation or use
FLEX_START provisioning model, then this flag is optional. Otherwise,
it's required.
```

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
allowlist. These variants are also available:

```
gcloud compute instance-groups managed resize-requests create
```

```
gcloud beta compute instance-groups managed resize-requests create
```