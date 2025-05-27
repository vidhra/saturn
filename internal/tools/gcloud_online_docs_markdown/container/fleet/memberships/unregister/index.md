# gcloud container fleet memberships unregister  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister)*

**NAME**

: **gcloud container fleet memberships unregister - unregister a cluster from a fleet**

**SYNOPSIS**

: **`gcloud container fleet memberships unregister` (`[MEMBERSHIP_NAME](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#MEMBERSHIP_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#--location)`=`LOCATION`) (`[--gke-cluster](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#--gke-cluster)`=`LOCATION`/`[CLUSTER_NAME](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#CLUSTER_NAME)`     | `[--gke-uri](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#--gke-uri)`=`GKE_URI`     | [`[--context](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#--context)`=`CONTEXT` : `[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#--kubeconfig)`=`KUBECONFIG`]) [`[--uninstall-connect-agent](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#--uninstall-connect-agent)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command unregisters a cluster with the fleet by:

```
1. Deleting the Fleet Membership resource for this cluster (a.k.a
   `gcloud container fleet memberships delete`).
2. Removing the corresponding in-cluster Kubernetes Resources that make the
   cluster exclusive to one fleet (a.k.a `kubectl delete memberships
   membership`).
3. [Optional for GKE cluster] Uninstalling the Connect agent from this
   cluster (a.k.a `kubectl delete on the gke-connect namespace`).
```

The unregister command makes additional internal checks to ensure that all three
steps can be safely done to properly clean-up in-Fleet and in-cluster resources.
To unregister a GKE cluster use `--gke-cluster` or
`--gke-uri` flag (no `--kubeconfig` flag is required).
To unregister a third-party cluster use `--context` flag (with an
optional -`-kubeconfig`s flag).
To only delete the Fleet Membership resource, consider using the command:`[gcloud
container fleet memberships delete](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete)`. This command is intended to delete
stale Fleet Membership resources as doing so on a fully registered cluster will
skip some of the steps above and orphan in-cluster resources and agent
connections to Google.`

**EXAMPLES**

: Unregister a third-party cluster referenced from a specific kubeconfig file:

```
gcloud container fleet memberships unregister my-membership --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig
```

Unregister a third-party cluster referenced from the default kubeconfig file:

```
gcloud container fleet memberships unregister my-membership --context=my-cluster-context
```

Unregister a GKE cluster referenced from a GKE URI:

```
gcloud container fleet memberships unregister my-membership --gke-uri=my-cluster-gke-uri
```

Unregister a GKE cluster referenced from a GKE Cluster location and name:

```
gcloud container fleet memberships unregister my-membership --gke-cluster=my-cluster-region-or-zone/my-cluster
```

Unregister a GKE cluster and uninstall Connect agent:

```
gcloud container fleet memberships unregister my-membership --gke-cluster=my-cluster-region-or-zone/my-cluster --uninstall-connect-agent
```

**POSITIONAL ARGUMENTS**

: **Membership resource - The group of arguments defining a membership. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MEMBERSHIP_NAME`**:
ID of the membership or fully qualified identifier for the membership.
To set the `membership` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the membership resource, e.g. `us-central1`. If not
specified, defaults to `global`.
To set the `location` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `gkehub/location`.**

**REQUIRED FLAGS**

: **--gke-cluster**

**OPTIONAL FLAGS**

: **--uninstall-connect-agent**:
If set to True for a GKE cluster, Connect agent will be uninstalled from the
cluster. No-op for third-party clusters, where Connect agent will always be
uninstalled.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha container fleet memberships unregister
```

```
gcloud beta container fleet memberships unregister
```