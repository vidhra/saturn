# gcloud container node-pools get-upgrade-info  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info)*

**NAME**

: **gcloud container node-pools get-upgrade-info - get upgrade information for an existing node pool for a cluster**

**SYNOPSIS**

: **`gcloud container node-pools get-upgrade-info` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#NAME)` [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#--cluster)`=`CLUSTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud container node-pools get-upgrade-info` displays all upgrade
information associated with the node pool in the Google Kubernetes Engine
cluster.

**EXAMPLES**

: To get upgrade information for a node pool of an existing cluster, run:

```
gcloud container node-pools get-upgrade-info node-pool-1 --cluster=sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the node pool.

**FLAGS**

: **--cluster**:
The name of the cluster. Overrides the default `container/cluster`
property value for this command invocation.

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
gcloud alpha container node-pools get-upgrade-info
```

```
gcloud beta container node-pools get-upgrade-info
```