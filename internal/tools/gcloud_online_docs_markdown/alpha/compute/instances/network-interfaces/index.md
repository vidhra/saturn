# gcloud alpha compute instances network-interfaces  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces)*

**NAME**

: **gcloud alpha compute instances network-interfaces - read and manipulate Compute Engine instance network interfaces**

**SYNOPSIS**

: **`gcloud alpha compute instances network-interfaces` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate Compute Engine instance network
interfaces.
For more information about instance network interfaces, see the [network
interfaces documentation](https://cloud.google.com/vpc/docs/multiple-interfaces-concepts).
See also: [instance
network interfaces API](https://cloud.google.com/compute/docs/reference/rest/v1/instances/updateNetworkInterface).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add)`**:
`(ALPHA)` Add a dynamic network interface to a Compute Engine
instance.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/delete)`**:
`(ALPHA)` Delete a dynamic network interface from a Compute Engine
instance.

**`[get-effective-firewalls](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/get-effective-firewalls)`**:
`(ALPHA)` Get the effective firewalls for a Compute Engine virtual
machine network interface.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/update)`**:
`(ALPHA)` Update a Compute Engine virtual machine network interface.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instances network-interfaces
```

```
gcloud beta compute instances network-interfaces
```