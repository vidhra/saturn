# gcloud compute networks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks](https://cloud.google.com/sdk/gcloud/reference/compute/networks)*

**NAME**

: **gcloud compute networks - list, create, and delete Compute Engine networks**

**SYNOPSIS**

: **`gcloud compute networks` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/networks#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/networks#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate VPC networks.
For more information about networks, see the [networks documentation](https://cloud.google.com/vpc/docs/vpc).
See also: [Networks
API](https://cloud.google.com/compute/docs/reference/rest/v1/networks).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[peerings](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings)`**:
List, create, and delete, and update VPC Network Peering.

**`[subnets](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets)`**:
List, describe, and delete, and update Compute Engine subnetworks.

**`[vpc-access](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access)`**:
Manage VPC Access Service resources.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create)`**:
Create a Compute Engine network.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete)`**:
Delete Compute Engine networks.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/networks/describe)`**:
Describe a Compute Engine network.

**`[get-effective-firewalls](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls)`**:
Get the effective firewalls of a Compute Engine network.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/networks/list)`**:
List Google Compute Engine networks.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update)`**:
Update a Compute Engine network.

**NOTES**

: These variants are also available:

```
gcloud alpha compute networks
```

```
gcloud beta compute networks
```