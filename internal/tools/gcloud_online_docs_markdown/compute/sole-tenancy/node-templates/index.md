# gcloud compute sole-tenancy node-templates  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates)*

**NAME**

: **gcloud compute sole-tenancy node-templates - read and manage Compute Engine sole-tenancy node templates**

**SYNOPSIS**

: **`gcloud compute sole-tenancy node-templates` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Node templates are used to create the nodes in node groups. Nodes are Compute
Engine servers that are dedicated to your workload. Node templates define either
the node type or the requirements for a node in terms of vCPU, memory, and
localSSD.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/add-iam-policy-binding)`**:
Add IAM policy binding to a Compute Engine node template.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create)`**:
Create a Compute Engine node template.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/delete)`**:
Delete a Compute Engine node template.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/describe)`**:
Describe a Compute Engine node template.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/get-iam-policy)`**:
Get the IAM Policy for a Compute Engine node template.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/list)`**:
List Google Compute Engine node templates.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/remove-iam-policy-binding)`**:
Remove IAM policy binding from a Compute Engine node template.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/set-iam-policy)`**:
Set the IAM policy for a Compute Engine node template.

**NOTES**

: These variants are also available:

```
gcloud alpha compute sole-tenancy node-templates
```

```
gcloud beta compute sole-tenancy node-templates
```