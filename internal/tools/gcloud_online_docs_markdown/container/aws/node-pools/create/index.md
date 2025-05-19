# gcloud container aws node-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create)*

**NAME**

: **gcloud container aws node-pools create - create a node pool in an Anthos cluster on AWS**

**SYNOPSIS**

: **`gcloud container aws node-pools create` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--location)`=`LOCATION`) `[--config-encryption-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--config-encryption-kms-key-arn)`=`CONFIG_ENCRYPTION_KMS_KEY_ARN` `[--iam-instance-profile](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--iam-instance-profile)`=`IAM_INSTANCE_PROFILE` `[--max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--max-pods-per-node)`=`MAX_PODS_PER_NODE` `[--node-version](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--node-version)`=`NODE_VERSION` `[--subnet-id](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--subnet-id)`=`SUBNET_ID` (`[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--min-nodes)`=`MIN_NODES`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#ANNOTATION)`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--async)`] [`[--enable-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--enable-autorepair)`] [`[--kubelet-config-cpu-cfs-quota](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--kubelet-config-cpu-cfs-quota)`=`KUBELET_CONFIG_CPU_CFS_QUOTA`] [`[--kubelet-config-cpu-cfs-quota-period](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--kubelet-config-cpu-cfs-quota-period)`=`KUBELET_CONFIG_CPU_CFS_QUOTA_PERIOD`] [`[--kubelet-config-cpu-manager-policy](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--kubelet-config-cpu-manager-policy)`=`KUBELET_CONFIG_CPU_MANAGER_POLICY`] [`[--kubelet-config-pod-pids-limit](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--kubelet-config-pod-pids-limit)`=`KUBELET_CONFIG_POD_PIDS_LIMIT`] [`[--max-surge-update](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--max-surge-update)`=`MAX_SURGE_UPDATE`] [`[--max-unavailable-update](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--max-unavailable-update)`=`MAX_UNAVAILABLE_UPDATE`] [`[--node-labels](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--node-labels)`=`NODE_LABEL`,[`[NODE_LABEL](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#NODE_LABEL)`,…]] [`[--node-taints](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--node-taints)`=`NODE_TAINT`,[`[NODE_TAINT](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#NODE_TAINT)`,…]] [`[--root-volume-iops](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--root-volume-iops)`=`ROOT_VOLUME_IOPS`] [`[--root-volume-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--root-volume-kms-key-arn)`=`ROOT_VOLUME_KMS_KEY_ARN`] [`[--root-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--root-volume-size)`=`ROOT_VOLUME_SIZE`] [`[--root-volume-throughput](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--root-volume-throughput)`=`ROOT_VOLUME_THROUGHPUT`] [`[--root-volume-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--root-volume-type)`=`ROOT_VOLUME_TYPE`] [`[--security-group-ids](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--security-group-ids)`=[`SECURITY_GROUP_ID`,…]] [`[--ssh-ec2-key-pair](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--ssh-ec2-key-pair)`=`SSH_EC2_KEY_PAIR`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#TAG)`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--validate-only)`] [`[--autoscaling-metrics-granularity](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--autoscaling-metrics-granularity)`=`AUTOSCALING_METRICS_GRANULARITY` : `[--autoscaling-metrics](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--autoscaling-metrics)`=[`AUTOSCALING_METRIC`,…]] [`[--instance-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--instance-type)`=`INSTANCE_TYPE`     | `[--spot-instance-types](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--spot-instance-types)`=[`INSTANCE_TYPE`,…]] [`[--proxy-secret-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--proxy-secret-arn)`=`PROXY_SECRET_ARN` `[--proxy-secret-version-id](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--proxy-secret-version-id)`=`PROXY_SECRET_VERSION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Create a node pool in an Anthos cluster on AWS.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To create a node pool named ``my-node-pool`` in
a cluster named ``my-cluster`` managed in
location ``us-west1``, run:

```
gcloud container aws node-pools create my-node-pool --cluster=my-cluster --location=us-west1 --iam-instance-profile=IAM_INSTANCE_PROFILE --node-version=NODE_VERSION --subnet-id=SUBNET_ID
```

**POSITIONAL ARGUMENTS**

: **Node pool resource - node pool to create. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_POOL`**:
ID of the node_pool or fully qualified identifier for the node_pool.
To set the `node_pool` attribute:

- provide the argument `node_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
cluster of the node_pool.
To set the `cluster` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--location**:
Google Cloud location for the node_pool.
To set the `location` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_aws/location`.**

**REQUIRED FLAGS**

: **--config-encryption-kms-key-arn**:
Amazon Resource Name (ARN) of the AWS KMS key to encrypt the user data.

**--iam-instance-profile**:
Name or ARN of the IAM instance profile associated with the node pool.

**--max-pods-per-node**:
Maximum number of pods per node.

**--node-version**:
Kubernetes version to use for the node pool.

**--subnet-id**:
Subnet ID of an existing VNET to use for the node pool.

**--max-nodes**

**OPTIONAL FLAGS**

: **--annotations**:
Annotations for the node pool.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--enable-autorepair**:
Enable node autorepair feature for a node pool. Use --no-enable-autorepair to
disable.

```
gcloud container aws node-pools create --enable-autorepair
```

Node autorepair is disabled by default.

**--kubelet-config-cpu-cfs-quota**:
Enforce a Kubelet CPU CFS quota.

**--kubelet-config-cpu-cfs-quota-period**:
Kubelet CPU CFS quota period, within the range "1ms" to "1s".

**--kubelet-config-cpu-manager-policy**:
Kubelet CPU manager policy.
`KUBELET_CONFIG_CPU_MANAGER_POLICY` must be one of:
`none`, `static`.

**--kubelet-config-pod-pids-limit**:
Kubelet maximum number of PIDS in any pod, within the range 1024 to 4194304.

**--max-surge-update**:
Maximum number of extra (surge) nodes to be created beyond the current size of
the node pool during its update process. Use --max-unavailable-update as well,
if needed, to control the overall surge settings.
To create an extra node each time the node pool is rolling updated, run:

```
gcloud container aws node-pools create --max-surge-update=1 --max-unavailable-update=0
```

**--max-unavailable-update**:
Maximum number of nodes that can be simultaneously unavailable during this node
pool's update process. Use --max-surge-update as well, if needed, to control the
overall surge settings.
To update 3 nodes in parallel (1 + 2), but keep at least 4 nodes (6 - 2)
available each time the node pool is rolling updated, run:

```
gcloud container aws node-pools create --min-nodes=6 --max-surge-update=1 --max-unavailable-update=2
```

**--node-labels**:
Labels assigned to the node pool's nodes.

**--node-taints**:
Taints assigned to nodes of the node pool. Node taint is of format
key=value:effect. Effect must be one of: NoExecute, NoSchedule,
PreferNoSchedule.

**--root-volume-iops**:
Number of I/O operations per second (IOPS) to provision for the root volume.

**--root-volume-kms-key-arn**:
Amazon Resource Name (ARN) of the AWS KMS key to encrypt the root volume.

**--root-volume-size**:
Size of the root volume. The value must be a whole number followed by a size
unit of `GB` for gigabyte, or `TB` for terabyte. If no
size unit is specified, GB is assumed.

**--root-volume-throughput**:
Throughput to provision for the root volume, in MiB/s. Only valid if the volume
type is GP3. If volume type is GP3 and throughput is not provided, it defaults
to 125.

**--root-volume-type**:
Type of the root volume. `ROOT_VOLUME_TYPE` must be one
of: `gp2`, `gp3`.

**--security-group-ids**:
IDs of additional security groups to add to the node pool's nodes.

**--ssh-ec2-key-pair**:
Name of the EC2 key pair authorized to login to the node pool's nodes.

**--tags**:
Applies the given tags (comma separated) on the node pool. Example:

```
gcloud container aws node-pools create EXAMPLE_NODE_POOL --tags=tag1=one,tag2=two
```

**--validate-only**:
Validate the node pool to create, but don't actually perform it.

**--autoscaling-metrics-granularity**

**--instance-type**

**--proxy-secret-arn**

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

: This variant is also available:

```
gcloud alpha container aws node-pools create
```