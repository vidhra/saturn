# gcloud edge-cloud container clusters node-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/delete](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/delete)*

**NAME**

: **gcloud edge-cloud container clusters node-pools delete - delete an Edge Container nodePool**

**SYNOPSIS**

: **`gcloud edge-cloud container clusters node-pools delete` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/delete#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/delete#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an Edge Container nodePool.

**EXAMPLES**

: To delete a nodePool called 'my-nodePool' in region us-central1, run:

```
gcloud edge-cloud container clusters node-pools delete my-nodePool --cluster=<my-cluster> --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Node pool resource - Edge Container nodePool to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_POOL`**:
ID of the node pool or fully qualified identifier for the node pool.
To set the `node_pool` attribute:

- provide the argument `node_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
Kubernetes cluster.
To set the `cluster` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--location**:
The global location name.
To set the `location` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `edge_container/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `edgecontainer/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/edge-cloud](https://cloud.google.com/edge-cloud)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud container clusters node-pools delete
```