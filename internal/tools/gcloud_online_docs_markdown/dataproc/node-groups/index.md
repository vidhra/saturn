# gcloud dataproc node-groups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups)*

**NAME**

: **gcloud dataproc node-groups - manage Dataproc node groups**

**SYNOPSIS**

: **`gcloud dataproc node-groups` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage and modify Dataproc node groups created with a parent cluster.

**EXAMPLES**

: To describe a node group:

```
gcloud dataproc node-groups describe NODE_GROUP_ID --cluster cluster_name --region region
```

To resize a node group:

```
gcloud dataproc node-groups resize NODE_GROUP_ID --cluster cluster_name --region region --size new_size
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/describe)`**:
Describe the node group.

**`[resize](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups/resize)`**:
Resize the number of nodes in the node group.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc node-groups
```

```
gcloud beta dataproc node-groups
```