# gcloud compute instance-groups managed resize-requests create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create)*

**NAME**

: **gcloud compute instance-groups managed resize-requests create - create a Compute Engine managed instance group resize request**

**SYNOPSIS**

: **`gcloud compute instance-groups managed resize-requests create` `[INSTANCE_GROUP_MANAGER](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#INSTANCE_GROUP_MANAGER)` `[--resize-by](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--resize-by)`=`RESIZE_BY` `[--resize-request](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--resize-request)`=`RESIZE_REQUEST_NAME` [`[--requested-run-duration](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--requested-run-duration)`=`REQUESTED_RUN_DURATION`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Compute Engine managed instance group resize request.

**EXAMPLES**

: To create a resize request for a managed instance group, run the following
command:

```
gcloud compute instance-groups managed resize-requests create my-mig --resize-request=resize-request-1 --resize-by=1 --requested-run-duration=3d1h30s
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_GROUP_MANAGER`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--resize-by**:
The number of VMs to resize managed instance group by.

**--resize-request**:
The name of the resize request to create.

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

**--zone**:
Zone of the managed instance group to operate on. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

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
gcloud alpha compute instance-groups managed resize-requests create
```

```
gcloud beta compute instance-groups managed resize-requests create
```