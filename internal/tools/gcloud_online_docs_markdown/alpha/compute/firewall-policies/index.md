# gcloud alpha compute firewall-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies)*

**NAME**

: **gcloud alpha compute firewall-policies - manage Compute Engine organization firewall policies**

**SYNOPSIS**

: **`gcloud alpha compute firewall-policies` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Compute Engine organization firewall policies.
Organization firewall policies are used to control incoming/outgoing traffic.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[associations](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/associations)`**:
`(ALPHA)` Read and manipulate Compute Engine organization firewall
policy associations.

**`[mirroring-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules)`**:
`(ALPHA)` Read and manipulate Compute Engine organization firewall
policy packet mirroring rules.

**`[rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules)`**:
`(ALPHA)` Read and manipulate Compute Engine organization firewall
policy rules.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[clone-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/clone-rules)`**:
`(ALPHA)` Replace the rules of a Compute Engine organization firewall
policy with rules from another policy.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create)`**:
`(ALPHA)` Create a Compute Engine organization firewall policy.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/delete)`**:
`(ALPHA)` Delete a Compute Engine organization firewall policy.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/describe)`**:
`(ALPHA)` Describe a Compute Engine organization firewall policy.

**`[export-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/export-rules)`**:
`(ALPHA)` Export Compute Engine organization firewall policy rules.

**`[import-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules)`**:
`(ALPHA)` Import Compute Engine organization firewall policy rules.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/list)`**:
`(ALPHA)` List Compute Engine organization firewall policies.

**`[list-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/list-rules)`**:
`(ALPHA)` List the rules of a Compute Engine organization firewall
policy.

**`[move](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/move)`**:
`(ALPHA)` Move a Compute Engine organization firewall policy.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/update)`**:
`(ALPHA)` Update a Compute Engine organization firewall policy.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute firewall-policies
```

```
gcloud beta compute firewall-policies
```