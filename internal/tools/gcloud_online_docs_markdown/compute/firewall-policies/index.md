# gcloud compute firewall-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies)*

**NAME**

: **gcloud compute firewall-policies - manage Compute Engine organization firewall policies**

**SYNOPSIS**

: **`gcloud compute firewall-policies` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Compute Engine organization firewall policies. Organization firewall
policies are used to control incoming/outgoing traffic.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[associations](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations)`**:
Read and manipulate Compute Engine organization firewall policy associations.

**`[rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules)`**:
Read and manipulate Compute Engine organization firewall policy rules.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[clone-rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules)`**:
Replace the rules of a Compute Engine organization firewall policy with rules
from another policy.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/create)`**:
Create a Compute Engine organization firewall policy.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/delete)`**:
Delete a Compute Engine organization firewall policy.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/describe)`**:
Describe a Compute Engine organization firewall policy.

**`[export-rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules)`**:
Export Compute Engine organization firewall policy rules.

**`[import-rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/import-rules)`**:
Import Compute Engine organization firewall policy rules.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/list)`**:
List Compute Engine organization firewall policies.

**`[list-rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/list-rules)`**:
List the rules of a Compute Engine organization firewall policy.

**`[move](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/move)`**:
Move a Compute Engine organization firewall policy.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/update)`**:
Update a Compute Engine organization firewall policy.

**NOTES**

: These variants are also available:

```
gcloud alpha compute firewall-policies
```

```
gcloud beta compute firewall-policies
```