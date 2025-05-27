# gcloud container hub memberships  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships)*

**NAME**

: **gcloud container hub memberships - manage memberships of all your GKE and other Kubernetes clusters with fleets**

**SYNOPSIS**

: **`gcloud container hub memberships` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage memberships of all your GKE and other Kubernetes clusters with fleets.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[bindings](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings)`**:
Membership Bindings for permissions.

**`[support-access](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/support-access)`**:
Membership used for support access.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/delete)`**:
Delete a membership.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/describe)`**:
Describe a membership.

**`[generate-gateway-rbac](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/generate-gateway-rbac)`**:
Generate RBAC policy files for connected clusters by the user.

**`[get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/get-credentials)`**:
Fetch credentials for a fleet-registered cluster to be used in Connect Gateway.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/list)`**:
List memberships.

**`[register](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register)`**:
Register a cluster with a fleet.

**`[unregister](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/unregister)`**:
Unregister a cluster from a fleet.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/update)`**:
Update a membership.

**NOTES**

: These variants are also available:

```
gcloud alpha container hub memberships
```

```
gcloud beta container hub memberships
```