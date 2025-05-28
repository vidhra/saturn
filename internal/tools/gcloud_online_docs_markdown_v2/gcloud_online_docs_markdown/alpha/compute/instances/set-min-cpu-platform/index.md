# gcloud alpha compute instances set-min-cpu-platform  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform)*

**NAME**

: **gcloud alpha compute instances set-min-cpu-platform - set minimum CPU platform for Compute Engine virtual machines**

**SYNOPSIS**

: **`gcloud alpha compute instances set-min-cpu-platform` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform#INSTANCE_NAME)` `[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform#--min-cpu-platform)`=`PLATFORM` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform#--async)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `(DEPRECATED)` This command is deprecated. Use $
[gcloud alpha
compute instances update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update) --set-min-cpu-platform instead.
`gcloud alpha compute instances set-min-cpu-platform` changes the
minimum CPU platform of a virtual machine with the `TERMINATED`
status (a virtual machine instance that has been stopped).
For example, running the command on example-instance virtual machine which has a
status of TERMINATED

```
gcloud alpha compute instances set-min-cpu-platform example-instance --zone us-central1-a        --min-cpu-platform "Intel Broadwell"
```

will set the minimum CPU platform to `Intel Broadwell`. When you
start `example-instance` later, it will be provisioned using at least
`Intel Broadwell` CPU platform.
To get a list of available CPU platforms in us-central1-a zone, run:

```
gcloud alpha compute zones describe us-central1-a        --format="value(availableCpuPlatforms)"
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**REQUIRED FLAGS**

: **--min-cpu-platform**:
When specified, the VM will be scheduled on host with specified CPU architecture
or a newer one. To list available CPU platforms in given zone, run:

```
gcloud alpha compute zones describe ZONE --format="value(availableCpuPlatforms)"
```

Default setting is "AUTOMATIC".
CPU platform selection is available only in selected zones.
You can find more information on-line: [https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
allowlist.