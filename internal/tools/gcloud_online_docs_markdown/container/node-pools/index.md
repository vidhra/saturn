# gcloud container node-pools  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/node-pools](https://cloud.google.com/sdk/gcloud/reference/container/node-pools)*

**NAME**

: **gcloud container node-pools - create and delete operations for Google Kubernetes Engine node pools**

**SYNOPSIS**

: **`gcloud container node-pools` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/container/node-pools#COMMAND)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/node-pools#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/node-pools#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/node-pools#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/node-pools#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and delete operations for Google Kubernetes Engine node pools.

**FLAGS**

: **--location**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[complete-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade)`**:
Complete a node pool upgrade.

**`[create](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create)`**:
Create a node pool in a running cluster.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete)`**:
Delete an existing node pool in a running cluster.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/describe)`**:
Describe an existing node pool for a cluster.

**`[get-upgrade-info](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info)`**:
Get upgrade information for an existing node pool for a cluster.

**`[list](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/list)`**:
List existing node pools for a cluster.

**`[rollback](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback)`**:
Rollback a node-pool upgrade.

**`[update](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update)`**:
Updates a node pool in a running cluster.

**NOTES**

: These variants are also available:

```
gcloud alpha container node-pools
```

```
gcloud beta container node-pools
```