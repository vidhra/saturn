# gcloud compute instances simulate-maintenance-event  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event](https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event)*

**NAME**

: **gcloud compute instances simulate-maintenance-event - simulate host maintenance of VM instances**

**SYNOPSIS**

: **`gcloud compute instances simulate-maintenance-event` `[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event#INSTANCE_NAMES)` [`[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event#INSTANCE_NAMES)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event#--async)`] [`[--with-extended-notifications](https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event#--with-extended-notifications)`=`WITH_EXTENDED_NOTIFICATIONS`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances simulate-maintenance-event` simulates a
host maintenance event on a Compute Engine VM. For more information, see [https://cloud.google.com/compute/docs/instances/simulating-host-maintenance](https://cloud.google.com/compute/docs/instances/simulating-host-maintenance).

**EXAMPLES**

: To simulate a maintenance event on an instance named
``test-instance`` located in zone
``us-east1-d``, run:

```
gcloud compute instances simulate-maintenance-event test-instance --zone=us-east1-d
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAMES` [`INSTANCE_NAMES` …]**:
Names of the instances to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--with-extended-notifications**:
Send an extended notification before simulating a host maintenance event on a
Compute Engine VM.

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
gcloud alpha compute instances simulate-maintenance-event
```

```
gcloud beta compute instances simulate-maintenance-event
```