# gcloud container hub scopes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes)*

**NAME**

: **gcloud container hub scopes - manage scopes of all your GKE fleets**

**SYNOPSIS**

: **`gcloud container hub scopes` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage scopes of all your GKE fleets.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[namespaces](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces)`**:
Fleet namespaces are the fleet equivalent of k8s cluster namespaces.

**`[rbacrolebindings](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings)`**:
Fleet scope RBAC RoleBindings for permissions.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/add-iam-policy-binding)`**:
Add IAM policy binding to a Fleet Scope.

**`[create](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create)`**:
Create a new fleet scope.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/delete)`**:
Delete a fleet scope.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/describe)`**:
Describe a fleet scope.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/get-iam-policy)`**:
Get the IAM policy for a Fleet Scope.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/list)`**:
List fleet scopes in a project permitted to be viewed by the caller.

**`[list-memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/list-memberships)`**:
List memberships bound to a fleet scope.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/remove-iam-policy-binding)`**:
Remove IAM policy binding of a Fleet Scope.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update)`**:
Update a scope.

**NOTES**

: These variants are also available:

```
gcloud alpha container hub scopes
```

```
gcloud beta container hub scopes
```