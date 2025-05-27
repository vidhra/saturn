# gcloud container hub memberships register  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register)*

**NAME**

: **gcloud container hub memberships register - register a cluster with a fleet**

**SYNOPSIS**

: **`gcloud container hub memberships register` (`[MEMBERSHIP_NAME](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#MEMBERSHIP_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--location)`=`LOCATION`) (`[--gke-cluster](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--gke-cluster)`=`LOCATION`/`[CLUSTER_NAME](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#CLUSTER_NAME)`     | `[--gke-uri](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--gke-uri)`=`GKE_URI`     | [`[--context](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--context)`=`CONTEXT` : `[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--kubeconfig)`=`KUBECONFIG`]) [`[--install-connect-agent](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--install-connect-agent)`] [`[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--internal-ip)`] [`[--manifest-output-file](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--manifest-output-file)`=`MANIFEST_OUTPUT_FILE`] [`[--proxy](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--proxy)`=`PROXY`] [`[--service-account-key-file](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--service-account-key-file)`=`SERVICE_ACCOUNT_KEY_FILE`     | [`[--enable-workload-identity](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--enable-workload-identity)` : `[--has-private-issuer](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--has-private-issuer)` | `[--public-issuer-url](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#--public-issuer-url)`=`PUBLIC_ISSUER_URL`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/register#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command registers a cluster with the fleet by:

```
1. Creating a Fleet Membership resource corresponding to the cluster.
2. Adding in-cluster Kubernetes Resources that make the cluster exclusive
   to one fleet.
3. Installing the Connect agent into this cluster (optional for GKE).
```

A successful registration implies that the cluster is now exclusive to a single
Fleet. If the cluster is already registered to another Fleet, the registration
will not be successful.
To register a GKE cluster, use `--gke-cluster` or
`--gke-uri` flag (no `--kubeconfig` flag is required).
Connect agent will not be installed by default for GKE clusters. To install it,
specify `--install-connect-agent`. The default value for
`--location` is the same as the cluster's region or zone, can be
specified as `global`.
Anthos clusters on VMware, bare metal, AWS, and Azure are registered with a
fleet when the clusters are created. To register Amazon EKS clusters, see [Attach
your EKS cluster](https://cloud.google.com/anthos/clusters/docs/multi-cloud/attached/eks/how-to/attach-cluster). To regiser Microsoft Azure clusters, see [Attach
your AKS cluster](https://cloud.google.com/anthos/clusters/docs/multi-cloud/attached/aks/how-to/attach-cluster).
To register a third-party cluster, use --context flag (with an optional
--kubeconfig flag). Connect agent will always be installed for these clusters.
If Connect agent is to be installed, its authentication needs to be configured
by `--enable-workload-identity` or
`--service-account-key-file`. For the latter case, the corresponding
service account must have been granted `gkehub.connect` permissions.
For more information about Connect agent, go to: [https://cloud.google.com/anthos/multicluster-management/connect/overview/](https://cloud.google.com/anthos/multicluster-management/connect/overview/)
Rerunning this command against the same cluster with the same MEMBERSHIP_NAME
and target fleet is successful, and will upgrade the Connect agent if it is
supposed to be installed and a newer version is available. Rerunning with
`--enable-workload-identity` ensures that Workload Identity is
enabled on the cluster.

**EXAMPLES**

: Register a non-GKE cluster referenced from a specific kubeconfig file, and
install the Connect agent:

```
gcloud container hub memberships register my-cluster --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --service-account-key-file=/tmp/keyfile.json
```

Register a non-GKE cluster referenced from the default kubeconfig file, and
install the Connect agent:

```
gcloud container hub memberships register my-cluster --context=my-cluster-context --service-account-key-file=/tmp/keyfile.json
```

Register a non-GKE cluster, and install a specific version of the Connect agent:

```
gcloud container hub memberships register my-cluster --context=my-cluster-context --version=gkeconnect_20190802_02_00 --service-account-key-file=/tmp/keyfile.json
```

Register a non-GKE cluster and output a manifest that can be used to install the
Connect agent by kubectl:

```
gcloud container hub memberships register my-cluster --context=my-cluster-context --manifest-output-file=/tmp/manifest.yaml --service-account-key-file=/tmp/keyfile.json
```

Register a GKE cluster referenced from a GKE URI:

```
gcloud container hub memberships register my-cluster --gke-uri=my-cluster-gke-uri
```

Register a GKE cluster referenced from a GKE URI, and install the Connect agent
using service account key file:

```
gcloud container hub memberships register my-cluster --gke-uri=my-cluster-gke-uri --install-connect-agent --service-account-key-file=/tmp/keyfile.json
```

Register a GKE cluster and output a manifest that can be used to install the
Connect agent by kubectl:

```
gcloud container hub memberships register my-cluster --gke-uri=my-cluster-gke-uri --enable-workload-identity --install-connect-agent --manifest-output-file=/tmp/manifest.yaml
```

Register a GKE cluster first, and install the Connect agent later.

```
gcloud container hub memberships register my-cluster --gke-cluster=my-cluster-region-or-zone/my-cluster
```

```
gcloud container hub memberships register my-cluster --gke-cluster=my-cluster-region-or-zone/my-cluster --install-connect-agent --enable-workload-identity
```

Register a GKE cluster, and install a specific version of the Connect agent:

```
gcloud container hub memberships register my-cluster --gke-cluster=my-cluster-region-or-zone/my-cluster --install-connect-agent --version=20220819-00-00 --service-account-key-file=/tmp/keyfile.json
```

Register a GKE cluster and output a manifest that can be used to install the
Connect agent:

```
gcloud container hub memberships register my-cluster --gke-uri=my-cluster-gke-uri --install-connect-agent --manifest-output-file=/tmp/manifest.yaml --service-account-key-file=/tmp/keyfile.json
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
The location for the membership resource, e.g. `us-central1`. If not
specified, defaults to `global`. Not supported for GKE clusters,
whose membership location will be the location of the cluster.
To set the `location` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `gkehub/location`.**

**REQUIRED FLAGS**

: **--gke-cluster**

**OPTIONAL FLAGS**

: **--install-connect-agent**:
If set to True for a GKE cluster, Connect agent will be installed in the
cluster. No-op for Non-GKE clusters, where Connect agent will always be
installed.

**--internal-ip**:
Whether to use the internal IP address of the cluster endpoint.

**--manifest-output-file**:
The full path of the file into which the Connect agent installation manifest
should be stored. If this option is provided, then the manifest will be written
to this file and will not be deployed into the cluster by gcloud, and it will
need to be deployed manually.

**--proxy**:
The proxy address in the format of http[s]://{hostname}. The proxy must support
the HTTP CONNECT method in order for this connection to succeed.

**--service-account-key-file**

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
gcloud alpha container hub memberships register
```

```
gcloud beta container hub memberships register
```