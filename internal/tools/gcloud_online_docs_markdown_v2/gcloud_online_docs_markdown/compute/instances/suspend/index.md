# gcloud compute instances suspend  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend](https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend)*

**NAME**

: **gcloud compute instances suspend - suspend a virtual machine instance**

**SYNOPSIS**

: **`gcloud compute instances suspend` `[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend#INSTANCE_NAMES)` [`[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend#INSTANCE_NAMES)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend#--async)`] [`[--discard-local-ssd](https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend#--discard-local-ssd)`[=`DISCARD_LOCAL_SSD`]] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/suspend#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances suspend` is used to suspend a Compute
Engine virtual machine. Suspending a VM is the equivalent of sleep or standby
mode: the guest receives an ACPI S3 suspend signal, after which all VM state is
saved to temporary storage. An instance can only be suspended while it is in the
RUNNING state. A suspended instance will be put in SUSPENDED state.
Note: A suspended instance can be resumed by running the gcloud compute
instances resume command.
If a VM has any attached Local SSD disks, you can preserve the Local SSD data
when you suspend the VM by setting `--discard-local-ssd=False`.
Preserving the Local SSD disk data incurs costs and is subject to limitations.
Limitations:

- Limitations for suspending a VM: [https://cloud.google.com/compute/docs/instances/suspend-resume-instance#limitations](https://cloud.google.com/compute/docs/instances/suspend-resume-instance#limitations)
- Limitations for preserving Local SSD data: [https://cloud.google.com/compute/docs/disks/local-ssd#stop_instance](https://cloud.google.com/compute/docs/disks/local-ssd#stop_instance)

**EXAMPLES**

: To suspend an instance named ``test-instance``,
run:

```
gcloud compute instances suspend test-instance
```

To suspend an instance named `test-instance` that has a Local SSD,
run:

```
gcloud compute instances suspend test-instance --discard-local-ssd=True
```

Using `--discard-local-ssd` without a value defaults to
`True`.

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAMES` [`INSTANCE_NAMES` …]**:
Names of the instances to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--discard-local-ssd**:
If set to true, local SSD data is discarded.

**--zone**:
Zone of the instances to operate on. If not specified, you might be prompted to
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

: These variants are also available:

```
gcloud alpha compute instances suspend
```

```
gcloud beta compute instances suspend
```