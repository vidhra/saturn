# gcloud container aws node-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update)*

**NAME**

: **gcloud container aws node-pools update - update a node pool in an Anthos cluster on AWS**

**SYNOPSIS**

: **`gcloud container aws node-pools update` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--async)`] [`[--config-encryption-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--config-encryption-kms-key-arn)`=`CONFIG_ENCRYPTION_KMS_KEY_ARN`] [`[--enable-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--enable-autorepair)`] [`[--iam-instance-profile](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--iam-instance-profile)`=`IAM_INSTANCE_PROFILE`] [`[--instance-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--instance-type)`=`INSTANCE_TYPE`] [`[--max-surge-update](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--max-surge-update)`=`MAX_SURGE_UPDATE`] [`[--max-unavailable-update](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--max-unavailable-update)`=`MAX_UNAVAILABLE_UPDATE`] [`[--node-version](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--node-version)`=`NODE_VERSION`] [`[--root-volume-iops](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--root-volume-iops)`=`ROOT_VOLUME_IOPS`] [`[--root-volume-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--root-volume-kms-key-arn)`=`ROOT_VOLUME_KMS_KEY_ARN`] [`[--root-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--root-volume-size)`=`ROOT_VOLUME_SIZE`] [`[--root-volume-throughput](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--root-volume-throughput)`=`ROOT_VOLUME_THROUGHPUT`] [`[--root-volume-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--root-volume-type)`=`ROOT_VOLUME_TYPE`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--validate-only)`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#ANNOTATION)`,…]     | `[--clear-annotations](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--clear-annotations)`] [`[--clear-autoscaling-metrics](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--clear-autoscaling-metrics)`     | `[--autoscaling-metrics](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--autoscaling-metrics)`=[`AUTOSCALING_METRIC`,…] `[--autoscaling-metrics-granularity](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--autoscaling-metrics-granularity)`=`AUTOSCALING_METRICS_GRANULARITY`] [`[--clear-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--clear-node-labels)`     | `[--node-labels](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--node-labels)`=`NODE_LABEL`,[`[NODE_LABEL](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#NODE_LABEL)`,…]] [`[--clear-proxy-config](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--clear-proxy-config)`     | `[--proxy-secret-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--proxy-secret-arn)`=`PROXY_SECRET_ARN` `[--proxy-secret-version-id](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--proxy-secret-version-id)`=`PROXY_SECRET_VERSION_ID`] [`[--clear-security-group-ids](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--clear-security-group-ids)`     | `[--security-group-ids](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--security-group-ids)`=[`SECURITY_GROUP_ID`,…]] [`[--clear-ssh-ec2-key-pair](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--clear-ssh-ec2-key-pair)`     | `[--ssh-ec2-key-pair](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--ssh-ec2-key-pair)`=`SSH_EC2_KEY_PAIR`] [`[--clear-tags](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--clear-tags)`     | `[--tags](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#TAG)`,…]] [`[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#--min-nodes)`=`MIN_NODES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Update a node pool in an Anthos cluster on AWS.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To update a node pool named ``my-node-pool`` in
a cluster named ``my-cluster`` managed in
location ``us-west1``, run:

```
gcloud container aws node-pools update my-node-pool --cluster=my-cluster --location=us-west1 --node-version=NODE_VERSION
```

**POSITIONAL ARGUMENTS**

: **Node pool resource - node pool to update. The arguments in this group can be
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--config-encryption-kms-key-arn**:
Amazon Resource Name (ARN) of the AWS KMS key to encrypt the user data.

**--enable-autorepair**:
Enable node autorepair feature for a node pool. Use --no-enable-autorepair to
disable.

```
gcloud container aws node-pools update --enable-autorepair
```

**--iam-instance-profile**:
Name or ARN of the IAM instance profile associated with the node pool.

**--instance-type**:
AWS EC2 instance type for the node pool's nodes.

**--max-surge-update**:
Maximum number of extra (surge) nodes to be created beyond the current size of
the node pool during its update process. Use --max-unavailable-update as well,
if needed, to control the overall surge settings.
To create an extra node each time the node pool is rolling updated, run:

```
gcloud container aws node-pools update --max-surge-update=1 --max-unavailable-update=0
```

**--max-unavailable-update**:
Maximum number of nodes that can be simultaneously unavailable during this node
pool's update process. Use --max-surge-update as well, if needed, to control the
overall surge settings.
To modify a node pool with 6 nodes such that, 3 nodes are updated in parallel (1
+ 2), but keep at least 4 nodes (6 - 2) available each time this node pool is
rolling updated, run:

```
gcloud container aws node-pools update --max-surge-update=1 --max-unavailable-update=2
```

**--node-version**:
Kubernetes version to use for the node pool.

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

**--validate-only**:
Validate the node pool to update, but don't actually perform it.

**--annotations**

**--clear-autoscaling-metrics**

**--clear-node-labels**

**--clear-proxy-config**

**--clear-security-group-ids**

**--clear-ssh-ec2-key-pair**

**--clear-tags**

**--max-nodes**

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
gcloud alpha container aws node-pools update
```