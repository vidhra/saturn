# gcloud container hub  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub](https://cloud.google.com/sdk/gcloud/reference/container/hub)*

**NAME**

: **gcloud container hub - centrally manage features and services on all your Kubernetes clusters with fleet**

**SYNOPSIS**

: **`gcloud container hub` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/container/hub#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/hub#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The command group to register GKE or other Kubernetes clusters running in a
variety of environments, including Google cloud, on premises in customer
datacenters, or other third party clouds with fleet. Fleet provides a
centralized control-plane to managed features and services on all registered
clusters.
A registered cluster is always associated with a Membership, a resource within
fleet.

**EXAMPLES**

: Manage memberships of all your GKE and other Kubernetes clusters with fleet:

```
gcloud container hub memberships --help
```

Manage Config Management feature on all memberships:

```
gcloud container hub config-management --help
```

Manage Multi-cluster Ingress feature on all memberships:

```
gcloud container hub ingress --help
```

Manage Multi-cluster Services feature on all memberships:

```
gcloud container hub multi-cluster-services --help
```

Manage CloudRun feature on all memberships:

```
gcloud container hub cloudrun --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[cloudrun](https://cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun)`**:
Manage the CloudRun feature.

**`[clusterupgrade](https://cloud.google.com/sdk/gcloud/reference/container/hub/clusterupgrade)`**:
Configure the Fleet clusterupgrade feature.

**`[dataplane-v2-encryption](https://cloud.google.com/sdk/gcloud/reference/container/hub/dataplane-v2-encryption)`**:
Manage Dataplane V2 Encryption Feature.

**`[features](https://cloud.google.com/sdk/gcloud/reference/container/hub/features)`**:
Manage Hub Feature resources.

**`[fleetobservability](https://cloud.google.com/sdk/gcloud/reference/container/hub/fleetobservability)`**:
Manage Fleet Observability Feature.

**`[identity-service](https://cloud.google.com/sdk/gcloud/reference/container/hub/identity-service)`**:
Manage Identity Service Feature.

**`[ingress](https://cloud.google.com/sdk/gcloud/reference/container/hub/ingress)`**:
Manage Multi-cluster Ingress Feature.

**`[memberships](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships)`**:
Manage memberships of all your GKE and other Kubernetes clusters with fleets.

**`[mesh](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh)`**:
Manage Service Mesh Feature.

**`[multi-cluster-services](https://cloud.google.com/sdk/gcloud/reference/container/hub/multi-cluster-services)`**:
Manage Multi-cluster Services Feature.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/container/hub/operations)`**:
Manage Anthos fleet long-running operations.

**`[policycontroller](https://cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller)`**:
Manage Policy Controller Feature.

**`[scopes](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes)`**:
Manage scopes of all your GKE fleets.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/container/hub/create)`**:
Create a fleet.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/hub/delete)`**:
Delete a fleet.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/hub/describe)`**:
Show fleet info.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/hub/list)`**:
List fleets visible to the user in an organization.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/hub/update)`**:
Update a fleet.

**NOTES**

: These variants are also available:

```
gcloud alpha container hub
```

```
gcloud beta container hub
```