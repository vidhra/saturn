# gcloud compute instances set-machine-type  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type)*

**NAME**

: **gcloud compute instances set-machine-type - set machine type for Compute Engine virtual machines**

**SYNOPSIS**

: **`gcloud compute instances set-machine-type` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#INSTANCE_NAME)` [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#--machine-type)`=`MACHINE_TYPE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#--zone)`=`ZONE`] [`[--custom-cpu](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#--custom-cpu)`=`CUSTOM_CPU` `[--custom-memory](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#--custom-memory)`=`CUSTOM_MEMORY` : `[--custom-extensions](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#--custom-extensions)` `[--custom-vm-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#--custom-vm-type)`=`CUSTOM_VM_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: ``gcloud compute instances set-machine-type``
lets you change the machine type of a virtual machine in the
`TERMINATED` state (that is, a virtual machine instance that has been
stopped).
For example, if ``example-instance`` is a
``g1-small`` virtual machine currently in the
`TERMINATED` state, running:

```
gcloud compute instances set-machine-type example-instance --zone us-central1-b --machine-type n1-standard-4
```

will change the machine type to
``n1-standard-4``, so that when you next start
``example-instance``, it will be provisioned as
an ``n1-standard-4`` instead of a
``g1-small``.
See [https://cloud.google.com/compute/docs/machine-types](https://cloud.google.com/compute/docs/machine-types)
for more information on machine types.

**EXAMPLES**

: To change the machine type of a VM to `n1-standard-4`, run:

```
gcloud compute instances set-machine-type example-instance --zone=us-central1-b --machine-type=n1-standard-4
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--machine-type**:
Specifies the machine type used for the instances. To get a list of available
machine types, run 'gcloud compute machine-types list'. Either this flag,
--custom-cpu, or --custom-memory must be specified.

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

**--custom-cpu**

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
gcloud alpha compute instances set-machine-type
```

```
gcloud beta compute instances set-machine-type
```