# gcloud org-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/org-policies](https://cloud.google.com/sdk/gcloud/reference/org-policies)*

**NAME**

: **gcloud org-policies - create and manage Organization Policies**

**SYNOPSIS**

: **`gcloud org-policies` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/org-policies#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/org-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud org-policies command group lets you create and manipulate
Organization Policies.
The Organization Policy Service gives you centralized and programmatic control
over your organization's cloud resources. As the organization policy
administrator, you will be able to configure restrictions across your entire
resource hierarchy.
More information on Organization Policies can be found here: [https://cloud.google.com/resource-manager/docs/organization-policy/overview](https://cloud.google.com/resource-manager/docs/organization-policy/overview)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/org-policies/delete)`**:
Delete an organization policy.

**`[delete-custom-constraint](https://cloud.google.com/sdk/gcloud/reference/org-policies/delete-custom-constraint)`**:
Deletes a custom constraint.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe)`**:
Describe an organization policy.

**`[describe-custom-constraint](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint)`**:
Describe a custom constraint.

**`[list](https://cloud.google.com/sdk/gcloud/reference/org-policies/list)`**:
List the policies set on a resource.

**`[list-custom-constraints](https://cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints)`**:
Lists the custom constraints set on an organization.

**`[reset](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset)`**:
Reset the policy to the default for the constraint.

**`[set-custom-constraint](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint)`**:
Set a custom constraint from a JSON or YAML file.

**`[set-policy](https://cloud.google.com/sdk/gcloud/reference/org-policies/set-policy)`**:
Set an organization policy from a JSON or YAML file.