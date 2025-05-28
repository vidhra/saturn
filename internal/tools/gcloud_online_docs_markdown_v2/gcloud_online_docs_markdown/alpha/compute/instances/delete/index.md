# gcloud alpha compute instances delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete)*

**NAME**

: **gcloud alpha compute instances delete - delete Compute Engine virtual machine instances**

**SYNOPSIS**

: **`gcloud alpha compute instances delete` `[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete#INSTANCE_NAMES)` [`[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete#INSTANCE_NAMES)` …] [`[--no-graceful-shutdown](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete#--graceful-shutdown)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete#--zone)`=`ZONE`] [`[--delete-disks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete#--delete-disks)`=`DISK_TYPE`     | `[--keep-disks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete#--keep-disks)`=`DISK_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances delete` deletes
one or more Compute Engine virtual machine instances.

**EXAMPLES**

: To delete an instance called 'instance-1' in the zone 'us-central-2-a', run:

```
gcloud alpha compute instances delete instance-1 --zone=us-central2-a
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAMES` [`INSTANCE_NAMES` …]**:
Names of the instances to delete. For details on valid instance names, refer to
the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--no-graceful-shutdown**:
Deletes the instance immediately without gracefully shutting it down. If a
graceful shutdown is in progress, then the instance is forcefully stopped and
deleted.

**--zone**:
Zone of the instances to delete. If not specified, you might be prompted to
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

**--delete-disks**

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
gcloud compute instances delete
```

```
gcloud beta compute instances delete
```