# gcloud container node-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update)*

**NAME**

: **gcloud container node-pools update - updates a node pool in a running cluster**

**SYNOPSIS**

: **`gcloud container node-pools update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#NAME)` (`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--accelerator)`=[`type`=`TYPE`,[`count`=`COUNT`,`gpu-driver-version`=`GPU_DRIVER_VERSION`,`gpu-partition-size`=`GPU_PARTITION_SIZE`,`gpu-sharing-strategy`=`GPU_SHARING_STRATEGY`,`max-shared-clients-per-gpu`=`MAX_SHARED_CLIENTS_PER_GPU`],…]     | `[--confidential-node-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--confidential-node-type)`=`CONFIDENTIAL_NODE_TYPE`     | `[--containerd-config-from-file](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--containerd-config-from-file)`=`PATH_TO_FILE`     | `[--enable-confidential-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-confidential-nodes)`     | `[--enable-gvnic](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-gvnic)`     | `[--enable-image-streaming](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-image-streaming)`     | `[--enable-insecure-kubelet-readonly-port](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-insecure-kubelet-readonly-port)`     | `[--enable-private-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-private-nodes)`     | `[--enable-queued-provisioning](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-queued-provisioning)`     | `[--flex-start](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--flex-start)`     | `[--labels](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--labels)`=[`KEY`=`VALUE`,…]     | `[--logging-variant](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--logging-variant)`=`LOGGING_VARIANT`     | `[--max-run-duration](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--max-run-duration)`=`MAX_RUN_DURATION`     | `[--network-performance-configs](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--network-performance-configs)`=[`PROPERTY`=`VALUE`,…]     | `[--node-labels](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--node-labels)`=[`NODE_LABEL`,…]     | `[--node-locations](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--node-locations)`=`ZONE`,[`[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#ZONE)`,…]     | `[--node-taints](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--node-taints)`=[`NODE_TAINT`,…]     | `[--resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--resource-manager-tags)`=[`KEY`=`VALUE`,…]     | `[--storage-pools](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--storage-pools)`=`STORAGE_POOL`,[…]     | `[--system-config-from-file](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--system-config-from-file)`=`PATH_TO_FILE`     | `[--tags](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--tags)`=[`TAG`,…]     | `[--windows-os-version](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--windows-os-version)`=`WINDOWS_OS_VERSION`     | `[--workload-metadata](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--workload-metadata)`=`WORKLOAD_METADATA`     | `[--disk-size](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--disk-size)`=`DISK_SIZE` `[--disk-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--disk-type)`=`DISK_TYPE` `[--machine-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--machine-type)`=`MACHINE_TYPE`     | `[--enable-autoprovisioning](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-autoprovisioning)` `[--enable-autoscaling](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-autoscaling)` `[--location-policy](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--location-policy)`=`LOCATION_POLICY` `[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--min-nodes)`=`MIN_NODES` `[--total-max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--total-max-nodes)`=`TOTAL_MAX_NODES` `[--total-min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--total-min-nodes)`=`TOTAL_MIN_NODES`     | `[--enable-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-autorepair)` `[--enable-autoupgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-autoupgrade)`     | `[--enable-blue-green-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-blue-green-upgrade)` `[--enable-surge-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-surge-upgrade)` `[--max-surge-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--max-surge-upgrade)`=`MAX_SURGE_UPGRADE` `[--max-unavailable-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--max-unavailable-upgrade)`=`MAX_UNAVAILABLE_UPGRADE` `[--node-pool-soak-duration](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--node-pool-soak-duration)`=`NODE_POOL_SOAK_DURATION` `[--standard-rollout-policy](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--standard-rollout-policy)`=[`batch-node-count`=`BATCH_NODE_COUNT`,`batch-percent`=`BATCH_NODE_PERCENTAGE`,`batch-soak-duration`=`BATCH_SOAK_DURATION`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--async)`] [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--cluster)`=`CLUSTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud container node-pools update` updates a node pool in a Google
Kubernetes Engine cluster.

**EXAMPLES**

: To turn on node autoupgrade in "node-pool-1" in the cluster "sample-cluster",
run:

```
gcloud container node-pools update node-pool-1 --cluster=sample-cluster --enable-autoupgrade
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the node pool.

**REQUIRED FLAGS**

: **--accelerator**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster**:
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
gcloud alpha container node-pools update
```

```
gcloud beta container node-pools update
```