# gcloud container aws clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update)*

**NAME**

: **gcloud container aws clusters update - update an Anthos cluster on AWS**

**SYNOPSIS**

: **`gcloud container aws clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--location)`=`LOCATION`) [`[--admin-groups](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--admin-groups)`=[`GROUP`,…]] [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--admin-users)`=`USER`,[`[USER](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#USER)`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--async)`] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--cluster-version](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--cluster-version)`=`CLUSTER_VERSION`] [`[--config-encryption-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--config-encryption-kms-key-arn)`=`CONFIG_ENCRYPTION_KMS_KEY_ARN`] [`[--iam-instance-profile](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--iam-instance-profile)`=`IAM_INSTANCE_PROFILE`] [`[--instance-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--instance-type)`=`INSTANCE_TYPE`] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--logging)`=`COMPONENT`,[`[COMPONENT](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#COMPONENT)`,…]] [`[--role-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--role-arn)`=`ROLE_ARN`] [`[--role-session-name](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--role-session-name)`=`ROLE_SESSION_NAME`] [`[--root-volume-iops](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--root-volume-iops)`=`ROOT_VOLUME_IOPS`] [`[--root-volume-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--root-volume-kms-key-arn)`=`ROOT_VOLUME_KMS_KEY_ARN`] [`[--root-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--root-volume-size)`=`ROOT_VOLUME_SIZE`] [`[--root-volume-throughput](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--root-volume-throughput)`=`ROOT_VOLUME_THROUGHPUT`] [`[--root-volume-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--root-volume-type)`=`ROOT_VOLUME_TYPE`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--validate-only)`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#ANNOTATION)`,…]     | `[--clear-annotations](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--clear-annotations)`] [`[--clear-description](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--clear-description)`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--description)`=`DESCRIPTION`] [`[--clear-proxy-config](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--clear-proxy-config)`     | `[--proxy-secret-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--proxy-secret-arn)`=`PROXY_SECRET_ARN` `[--proxy-secret-version-id](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--proxy-secret-version-id)`=`PROXY_SECRET_VERSION_ID`] [`[--clear-security-group-ids](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--clear-security-group-ids)`     | `[--security-group-ids](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--security-group-ids)`=[`SECURITY_GROUP_ID`,…]] [`[--clear-ssh-ec2-key-pair](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--clear-ssh-ec2-key-pair)`     | `[--ssh-ec2-key-pair](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--ssh-ec2-key-pair)`=`SSH_EC2_KEY_PAIR`] [`[--clear-tags](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--clear-tags)`     | `[--tags](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#TAG)`,…]] [`[--disable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--disable-managed-prometheus)`     | `[--enable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--enable-managed-prometheus)`] [`[--disable-per-node-pool-sg-rules](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--disable-per-node-pool-sg-rules)`     | `[--enable-per-node-pool-sg-rules](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#--enable-per-node-pool-sg-rules)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Update an Anthos cluster on AWS.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To update a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container aws clusters update my-cluster --location=us-west1 --cluster-version=CLUSTER_VERSION
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to update. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the cluster.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_aws/location`.**

**FLAGS**

: **--admin-groups**:
Groups of users that can perform operations as a cluster administrator.

**--admin-users**:
Users that can perform operations as a cluster administrator.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--binauthz-evaluation-mode**:
Set Binary Authorization evaluation mode for this cluster.
`BINAUTHZ_EVALUATION_MODE` must be one of:
`DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`.

**--cluster-version**:
Kubernetes version to use for the cluster.

**--config-encryption-kms-key-arn**:
Amazon Resource Name (ARN) of the AWS KMS key to encrypt the user data.

**--iam-instance-profile**:
Name or ARN of the IAM instance profile associated with the cluster.

**--instance-type**:
AWS EC2 instance type for the control plane's nodes.

**--logging**:
Set the components that have logging enabled.
Examples:

```
gcloud container aws clusters update --logging=SYSTEM
gcloud container aws clusters update --logging=SYSTEM,WORKLOAD
```

`COMPONENT` must be one of: `SYSTEM`,
`WORKLOAD`.

**--role-arn**:
Amazon Resource Name (ARN) of the IAM role to assume when managing AWS
resources.

**--role-session-name**:
Identifier for the assumed role session.

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
Validate the update of the cluster, but don't actually perform it.

**--annotations**

**--clear-description**

**--clear-proxy-config**

**--clear-security-group-ids**

**--clear-ssh-ec2-key-pair**

**--clear-tags**

**--disable-managed-prometheus**

**--disable-per-node-pool-sg-rules**

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
gcloud alpha container aws clusters update
```