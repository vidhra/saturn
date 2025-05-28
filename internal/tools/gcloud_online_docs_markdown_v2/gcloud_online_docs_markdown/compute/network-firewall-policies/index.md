# gcloud compute network-firewall-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies)*

**NAME**

: **gcloud compute network-firewall-policies - manage Compute Engine network firewall policies**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Compute Engine network firewall policies. Network firewall policies are
used to control incoming/outgoing traffic.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[associations](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations)`**:
Read and manipulate Compute Engine network firewall policy associations.

**`[mirroring-rules](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules)`**:
Read and manipulate Compute Engine packet mirroring rules in network firewall
policy.

**`[rules](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules)`**:
Read and manipulate Compute Engine network firewall policy rules.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[clone-rules](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules)`**:
Replace the rules of a Compute Engine network firewall policy with rules from
another policy.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create)`**:
Create a Compute Engine Network firewall policy.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete)`**:
Delete a Compute Engine network firewall policy.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/describe)`**:
Describe a Compute Engine network firewall policy.

**`[export-rules](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/export-rules)`**:
Export Compute Engine network firewall policy rules.

**`[get-effective-firewalls](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls)`**:
Get the effective firewalls for a network.

**`[import-rules](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/import-rules)`**:
Import a Compute Engine network firewall policy rules.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/list)`**:
List Compute Engine network firewall policies.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update)`**:
Update a Compute Engine network firewall policy.

**NOTES**

: These variants are also available:

```
gcloud alpha compute network-firewall-policies
```

```
gcloud beta compute network-firewall-policies
```