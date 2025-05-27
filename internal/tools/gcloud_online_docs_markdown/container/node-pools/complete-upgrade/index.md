# gcloud container node-pools complete-upgrade  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade)*

**NAME**

: **gcloud container node-pools complete-upgrade - complete a node pool upgrade**

**SYNOPSIS**

: **`gcloud container node-pools complete-upgrade` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#NAME)` [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#--cluster)`=`CLUSTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Complete a node pool upgrade.
Complete upgrade is a method used to skip the remaining node pool soaking phase
during blue-green node pool upgrades.

**EXAMPLES**

: To complete an active upgrade in
``node-pool-1`` in the cluster
``sample-cluster``, run:

```
gcloud container node-pools complete-upgrade node-pool-1 --cluster=sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the node pool for which the upgrade is to be completed.

**FLAGS**

: **--cluster**:
Cluster to which the node pool belongs. Overrides the default
`container/cluster` property value for this command invocation.

**--location**

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
gcloud alpha container node-pools complete-upgrade
```

```
gcloud beta container node-pools complete-upgrade
```