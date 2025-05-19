# gcloud alpha compute instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances)*

**NAME**

: **gcloud alpha compute instances - read and manipulate Compute Engine virtual machine instances**

**SYNOPSIS**

: **`gcloud alpha compute instances` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate Compute Engine virtual machine
instances.
For more information about virtual machine instances, see the [virtual machine
instances documentation](https://cloud.google.com/compute/docs/instances/).
See also: [Instances
API](https://cloud.google.com/compute/docs/reference/rest/v1/instances).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[bulk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk)`**:
`(ALPHA)` Manipulate multiple Compute Engine virtual machines with
single command executions.

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/config)`**:
`(ALPHA)` Manage Compute Engine instance configurations.

**`[network-interfaces](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces)`**:
`(ALPHA)` Read and manipulate Compute Engine instance network
interfaces.

**`[ops-agents](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents)`**:
`(ALPHA)` Manage Google Cloud Observability agents for Compute Engine
VM instances.

**`[os-inventory](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/os-inventory)`**:
`(ALPHA)` Read Compute Engine OS Inventory Data and Related
Resources.

**`[vulnerabilities](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/vulnerabilities)`**:
`(ALPHA)` List and describe instance vulnerabilities.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-access-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config)`**:
`(ALPHA)` Create a Compute Engine virtual machine access
configuration.

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-iam-policy-binding)`**:
`(ALPHA)` Add IAM policy binding to a Compute Engine instance.

**`[add-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-labels)`**:
`(ALPHA)` Add labels to Google Compute Engine virtual machine
instances.

**`[add-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-metadata)`**:
`(ALPHA)` Add or update instance metadata.

**`[add-partner-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-partner-metadata)`**:
`(ALPHA)` Add or update partner metadata.

**`[add-resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-resource-policies)`**:
`(ALPHA)` Add resource policies to Compute Engine VM instances.

**`[add-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-tags)`**:
`(ALPHA)` Add tags to Compute Engine virtual machine instances.

**`[attach-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/attach-disk)`**:
`(ALPHA)` Attach a disk to an instance.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/create)`**:
`(ALPHA)` Create Compute Engine virtual machine instances.

**`[create-with-container](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/create-with-container)`**:
`(ALPHA)` Creates Compute Engine virtual machine instances running
container images.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete)`**:
`(ALPHA)` Delete Compute Engine virtual machine instances.

**`[delete-access-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config)`**:
`(ALPHA)` Delete an access configuration from a virtual machine
network interface.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/describe)`**:
`(ALPHA)` Describe a virtual machine instance.

**`[detach-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/detach-disk)`**:
`(ALPHA)` Detach disks from Compute Engine virtual machine instances.

**`[export](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/export)`**:
`(ALPHA)` Export a Compute Engine virtual machine instance's
configuration to a file.

**`[get-guest-attributes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/get-guest-attributes)`**:
`(ALPHA)` Get the Guest Attributes for a compute instance.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/get-iam-policy)`**:
`(ALPHA)` Get the IAM policy for a Compute Engine instance.

**`[get-serial-port-output](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/get-serial-port-output)`**:
`(ALPHA)` Read output from a virtual machine instance's serial port.

**`[get-shielded-identity](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/get-shielded-identity)`**:
`(ALPHA)` Get the Shielded identity for a Compute Engine instance.

**`[import](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/import)`**:
`(ALPHA)` Create Compute Engine virtual machine instances from
virtual appliance in OVA/OVF format.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/list)`**:
`(ALPHA)` List Compute Engine instances.

**`[move](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/move)`**:
`(ALPHA)` `(DEPRECATED)` Move an instance and its attached
persistent disks between zones.

**`[patch-partner-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/patch-partner-metadata)`**:
`(ALPHA)` Patch partner metadata.

**`[perform-maintenance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/perform-maintenance)`**:
`(ALPHA)` Perform maintenance of Google Compute Engine instance.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-iam-policy-binding)`**:
`(ALPHA)` Remove IAM policy binding from a Compute Engine instance.

**`[remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-labels)`**:
`(ALPHA)` Remove labels from Google Compute Engine virtual machine
instances.

**`[remove-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-metadata)`**:
`(ALPHA)` Remove instance metadata.

**`[remove-partner-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata)`**:
`(ALPHA)` Remove partner metadata.

**`[remove-resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-resource-policies)`**:
`(ALPHA)` Remove resource policies from Compute Engine VM instances.

**`[remove-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-tags)`**:
`(ALPHA)` Remove tags from Compute Engine virtual machine instances.

**`[report-host-as-faulty](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/report-host-as-faulty)`**:
`(ALPHA)` Report a host as faulty to start the repair process.

**`[reset](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/reset)`**:
`(ALPHA)` Reset a virtual machine instance.

**`[resume](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/resume)`**:
`(ALPHA)` Resume a virtual machine instance.

**`[send-diagnostic-interrupt](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/send-diagnostic-interrupt)`**:
`(ALPHA)` Send a diagnostic interrupt to a virtual machine instance.

**`[set-disk-auto-delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete)`**:
`(ALPHA)` Set auto-delete behavior for disks.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-iam-policy)`**:
`(ALPHA)` Set IAM policy for a Compute Engine instance.

**`[set-machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-machine-type)`**:
`(ALPHA)` Set machine type for Compute Engine virtual machines.

**`[set-min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-min-cpu-platform)`**:
`(ALPHA)` `(DEPRECATED)` Set minimum CPU platform for
Compute Engine virtual machines.

**`[set-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-name)`**:
`(ALPHA)` Set the name of a Compute Engine virtual machine.

**`[set-scheduling](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scheduling)`**:
`(ALPHA)` Set scheduling options for Compute Engine virtual machines.

**`[set-scopes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes)`**:
`(ALPHA)` Set scopes and service account for a Compute Engine VM
instance.

**`[simulate-maintenance-event](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/simulate-maintenance-event)`**:
`(ALPHA)` Simulate host maintenance of VM instances.

**`[start](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/start)`**:
`(ALPHA)` Start a stopped virtual machine instance.

**`[stop](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/stop)`**:
`(ALPHA)` Stop a virtual machine instance.

**`[suspend](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/suspend)`**:
`(ALPHA)` Suspend a virtual machine instance.

**`[tail-serial-port-output](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/tail-serial-port-output)`**:
`(ALPHA)` Periodically fetch new output from a virtual machine
instance's serial port and display it as it becomes available.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update)`**:
`(ALPHA)` Update a Compute Engine virtual machine.

**`[update-access-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config)`**:
`(ALPHA)` Update a Compute Engine virtual machine access
configuration.

**`[update-container](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-container)`**:
`(ALPHA)` Updates Compute Engine virtual machine instances running
container images.

**`[update-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-from-file)`**:
`(ALPHA)` Update a Compute Engine virtual machine instance using a
configuration file.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instances
```

```
gcloud beta compute instances
```