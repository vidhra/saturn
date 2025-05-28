# gcloud projects  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/projects](https://cloud.google.com/sdk/gcloud/reference/projects)*

**NAME**

: **gcloud projects - create and manage project access policies**

**SYNOPSIS**

: **`gcloud projects` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/projects#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/projects#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud projects group lets you create and manage IAM policies for projects
on the Google Cloud Platform. Resources are organized hierarchically and
assigned to a particular project. A Project resource is required to use Google
Cloud Platform, and forms the basis for creating, enabling and using all Cloud
Platform services, managing APIs, enabling billing, adding and removing
collaborators, and managing permissions.
More information on the Cloud Platform Resource Hierarchy and the project
resource can be found here: [https://cloud.google.com/resource-manager/docs/creating-managing-organization](https://cloud.google.com/resource-manager/docs/creating-managing-organization)
and detailed documentation on creating and managing projects can be found here:
[https://cloud.google.com/resource-manager/docs/creating-managing-projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)`**:
Add IAM policy binding for a project.

**`[create](https://cloud.google.com/sdk/gcloud/reference/projects/create)`**:
Create a new project.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/projects/delete)`**:
Delete a project.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/projects/describe)`**:
Show metadata for a project.

**`[get-ancestors](https://cloud.google.com/sdk/gcloud/reference/projects/get-ancestors)`**:
Get the ancestors for a project.

**`[get-ancestors-iam-policy](https://cloud.google.com/sdk/gcloud/reference/projects/get-ancestors-iam-policy)`**:
Get IAM policies for a project and its ancestors.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy)`**:
Get IAM policy for a project.

**`[list](https://cloud.google.com/sdk/gcloud/reference/projects/list)`**:
List projects accessible by the active account.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/projects/remove-iam-policy-binding)`**:
Remove IAM policy binding for a project.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy)`**:
Set IAM policy for a project.

**`[undelete](https://cloud.google.com/sdk/gcloud/reference/projects/undelete)`**:
Undelete a project.

**`[update](https://cloud.google.com/sdk/gcloud/reference/projects/update)`**:
Update the name of a project.

**NOTES**

: These variants are also available:

```
gcloud alpha projects
```

```
gcloud beta projects
```