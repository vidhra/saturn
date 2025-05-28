# gcloud workstations clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create)*

**NAME**

: **gcloud workstations clusters create - create a workstation cluster**

**SYNOPSIS**

: **`gcloud workstations clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--async)`] [`[--domain](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--domain)`=`DOMAIN`] [`[--enable-private-endpoint](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--enable-private-endpoint)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--network)`=`NETWORK`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--subnetwork)`=`SUBNETWORK`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#--tags)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a workstation cluster.

**EXAMPLES**

: To create a public cluster `my-cluster` in region
`us-central1`, run:

```
gcloud workstations clusters create my-cluster --region=us-central1
```

To create a private cluster 'my-private-cluster' associated with network
'my-network' and subnetwork 'my-subnetwork'. run:

```
gcloud workstations clusters create my-private-cluster --region=us-central1 --enable-private-endpoint --network='my-network' --subnetwork='my-subnetwork'
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Arguments and flags that specify the cluster to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the region of the cluster.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `workstations/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--domain**:
Domain used by Workstations for HTTP ingress.

**--enable-private-endpoint**:
Default is false. If specified, the cluster will be assigned an internal IP
address to the Cluster Gateway. This isolates the cluster's workstations from
public networks, but requires additional configuration. Learn more: [https://cloud.google.com/workstations/docs](https://cloud.google.com/workstations/docs).

**--labels**:
Labels that are applied to the cluster and propagated to the underlying Compute
Engine resources.

**--network**:
Fully specified network path for instances created in this cluster.

**--subnetwork**:
Fully specified subnetwork path for instances created in this cluster.

**--tags**:
Resource manager tags to be bound to this cluster. For example:
"123/environment=production" "123/costCenter=marketing"

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

**API REFERENCE**

: This command uses the `workstations/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/workstations](https://cloud.google.com/workstations)

**NOTES**

: These variants are also available:

```
gcloud alpha workstations clusters create
```

```
gcloud beta workstations clusters create
```