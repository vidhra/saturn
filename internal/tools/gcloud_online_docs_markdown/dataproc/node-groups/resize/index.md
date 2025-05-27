# gcloud dataproc node-groups resize  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize)*

**NAME**

: **gcloud dataproc node-groups resize - resize the number of nodes in the node group**

**SYNOPSIS**

: **`gcloud dataproc node-groups resize` (`[NODE_GROUP](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize#NODE_GROUP)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize#--region)`=`REGION`) `[--size](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize#--size)`=`SIZE` [`[--graceful-decommission-timeout](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize#--graceful-decommission-timeout)`=`GRACEFUL_DECOMMISSION_TIMEOUT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resize the number of nodes in the node group.

**EXAMPLES**

: To resize a node group, run:

```
gcloud dataproc node-groups resize my-node-group-id --region=us-central1 --cluster=my-cluster-name --size=5
```

**POSITIONAL ARGUMENTS**

: **Node group resource - ID of the node group to resize. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_group` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_GROUP`**:
ID of the node_group or fully qualified identifier for the node_group.
To set the `node_group` attribute:

- provide the argument `node_group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The Cluster name.
To set the `cluster` attribute:

- provide the argument `node_group` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--region**:
Dataproc region for the node_group. Each Dataproc region constitutes an
independent resource namespace constrained to deploying instances into Compute
Engine zones inside the region. Overrides the default
`dataproc/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `node_group` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**REQUIRED FLAGS**

: **--size**:
New size for a node group.

**OPTIONAL FLAGS**

: **--graceful-decommission-timeout**:
Graceful decommission timeout for a node group scale-down resize.

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
gcloud alpha dataproc node-groups resize
```

```
gcloud beta dataproc node-groups resize
```