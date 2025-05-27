# gcloud container fleet scopes namespaces  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces)*

**NAME**

: **gcloud container fleet scopes namespaces - fleet namespaces are the fleet equivalent of k8s cluster namespaces**

**SYNOPSIS**

: **`gcloud container fleet scopes namespaces` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command group allows for manipulation of fleet namespaces.

**EXAMPLES**

: Manage fleet namespaces:

```
gcloud container fleet scopes namespaces --help
```

Manage RBAC RoleBindings in a fleet namespace:

```
gcloud container fleet scopes namespaces rbacrolebindings --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces/create)`**:
Create a fleet namespace.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces/delete)`**:
Delete a fleet namespace.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces/describe)`**:
Show fleet namespace info.

**`[get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces/get-credentials)`**:
Fetch credentials for a membership with a particular namespace.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces/list)`**:
List fleet namespaces in a project.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces/update)`**:
Update a fleet namespace.

**NOTES**

: These variants are also available:

```
gcloud alpha container fleet scopes namespaces
```

```
gcloud beta container fleet scopes namespaces
```