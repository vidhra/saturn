# gcloud compute instance-groups managed resize-requests delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/delete](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/delete)*

**NAME**

: **gcloud compute instance-groups managed resize-requests delete - delete a Compute Engine managed instance group resize request**

**SYNOPSIS**

: **`gcloud compute instance-groups managed resize-requests delete` `[INSTANCE_GROUP_MANAGER](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/delete#INSTANCE_GROUP_MANAGER)` `[--resize-requests](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/delete#--resize-requests)`=`RESIZE_REQUEST_NAMES`,[…] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed resize-requests delete`
deletes one or more Compute Engine managed instance group resize requests.
You can only delete a request when it is in a state SUCCEEDED, FAILED, or
CANCELLED.

**EXAMPLES**

: To delete a resize request for a managed instance group, run the following
command:

```
gcloud compute instance-groups managed resize-requests delete my-mig --resize-requests=resize-request-1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_GROUP_MANAGER`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--resize-requests**:
A list of comma-separated names of resize requests to delete.

**OPTIONAL FLAGS**

: **--zone**:
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
gcloud alpha compute instance-groups managed resize-requests delete
```

```
gcloud beta compute instance-groups managed resize-requests delete
```