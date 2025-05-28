# gcloud compute sole-tenancy node-groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update)*

**NAME**

: **gcloud compute sole-tenancy node-groups update - update a Compute Engine node group**

**SYNOPSIS**

: **`gcloud compute sole-tenancy node-groups update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#NAME)` [`[--node-template](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--node-template)`=`NODE_TEMPLATE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--zone)`=`ZONE`] [`[--add-nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--add-nodes)`=`ADD_NODES`     | `[--delete-nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--delete-nodes)`=[`NODE`,…]] [`[--autoscaler-mode](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--autoscaler-mode)`=`AUTOSCALER_MODE` `[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--min-nodes)`=`MIN_NODES`] [`[--share-setting](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--share-setting)`=`SHARE_SETTING` : `[--share-with](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#--share-with)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#PROJECT)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Compute Engine node group.

**EXAMPLES**

: To update a node group to have two more nodes, run:

```
gcloud compute sole-tenancy node-groups update my-node-group --add-nodes=2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the node group to operate on.

**FLAGS**

: **--node-template**:
The name of the node template resource to be set for this node group.

**--zone**:
Zone of the node group to operate on. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

**--add-nodes**

**--autoscaler-mode**

**--share-setting**

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
gcloud alpha compute sole-tenancy node-groups update
```

```
gcloud beta compute sole-tenancy node-groups update
```