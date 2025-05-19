# gcloud alpha compute instance-templates  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates)*

**NAME**

: **gcloud alpha compute instance-templates - read and manipulate Compute Engine instances templates**

**SYNOPSIS**

: **`gcloud alpha compute instance-templates` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Lists, creates, deletes, and modifies Compute Engine
instance templates.
For more information about instance templates, see the [instances
templates documentation](https://cloud.google.com/compute/docs/instance-templates).
See also: [Instance
templates API](https://cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/add-iam-policy-binding)`**:
`(ALPHA)` Add IAM policy binding to a Compute Engine instance
template.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/create)`**:
`(ALPHA)` Create a Compute Engine virtual machine instance template.

**`[create-with-container](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/create-with-container)`**:
`(ALPHA)` Creates a Compute Engine a virtual machine instance
template that runs a Docker container.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/delete)`**:
`(ALPHA)` Delete Compute Engine virtual machine instance templates.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe)`**:
`(ALPHA)` Describe a virtual machine instance template.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/get-iam-policy)`**:
`(ALPHA)` Get the IAM policy for a Compute Engine instance template.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/list)`**:
`(ALPHA)` List Google Compute Engine instance templates.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/remove-iam-policy-binding)`**:
`(ALPHA)` Remove IAM policy binding from a Compute Engine instance
template.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/set-iam-policy)`**:
`(ALPHA)` Set the IAM policy for a Compute Engine instance template.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-templates
```

```
gcloud beta compute instance-templates
```