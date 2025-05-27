# gcloud container node-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create)*

**NAME**

: **gcloud container node-pools create - create a node pool in a running cluster**

**SYNOPSIS**

: **`gcloud container node-pools create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#NAME)` [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--accelerator)`=[`type`=`TYPE`,[`count`=`COUNT`,`gpu-driver-version`=`GPU_DRIVER_VERSION`,`gpu-partition-size`=`GPU_PARTITION_SIZE`,`gpu-sharing-strategy`=`GPU_SHARING_STRATEGY`,`max-shared-clients-per-gpu`=`MAX_SHARED_CLIENTS_PER_GPU`],…]] [`[--additional-node-network](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--additional-node-network)`=[`network`=`NETWORK_NAME`,`subnetwork`=`SUBNETWORK_NAME`,…]] [`[--additional-pod-network](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--additional-pod-network)`=[`subnetwork`=`SUBNETWORK_NAME`,`pod-ipv4-range`=`SECONDARY_RANGE_NAME`,[`max-pods-per-node`=`NUM_PODS`],…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--async)`] [`[--boot-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--boot-disk-kms-key)`=`BOOT_DISK_KMS_KEY`] [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--cluster)`=`CLUSTER`] [`[--confidential-node-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--confidential-node-type)`=`CONFIDENTIAL_NODE_TYPE`] [`[--containerd-config-from-file](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--containerd-config-from-file)`=`PATH_TO_FILE`] [`[--data-cache-count](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--data-cache-count)`=`DATA_CACHE_COUNT`] [`[--disk-size](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--disk-size)`=`DISK_SIZE`] [`[--disk-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--disk-type)`=`DISK_TYPE`] [`[--enable-autoprovisioning](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-autoprovisioning)`] [`[--enable-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-autorepair)`] [`[--no-enable-autoupgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-autoupgrade)`] [`[--enable-blue-green-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-blue-green-upgrade)`] [`[--enable-confidential-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-confidential-nodes)`] [`[--enable-confidential-storage](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-confidential-storage)`] [`[--enable-gvnic](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-gvnic)`] [`[--enable-image-streaming](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-image-streaming)`] [`[--enable-insecure-kubelet-readonly-port](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-insecure-kubelet-readonly-port)`] [`[--enable-nested-virtualization](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-nested-virtualization)`] [`[--enable-private-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-private-nodes)`] [`[--enable-queued-provisioning](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-queued-provisioning)`] [`[--enable-surge-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-surge-upgrade)`] [`[--flex-start](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--flex-start)`] [`[--image-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--image-type)`=`IMAGE_TYPE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--logging-variant](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--logging-variant)`=`LOGGING_VARIANT`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--machine-type)`=`MACHINE_TYPE`, `[-m](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#-m)` `[MACHINE_TYPE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#MACHINE_TYPE)`] [`[--max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-pods-per-node)`=`MAX_PODS_PER_NODE`] [`[--max-run-duration](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-run-duration)`=`MAX_RUN_DURATION`] [`[--max-surge-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-surge-upgrade)`=`MAX_SURGE_UPGRADE`; default=1] [`[--max-unavailable-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-unavailable-upgrade)`=`MAX_UNAVAILABLE_UPGRADE`] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#KEY)`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--metadata-from-file)`=`KEY`=`LOCAL_FILE_PATH`,[…]] [`[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--min-cpu-platform)`=`PLATFORM`] [`[--network-performance-configs](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--network-performance-configs)`=[`PROPERTY`=`VALUE`,…]] [`[--node-group](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-group)`=`NODE_GROUP`] [`[--node-labels](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-labels)`=[`NODE_LABEL`,…]] [`[--node-locations](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-locations)`=`ZONE`,[`[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#ZONE)`,…]] [`[--node-pool-soak-duration](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-pool-soak-duration)`=`NODE_POOL_SOAK_DURATION`] [`[--node-taints](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-taints)`=[`NODE_TAINT`,…]] [`[--node-version](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-version)`=`NODE_VERSION`] [`[--num-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--num-nodes)`=`NUM_NODES`] [`[--opportunistic-maintenance](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--opportunistic-maintenance)`=[`node-idle-time`=`NODE_IDLE_TIME`,`window`=`WINDOW`,`min-nodes`=`MIN_NODES`,…]] [`[--placement-policy](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--placement-policy)`=`PLACEMENT_POLICY`] [`[--placement-type](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--placement-type)`=`PLACEMENT_TYPE`] [`[--preemptible](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--preemptible)`] [`[--resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--resource-manager-tags)`=[`KEY`=`VALUE`,…]] [`[--sandbox](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--sandbox)`=[`type`=`TYPE`]] [`[--secondary-boot-disk](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--secondary-boot-disk)`=[`disk-image`=`DISK_IMAGE`,[`mode`=`MODE`],…]] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--shielded-secure-boot)`] [`[--sole-tenant-node-affinity-file](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--sole-tenant-node-affinity-file)`=`SOLE_TENANT_NODE_AFFINITY_FILE`] [`[--spot](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--spot)`] [`[--standard-rollout-policy](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--standard-rollout-policy)`=[`batch-node-count`=`BATCH_NODE_COUNT`,`batch-percent`=`BATCH_NODE_PERCENTAGE`,`batch-soak-duration`=`BATCH_SOAK_DURATION`,…]] [`[--storage-pools](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--storage-pools)`=`STORAGE_POOL`,[…]] [`[--system-config-from-file](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--system-config-from-file)`=`PATH_TO_FILE`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#TAG)`,…]] [`[--threads-per-core](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--threads-per-core)`=`THREADS_PER_CORE`] [`[--tpu-topology](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--tpu-topology)`=`TPU_TOPOLOGY`] [`[--windows-os-version](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--windows-os-version)`=`WINDOWS_OS_VERSION`] [`[--workload-metadata](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--workload-metadata)`=`WORKLOAD_METADATA`] [`[--create-pod-ipv4-range](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--create-pod-ipv4-range)`=[`KEY`=`VALUE`,…]     | `[--pod-ipv4-range](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--pod-ipv4-range)`=`NAME`] [`[--enable-autoscaling](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-autoscaling)` `[--location-policy](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--location-policy)`=`LOCATION_POLICY` `[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--min-nodes)`=`MIN_NODES` `[--total-max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--total-max-nodes)`=`TOTAL_MAX_NODES` `[--total-min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--total-min-nodes)`=`TOTAL_MIN_NODES`] [`[--enable-best-effort-provision](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-best-effort-provision)` `[--min-provision-nodes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--min-provision-nodes)`=`MIN_PROVISION_NODES`] [`[--ephemeral-storage-local-ssd](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--ephemeral-storage-local-ssd)`[=[`count`=`COUNT`]]     | `[--local-nvme-ssd-block](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--local-nvme-ssd-block)`[=[`count`=`COUNT`]]     | `[--local-ssd-count](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--local-ssd-count)`=`LOCAL_SSD_COUNT`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#ZONE)`] [`[--reservation](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--reservation)`=`RESERVATION` `[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--reservation-affinity)`=`RESERVATION_AFFINITY`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--scopes)`=[`SCOPE`,…]; default="gke-default" `[--service-account](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--service-account)`=`SERVICE_ACCOUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud container node-pools create` facilitates the creation of a
node pool in a Google Kubernetes Engine cluster. A variety of options exists to
customize the node configuration and the number of nodes created.

**EXAMPLES**

: To create a new node pool "node-pool-1" with the default options in the cluster
"sample-cluster", run:

```
gcloud container node-pools create node-pool-1 --cluster=sample-cluster
```

The new node pool will show up in the cluster after all the nodes have been
provisioned.
To create a node pool with 5 nodes, run:

```
gcloud container node-pools create node-pool-1 --cluster=sample-cluster --num-nodes=5
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the node pool to create.

**FLAGS**

: **--accelerator**:
Attaches accelerators (e.g. GPUs) to all nodes.

**`type`**:
(Required) The specific type (e.g. nvidia-tesla-t4 for NVIDIA T4) of accelerator
to attach to the instances. Use `gcloud compute accelerator-types
list` to learn about all available accelerator types.

**`count`**:
(Optional) The number of accelerators to attach to the instances. The default
value is 1.

**`gpu-driver-version`**:
(Optional) The NVIDIA driver version to install. GPU_DRIVER_VERSION must be one
of:

```
`default`: Install the default driver version for this GKE version.
```

```
`latest`: Install the latest driver version available for this GKE version.
Can only be used for nodes that use Container-Optimized OS.
```

```
`disabled`: Skip automatic driver installation. You must manually install a
driver after you create the cluster. If you omit the flag `gpu-driver-version`,
this is the default option. To learn how to manually install the GPU driver,
refer to: https://cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers
```

**`gpu-partition-size`**:
(Optional) The GPU partition size used when running multi-instance GPUs. For
information about multi-instance GPUs, refer to: [https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi)

**`gpu-sharing-strategy`**:
(Optional) The GPU sharing strategy (e.g. time-sharing) to use. For information
about GPU sharing, refer to: [https://cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus](https://cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus)

**`max-shared-clients-per-gpu`**:
(Optional) The max number of containers allowed to share each GPU on the node.
This field is used together with `gpu-sharing-strategy`.

**--additional-node-network**:
Attach an additional network interface to each node in the pool. This parameter
can be specified up to 7 times.
e.g. --additional-node-network network=dataplane,subnetwork=subnet-dp

**`network`**:
(Required) The network to attach the new interface to.

**`subnetwork`**:
(Required) The subnetwork to attach the new interface to.

**--additional-pod-network**:
Specify the details of a secondary range to be used for an additional pod
network. Not needed if you use "host" typed NIC from this network. This
parameter can be specified up to 35 times.
e.g. --additional-pod-network
subnetwork=subnet-dp,pod-ipv4-range=sec-range-blue,max-pods-per-node=8.

**`subnetwork`**:
(Optional) The name of the subnetwork to link the pod network to. If not
specified, the pod network defaults to the subnet connected to the default
network interface.

**`pod-ipv4-range`**:
(Required) The name of the secondary range in the subnetwork. The range must
hold at least (2 * MAX_PODS_PER_NODE * MAX_NODES_IN_RANGE) IPs.

**`max-pods-per-node`**:
(Optional) Maximum amount of pods per node that can utilize this ipv4-range.
Defaults to NodePool (if specified) or Cluster value.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--boot-disk-kms-key**:
The Customer Managed Encryption Key used to encrypt the boot disk attached to
each node in the node pool. This should be of the form
projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME].
For more information about protecting resources with Cloud KMS Keys please see:
[https://cloud.google.com/compute/docs/disks/customer-managed-encryption](https://cloud.google.com/compute/docs/disks/customer-managed-encryption)

**--cluster**:
The cluster to add the node pool to. Overrides the default
`container/cluster` property value for this command invocation.

**--confidential-node-type**:
Enable confidential nodes for the node pool. Enabling Confidential Nodes will
create nodes using Confidential VM [https://cloud.google.com/compute/confidential-vm/docs/about-cvm](https://cloud.google.com/compute/confidential-vm/docs/about-cvm).
`CONFIDENTIAL_NODE_TYPE` must be one of: `sev`,
`sev_snp`, `tdx`, `disabled`.

**--containerd-config-from-file**:
Path of the YAML file that contains containerd configuration entries like
configuring access to private image registries.
For detailed information on the configuration usage, please refer to [https://cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration](https://cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).
Note: Updating the containerd configuration of an existing cluster or node pool
requires recreation of the existing nodes, which might cause disruptions in
running workloads.
Use a full or relative path to a local file containing the value of
containerd_config.

**--data-cache-count**:
Specifies the number of local SSDs to be utilized for GKE Data Cache in the node
pool.

**--disk-size**:
Size for node VM boot disks in GB. Defaults to 100GB.

**--disk-type**:
Type of the node VM boot disk. For version 1.24 and later, defaults to
pd-balanced. For versions earlier than 1.24, defaults to pd-standard.
`DISK_TYPE` must be one of: `pd-standard`,
`pd-ssd`, `pd-balanced`, `hyperdisk-balanced`,
`hyperdisk-extreme`, `hyperdisk-throughput`.

**--enable-autoprovisioning**:
Enables Cluster Autoscaler to treat the node pool as if it was autoprovisioned.
Cluster Autoscaler will be able to delete the node pool if it's unneeded.

**--enable-autorepair**:
Enable node autorepair feature for a node pool.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --enable-autorepair
```

Node autorepair is enabled by default for node pools using COS, COS_CONTAINERD,
UBUNTU or UBUNTU_CONTAINERD as a base image, use --no-enable-autorepair to
disable.
See [https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair)
for more info.

**--enable-autoupgrade**:
Sets autoupgrade feature for a node pool.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --enable-autoupgrade
```

See [https://cloud.google.com/kubernetes-engine/docs/node-auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/node-auto-upgrades)
for more info.
Enabled by default, use `--no-enable-autoupgrade` to disable.

**--enable-blue-green-upgrade**:
Changes node pool upgrade strategy to blue-green upgrade.

**--enable-confidential-nodes**:
Enable confidential nodes for the node pool. Enabling Confidential Nodes will
create nodes using Confidential VM [https://cloud.google.com/compute/confidential-vm/docs/about-cvm](https://cloud.google.com/compute/confidential-vm/docs/about-cvm).

**--enable-confidential-storage**:
Enable confidential storage for the node pool. Enabling Confidential Storage
will create boot disk with confidential mode

**--enable-gvnic**:
Enable the use of GVNIC for this cluster. Requires re-creation of nodes using
either a node-pool upgrade or node-pool creation.

**--enable-image-streaming**:
Specifies whether to enable image streaming on node pool.

**--enable-insecure-kubelet-readonly-port**:
Enables the Kubelet's insecure read only port.
To disable the readonly port on a cluster or node-pool set the flag to
`--no-enable-insecure-kubelet-readonly-port`.

**--enable-nested-virtualization**:
Enables the use of nested virtualization on the node pool. Defaults to
`false`. Can only be enabled on UBUNTU_CONTAINERD base image or
COS_CONTAINERD base image with version 1.28.4-gke.1083000 and above.

**--enable-private-nodes**:
Enables provisioning nodes with private IP addresses only.
The control plane still communicates with all nodes through private IP addresses
only, regardless of whether private nodes are enabled or disabled.

**--enable-queued-provisioning**:
Mark the nodepool as Queued only. This means that all new nodes can be obtained
only through queuing via ProvisioningRequest API.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --enable-queued-provisioning
… and other required parameters, for more details see:
https://cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest
```

**--enable-surge-upgrade**:
Changes node pool upgrade strategy to surge upgrade.

**--flex-start**:
Start the node pool with Flex Start provisioning model.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --flex-start
and other required parameters, for more details see:
https://cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest
```

**--image-type**:
The image type to use for the node pool. Defaults to server-specified.
Image Type specifies the base OS that the nodes in the node pool will run on. If
an image type is specified, that will be assigned to the node pool and all
future upgrades will use the specified image type. If it is not specified the
server will pick the default image type.
The default image type and the list of valid image types are available using the
following command.

```
gcloud container get-server-config
```

**--labels**:
Labels to apply to the Google Cloud resources of node pools in the Kubernetes
Engine cluster. These are unrelated to Kubernetes labels. Warning: Updating this
label will causes the node(s) to be recreated.
Examples:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --labels=label1=value1,label2=value2
```

**--logging-variant**:
Specifies the logging variant that will be deployed on all the nodes in the node
pool. If the node pool doesn't specify a logging variant, then the logging
variant specified for the cluster will be deployed on all the nodes in the node
pool. Valid logging variants are `MAX_THROUGHPUT`,
`DEFAULT`. `LOGGING_VARIANT` must be one of:

**`DEFAULT`**:
'DEFAULT' variant requests minimal resources but may not guarantee high
throughput.

**`MAX_THROUGHPUT`**:
'MAX_THROUGHPUT' variant requests more node resources and is able to achieve
logging throughput up to 10MB per sec.

**--machine-type**:
The type of machine to use for nodes. Defaults to e2-medium. The list of
predefined machine types is available using the following command:

```
gcloud compute machine-types list
```

You can also specify custom machine types by providing a string with the format
"custom-CPUS-RAM" where "CPUS" is the number of virtual CPUs and "RAM" is the
amount of RAM in MiB.
For example, to create a node pool using custom machines with 2 vCPUs and 12 GB
of RAM:

```
gcloud container node-pools create high-mem-pool --machine-type=custom-2-12288
```

**--max-pods-per-node**:
The max number of pods per node for this node pool.
This flag sets the maximum number of pods that can be run at the same time on a
node. This will override the value given with --default-max-pods-per-node flag
set at the cluster level.
Must be used in conjunction with '--enable-ip-alias'.

**--max-run-duration**:
Limit the runtime of each node in the node pool to the specified duration.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --max-run-duration=3600s
```

**--max-surge-upgrade**:
Number of extra (surge) nodes to be created on each upgrade of the node pool.
Specifies the number of extra (surge) nodes to be created during this node
pool's upgrades. For example, running the following command will result in
creating an extra node each time the node pool is upgraded:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --max-surge-upgrade=1   --max-unavailable-upgrade=0
```

Must be used in conjunction with '--max-unavailable-upgrade'.

**--max-unavailable-upgrade**:
Number of nodes that can be unavailable at the same time on each upgrade of the
node pool.
Specifies the number of nodes that can be unavailable at the same time during
this node pool's upgrades. For example, running the following command will
result in having 3 nodes being upgraded in parallel (1 + 2), but keeping always
at least 3 (5 - 2) available each time the node pool is upgraded:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --num-nodes=5   --max-surge-upgrade=1 --max-unavailable-upgrade=2
```

Must be used in conjunction with '--max-surge-upgrade'.

**--metadata**:
Compute Engine metadata to be made available to the guest operating system
running on nodes within the node pool.
Each metadata entry is a key/value pair separated by an equals sign. Metadata
keys must be unique and less than 128 bytes in length. Values must be less than
or equal to 32,768 bytes in length. The total size of all keys and values must
be less than 512 KB. Multiple arguments can be passed to this flag. For example:
``--metadata
key-1=value-1,key-2=value-2,key-3=value-3``
Additionally, the following keys are reserved for use by Kubernetes Engine:

- ``cluster-location``
- ``cluster-name``
- ``cluster-uid``
- ``configure-sh``
- ``enable-os-login``
- ``gci-update-strategy``
- ``gci-ensure-gke-docker``
- ``instance-template``
- ``kube-env``
- ``startup-script``
- ``user-data``

Google Kubernetes Engine sets the following keys by default:

- ``serial-port-logging-enable``

See also Compute Engine's [documentation](https://cloud.google.com/compute/docs/storing-retrieving-metadata)
on storing and retrieving instance metadata.

**--metadata-from-file**:
Same as ``--metadata`` except that the value
for the entry will be read from a local file.

**--min-cpu-platform**:
When specified, the nodes for the new node pool will be scheduled on host with
specified CPU architecture or a newer one.
Examples:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --min-cpu-platform=PLATFORM
```

To list available CPU platforms in given zone, run:

```
gcloud beta compute zones describe ZONE --format="value(availableCpuPlatforms)"
```

CPU platform selection is available only in selected zones.

**--network-performance-configs**:
Configures network performance settings for the node pool. If this flag is not
specified, the pool will be created with its default network performance
configuration.

**`total-egress-bandwidth-tier`**:
Total egress bandwidth is the available outbound bandwidth from a VM, regardless
of whether the traffic is going to internal IP or external IP destinations. The
following tier values are allowed: [TIER_UNSPECIFIED,TIER_1]

**--node-group**:
Assign instances of this pool to run on the specified Google Compute Engine node
group. This is useful for running workloads on sole tenant nodes.
To see available sole tenant node-groups, run:

```
gcloud compute sole-tenancy node-groups list
```

To create a sole tenant node group, run:

```
gcloud compute sole-tenancy node-groups create [GROUP_NAME]     --location [ZONE] --node-template [TEMPLATE_NAME]     --target-size [TARGET_SIZE]
```

See [https://cloud.google.com/compute/docs/nodes](https://cloud.google.com/compute/docs/nodes)
for more information on sole tenancy and node groups.

**--node-labels**:
Applies the given Kubernetes labels on all nodes in the new node pool.
Examples:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --node-labels=label1=value1,label2=value2
```

New nodes, including ones created by resize or recreate, will have these labels
on the Kubernetes API node object and can be used in nodeSelectors. See [https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
for examples.
Note that Kubernetes labels, intended to associate cluster components and
resources with one another and manage resource lifecycles, are different from
Google Kubernetes Engine labels that are used for the purpose of tracking
billing and usage information.

**--node-locations**:
The set of zones in which the node pool's nodes should be located.
Multiple locations can be specified, separated by commas. For example:

```
gcloud container node-pools create node-pool-1 --cluster=sample-cluster --node-locations=us-central1-a,us-central1-b
```

**--node-pool-soak-duration**:
Time in seconds to be spent waiting during blue-green upgrade before deleting
the blue pool and completing the upgrade.

```
gcloud container node-pools create example-cluster  --node-pool-soak-duration=600s
```

**--node-taints**:
Applies the given kubernetes taints on all nodes in the new node pool, which can
be used with tolerations for pod scheduling.
Examples:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --node-taints=key1=val1:NoSchedule,key2=val2:PreferNoSchedule
```

To read more about node-taints, see [https://cloud.google.com/kubernetes-engine/docs/node-taints](https://cloud.google.com/kubernetes-engine/docs/node-taints).

**--node-version**:
The Kubernetes version to use for nodes. Defaults to server-specified.
The default Kubernetes version is available using the following command.

```
gcloud container get-server-config
```

**--num-nodes**:
The number of nodes in the node pool in each of the cluster's zones. Defaults to
3.
Exception: when `--tpu-topology` is specified for multi-host TPU
machine types the number of nodes will be defaulted to `(product of
topology)/(# of chips per VM)`.

**--opportunistic-maintenance**:
Opportunistic maintenance options.
node-idle-time: Time to be spent waiting for node to be idle before starting
maintenance, ending with 's'. Example: "3.5s"
window: The window of time that opportunistic maintenance can run, ending with
's'. Example: A setting of 14 days (1209600s) implies that opportunistic
maintenance can only be ran in the 2 weeks leading up to the scheduled
maintenance date. Setting 28 days(2419200s) allows opportunistic maintenance to
run at any time in the scheduled maintenance window.
min-nodes: Minimum number of nodes in the node pool to be available during the
opportunistic triggered maintenance.

```
gcloud container node-pools create example-cluster  --opportunistic-maintenance=node-idle-time=600s,window=600s,min-nodes=2
```

**--placement-policy**:
Indicates the desired resource policy to use.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --placement-policy my-placement
```

**--placement-type**:
Placement type allows to define the type of node placement within this node
pool.
`UNSPECIFIED` - No requirements on the placement of nodes. This is
the default option.
`COMPACT` - GKE will attempt to place the nodes in a close proximity
to each other. This helps to reduce the communication latency between the nodes,
but imposes additional limitations on the node pool size.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --placement-type=COMPACT
```

`PLACEMENT_TYPE` must be one of: `UNSPECIFIED`,
`COMPACT`.

**--preemptible**:
Create nodes using preemptible VM instances in the new node pool.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --preemptible
```

New nodes, including ones created by resize or recreate, will use preemptible VM
instances. See [https://cloud.google.com/kubernetes-engine/docs/preemptible-vm](https://cloud.google.com/kubernetes-engine/docs/preemptible-vm)
for more information on how to use Preemptible VMs with Kubernetes Engine.

**--resource-manager-tags**:
Applies the specified comma-separated resource manager tags that has the
GCE_FIREWALL purpose to all nodes in the new node pool.
Examples:

```
gcloud container node-pools create example-node-pool --resource-manager-tags=tagKeys/1234=tagValues/2345
gcloud container node-pools create example-node-pool --resource-manager-tags=my-project/key1=value1
gcloud container node-pools create example-node-pool --resource-manager-tags=12345/key1=value1,23456/key2=value2
gcloud container node-pools create example-node-pool --resource-manager-tags=
```

All nodes, including nodes that are resized or re-created, will have the
specified tags on the corresponding Instance object in the Compute Engine API.
You can reference these tags in network firewall policy rules. For instructions,
see [https://cloud.google.com/firewall/docs/use-tags-for-firewalls](https://cloud.google.com/firewall/docs/use-tags-for-firewalls).

**--sandbox**:
Enables the requested sandbox on all nodes in the node pool.
Examples:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --sandbox="type=gvisor"
```

The only supported type is 'gvisor'.

**--secondary-boot-disk**:
Attaches secondary boot disks to all nodes.

**`disk-image`**:
(Required) The full resource path to the source disk image to create the
secondary boot disks from.

**`mode`**:
(Optional) The configuration mode for the secondary boot disks. The default
value is "CONTAINER_IMAGE_CACHE".

**--shielded-integrity-monitoring**:
Enables monitoring and attestation of the boot integrity of the instance. The
attestation is performed against the integrity policy baseline. This baseline is
initially derived from the implicitly trusted boot image when the instance is
created.

**--shielded-secure-boot**:
The instance will boot with secure boot enabled.

**--sole-tenant-node-affinity-file**:
JSON/YAML file containing the configuration of desired sole tenant nodes onto
which this node pool could be backed by. These rules filter the nodes according
to their node affinity labels. A node's affinity labels come from the node
template of the group the node is in.
The file should contain a list of a JSON/YAML objects. For an example, see [https://cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#configure_node_affinity_labels](https://cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#configure_node_affinity_labels).
The following list describes the fields:

**`key`**:
Corresponds to the node affinity label keys of the Node resource.

**`operator`**:
Specifies the node selection type. Must be one of: `IN`: Requires
Compute Engine to seek for matched nodes. `NOT_IN`: Requires Compute
Engine to avoid certain nodes.

**`values`**:
Optional. A list of values which correspond to the node affinity label values of
the Node resource.

**--spot**:
Create nodes using spot VM instances in the new node pool.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --spot
```

New nodes, including ones created by resize or recreate, will use spot VM
instances.

**--standard-rollout-policy**:
Standard rollout policy options for blue-green upgrade.
Batch sizes are specified by one of, batch-node-count or batch-percent. The
duration between batches is specified by batch-soak-duration.

```
gcloud container node-pools create example-cluster  --standard-rollout-policy=batch-node-count=3,batch-soak-duration=60s
```

```
gcloud container node-pools create example-cluster  --standard-rollout-policy=batch-percent=0.3,batch-soak-duration=60s
```

**--storage-pools**:
A list of storage pools where the node pool's boot disks will be provisioned.
STORAGE_POOL must be in the format
projects/project/zones/zone/storagePools/storagePool

**--system-config-from-file**:
Path of the YAML/JSON file that contains the node configuration, including Linux
kernel parameters (sysctls) and kubelet configs.
Examples:

```
kubeletConfig:
  cpuManagerPolicy: static
  memoryManager:
    policy: Static
  topologyManager:
    policy: BestEffort
    scope: pod
linuxConfig:
  sysctl:
    net.core.somaxconn: '2048'
    net.ipv4.tcp_rmem: '4096 87380 6291456'
  hugepageConfig:
    hugepage_size2m: '1024'
    hugepage_size1g: '2'
  cgroupMode: 'CGROUP_MODE_V2'
```

List of supported kubelet configs in 'kubeletConfig'.

| KEY | VALUE |
| --- | --- |
| cpuManagerPolicy | either 'static' or 'none' |
| cpuCFSQuota | true or false (enabled by default) |
| cpuCFSQuotaPeriod | interval (e.g., '100ms') |
| memoryManager | specify memory manager policy |
| topologyManager | specify topology manager policy and scope |
| podPidsLimit | integer (The value must be greater than or equal to 1024 and less than 4194304.) |
| containerLogMaxSize | positive number plus unit suffix (e.g., '100Mi', '0.2Gi'. The value must be between 10Mi and 500Mi.) |
| containerLogMaxFiles | integer (The value must be between [2, 10].) |
| imageGcLowThresholdPercent | integer (The value must be between [10, 85], and lower than imageGcHighThresholdPercent.) |
| imageGcHighThresholdPercent | integer (The value must be between [10, 85], and greater than imageGcLowThresholdPercent.) |
| imageMinimumGcAge | interval (e.g., '100s', '1m'. The value must be less than '2m'.) |
| imageMaximumGcAge | interval (e.g., '100s', '1m'. The value must be greater than imageMinimumGcAge.) |
| allowedUnsafeSysctls | list of sysctls (Allowlisted groups: 'kernel.shm*', 'kernel.msg*', 'kernel.sem', 'fs.mqueue.*', and 'net.*', and sysctls under the groups.) |
| singleProcessOomKill | true or false |

| KEY | VALUE |
| --- | --- |
| policy | either 'Static' or 'None' |

| KEY | VALUE |
| --- | --- |
| policy | either 'none' or 'best-effort' or 'single-numa-node' or 'restricted' |
| scope | either 'pod' or 'container' |

List of supported sysctls in 'linuxConfig'.

| KEY | VALUE |
| --- | --- |
| net.core.netdev_max_backlog | Any positive integer, less than 2147483647 |
| net.core.rmem_default | Must be between [2304, 2147483647] |
| net.core.rmem_max | Must be between [2304, 2147483647] |
| net.core.wmem_default | Must be between [4608, 2147483647] |
| net.core.wmem_max | Must be between [4608, 2147483647] |
| net.core.optmem_max | Any positive integer, less than 2147483647 |
| net.core.somaxconn | Must be between [128, 2147483647] |
| net.ipv4.tcp_rmem | Any positive integer tuple |
| net.ipv4.tcp_wmem | Any positive integer tuple |
| net.ipv4.tcp_tw_reuse | Must be {0, 1, 2} |
| net.netfilter.nf_conntrack_max | Must be between [65536, 4194304] |
| net.netfilter.nf_conntrack_buckets | Must be between [65536, 524288]. Recommend setting: nf_conntrack_max = nf_conntrack_buckets * 4 |
| net.netfilter.nf_conntrack_tcp_timeout_close_wait | Must be between [60, 3600] |
| net.netfilter.nf_conntrack_tcp_timeout_time_wait | Must be between [1, 600] |
| net.netfilter.nf_conntrack_tcp_timeout_established | Must be between [600, 86400] |
| net.netfilter.nf_conntrack_acct | Must be {0, 1} |
| kernel.shmmni | Must be between [4096, 32768] |
| kernel.shmmax | Must be between [0, 18446744073692774399] |
| kernel.shmall | Must be between [0, 18446744073692774399] |
| vm.max_map_count | Must be between [65536, 2147483647] |

List of supported hugepage size in 'hugepageConfig'.

| KEY | VALUE |
| --- | --- |
| hugepage_size2m | Number of 2M huge pages, any positive integer |
| hugepage_size1g | Number of 1G huge pages, any positive integer |

Allocated hugepage size should not exceed 60% of available memory on the node.
For example, c2d-highcpu-4 has 8GB memory, total allocated hugepage of 2m and 1g
should not exceed 8GB * 0.6 = 4.8GB.
1G hugepages are only available in following machine familes: c3, m2, c2d, c3d,
h3, m3, a2, a3, g2.
Supported values for 'cgroupMode' under 'linuxConfig'.

- `CGROUP_MODE_V1`: Use cgroupv1 on the node pool.
- `CGROUP_MODE_V2`: Use cgroupv2 on the node pool.
- `CGROUP_MODE_UNSPECIFIED`: Use the default GKE cgroup configuration.

Note, updating the system configuration of an existing node pool requires
recreation of the nodes which which might cause a disruption.
Use a full or relative path to a local file containing the value of
system_config.

**--tags**:
Applies the given Compute Engine tags (comma separated) on all nodes in the new
node-pool. Example:

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --tags=tag1,tag2
```

New nodes, including ones created by resize or recreate, will have these tags on
the Compute Engine API instance object and can be used in firewall rules. See [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)
for examples.

**--threads-per-core**:
The number of visible threads per physical core for each node. To disable
simultaneous multithreading (SMT) set this to 1.

**--tpu-topology**:
The desired physical topology for the PodSlice.

```
gcloud container node-pools create node-pool-1 --cluster=example-cluster --tpu-topology
```

**--windows-os-version**:
Specifies the Windows Server Image to use when creating a Windows node pool.
Valid variants can be "ltsc2019", "ltsc2022". It means using LTSC2019 server
image or LTSC2022 server image. If the node pool doesn't specify a Windows
Server Image Os version, then Ltsc2019 will be the default one to use.
`WINDOWS_OS_VERSION` must be one of:
`ltsc2019`, `ltsc2022`.

**--workload-metadata**:
Type of metadata server available to pods running in the node pool.
`WORKLOAD_METADATA` must be one of:

**`GCE_METADATA`**:
Pods running in this node pool have access to the node's underlying Compute
Engine Metadata Server.

**`GKE_METADATA`**:
Run the Kubernetes Engine Metadata Server on this node. The Kubernetes Engine
Metadata Server exposes a metadata API to workloads that is compatible with the
V1 Compute Metadata APIs exposed by the Compute Engine and App Engine Metadata
Servers. This feature can only be enabled if Workload Identity is enabled at the
cluster level.

**--create-pod-ipv4-range**

**--enable-autoscaling**

**--enable-best-effort-provision**

**--ephemeral-storage-local-ssd**

**--location**

**--reservation**

**--scopes**

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
gcloud alpha container node-pools create
```

```
gcloud beta container node-pools create
```