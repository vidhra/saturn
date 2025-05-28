# gcloud alpha compute instances set-disk-auto-delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete)*

**NAME**

: **gcloud alpha compute instances set-disk-auto-delete - set auto-delete behavior for disks**

**SYNOPSIS**

: **`gcloud alpha compute instances set-disk-auto-delete` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete#INSTANCE_NAME)` (`[--device-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete#--device-name)`=`DEVICE_NAME`     | `[--disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete#--disk)`=`DISK`) [`[--no-auto-delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete#--auto-delete)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `$gcloud alpha compute instances
set-disk-auto-delete` is used to configure the auto-delete behavior for
disks attached to Compute Engine virtual machines. When auto-delete is on, the
persistent disk is deleted when the instance it is attached to is deleted.

**EXAMPLES**

: To enable auto-delete for a disk named 'my-disk' on an instance named
'my-instance', run:

```
gcloud alpha compute instances set-disk-auto-delete my-instance --auto-delete --disk=my-disk
```

To enable auto-delete for a device named 'my-device' on an instance named
'my-instance', run:

```
gcloud alpha compute instances set-disk-auto-delete my-instance --auto-delete --device-name=my-device
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**REQUIRED FLAGS**

: **--device-name**

**OPTIONAL FLAGS**

: **--auto-delete**:
Enables auto-delete for the given disk. Enabled by default, use
`--no-auto-delete` to disable.

**--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instances set-disk-auto-delete
```

```
gcloud beta compute instances set-disk-auto-delete
```