# gcloud container fleet memberships  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships)*

**NAME**

: **gcloud container fleet memberships - manage memberships of all your GKE and other Kubernetes clusters with fleets**

**SYNOPSIS**

: **`gcloud container fleet memberships` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage memberships of all your GKE and other Kubernetes clusters with fleets.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[bindings](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/bindings)`**:
Membership Bindings for permissions.

**`[support-access](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/support-access)`**:
Membership used for support access.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete)`**:
Delete a membership.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/describe)`**:
Describe a membership.

**`[generate-gateway-rbac](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac)`**:
Generate RBAC policy files for connected clusters by the user.

**`[get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/get-credentials)`**:
Fetch credentials for a fleet-registered cluster to be used in Connect Gateway.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/list)`**:
List memberships.

**`[register](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/register)`**:
Register a cluster with a fleet.

**`[unregister](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister)`**:
Unregister a cluster from a fleet.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/update)`**:
Update a membership.

**NOTES**

: These variants are also available:

```
gcloud alpha container fleet memberships
```

```
gcloud beta container fleet memberships
```