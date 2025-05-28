# gcloud container fleet  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet](https://cloud.google.com/sdk/gcloud/reference/container/fleet)*

**NAME**

: **gcloud container fleet - centrally manage features and services on all your Kubernetes clusters with fleet**

**SYNOPSIS**

: **`gcloud container fleet` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/container/fleet#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/fleet#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet#GCLOUD-WIDE-FLAGS) …`]**

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
gcloud container fleet memberships --help
```

Manage Config Management feature on all memberships:

```
gcloud container fleet config-management --help
```

Manage Multi-cluster Ingress feature on all memberships:

```
gcloud container fleet ingress --help
```

Manage Multi-cluster Services feature on all memberships:

```
gcloud container fleet multi-cluster-services --help
```

Manage CloudRun feature on all memberships:

```
gcloud container fleet cloudrun --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[cloudrun](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun)`**:
Manage the CloudRun feature.

**`[clusterupgrade](https://cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade)`**:
Configure the Fleet clusterupgrade feature.

**`[dataplane-v2-encryption](https://cloud.google.com/sdk/gcloud/reference/container/fleet/dataplane-v2-encryption)`**:
Manage Dataplane V2 Encryption Feature.

**`[features](https://cloud.google.com/sdk/gcloud/reference/container/fleet/features)`**:
Manage Hub Feature resources.

**`[fleetobservability](https://cloud.google.com/sdk/gcloud/reference/container/fleet/fleetobservability)`**:
Manage Fleet Observability Feature.

**`[identity-service](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service)`**:
Manage Identity Service Feature.

**`[ingress](https://cloud.google.com/sdk/gcloud/reference/container/fleet/ingress)`**:
Manage Multi-cluster Ingress Feature.

**`[memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships)`**:
Manage memberships of all your GKE and other Kubernetes clusters with fleets.

**`[mesh](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh)`**:
Manage Service Mesh Feature.

**`[multi-cluster-services](https://cloud.google.com/sdk/gcloud/reference/container/fleet/multi-cluster-services)`**:
Manage Multi-cluster Services Feature.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/container/fleet/operations)`**:
Manage Anthos fleet long-running operations.

**`[policycontroller](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller)`**:
Manage Policy Controller Feature.

**`[scopes](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes)`**:
Manage scopes of all your GKE fleets.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/container/fleet/create)`**:
Create a fleet.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/fleet/delete)`**:
Delete a fleet.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/fleet/describe)`**:
Show fleet info.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/fleet/list)`**:
List fleets visible to the user in an organization.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/fleet/update)`**:
Update a fleet.

**NOTES**

: These variants are also available:

```
gcloud alpha container fleet
```

```
gcloud beta container fleet
```