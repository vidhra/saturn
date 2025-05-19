# gcloud container clusters delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete)*

**NAME**

: **gcloud container clusters delete - delete an existing cluster for running containers**

**SYNOPSIS**

: **`gcloud container clusters delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#NAME)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#--async)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: When you delete a cluster, the following resources are deleted:

- The control plane resources
- All of the node instances in the cluster
- Any Pods that are running on those instances
- Any firewalls and routes created by Kubernetes Engine at the time of cluster
creation
- Data stored in host hostPath and emptyDir volumes

GKE will attempt to delete the following resources. Deletion of these resources
is not always guaranteed:

- External load balancers created by the cluster
- Internal load balancers created by the cluster
- Persistent disk volumes

**EXAMPLES**

: To delete an existing cluster, run:

```
gcloud container clusters delete sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
The names of the clusters to delete.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha container clusters delete
```

```
gcloud beta container clusters delete
```