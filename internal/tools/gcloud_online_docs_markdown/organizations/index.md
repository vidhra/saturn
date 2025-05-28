# gcloud organizations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/organizations](https://cloud.google.com/sdk/gcloud/reference/organizations)*

**NAME**

: **gcloud organizations - create and manage Google Cloud Platform Organizations**

**SYNOPSIS**

: **`gcloud organizations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/organizations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/organizations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud organizations group lets you create and manage Cloud Organizations.
Google Cloud Platform resources form a hierarchy with Organizations at the root.
Organizations contain projects, and Projects contain the remaining Google Cloud
Platform resources.
More information on the Cloud Platform Resource Hierarchy and the Organization
resource can be found here: [https://cloud.google.com/resource-manager/docs/creating-managing-organization](https://cloud.google.com/resource-manager/docs/creating-managing-organization)
and detailed documentation on creating and managing organizations can be found
here: [https://cloud.google.com/resource-manager/docs/creating-managing-organization](https://cloud.google.com/resource-manager/docs/creating-managing-organization)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding)`**:
Add IAM policy binding for an organization.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/organizations/describe)`**:
Show metadata for an organization.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy)`**:
Get IAM policy for an organization.

**`[list](https://cloud.google.com/sdk/gcloud/reference/organizations/list)`**:
List organizations accessible by the active account.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/organizations/remove-iam-policy-binding)`**:
Remove IAM policy binding for an organization.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/organizations/set-iam-policy)`**:
Set IAM policy for an organization.

**NOTES**

: These variants are also available:

```
gcloud alpha organizations
```

```
gcloud beta organizations
```