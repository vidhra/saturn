# gcloud container aws clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create)*

**NAME**

: **gcloud container aws clusters create - create an Anthos cluster on AWS**

**SYNOPSIS**

: **`gcloud container aws clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--location)`=`LOCATION`) `[--aws-region](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--aws-region)`=`AWS_REGION` `[--cluster-version](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--cluster-version)`=`CLUSTER_VERSION` `[--config-encryption-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--config-encryption-kms-key-arn)`=`CONFIG_ENCRYPTION_KMS_KEY_ARN` `[--database-encryption-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--database-encryption-kms-key-arn)`=`DATABASE_ENCRYPTION_KMS_KEY_ARN` `[--fleet-project](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--fleet-project)`=`FLEET_PROJECT` `[--iam-instance-profile](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--iam-instance-profile)`=`IAM_INSTANCE_PROFILE` `[--pod-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--pod-address-cidr-blocks)`=`POD_ADDRESS_CIDR_BLOCKS` `[--role-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--role-arn)`=`ROLE_ARN` `[--service-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--service-address-cidr-blocks)`=`SERVICE_ADDRESS_CIDR_BLOCKS` `[--subnet-ids](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--subnet-ids)`=[`SUBNET_ID`,…] `[--vpc-id](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--vpc-id)`=`VPC_ID` [`[--admin-groups](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--admin-groups)`=[`GROUP`,…]] [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--admin-users)`=`USER`,[`[USER](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#USER)`,…]] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#ANNOTATION)`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--async)`] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--description)`=`DESCRIPTION`] [`[--disable-per-node-pool-sg-rules](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--disable-per-node-pool-sg-rules)`] [`[--enable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--enable-managed-prometheus)`] [`[--instance-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--instance-type)`=`INSTANCE_TYPE`] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--logging)`=`COMPONENT`,[`[COMPONENT](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#COMPONENT)`,…]] [`[--main-volume-iops](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--main-volume-iops)`=`MAIN_VOLUME_IOPS`] [`[--main-volume-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--main-volume-kms-key-arn)`=`MAIN_VOLUME_KMS_KEY_ARN`] [`[--main-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--main-volume-size)`=`MAIN_VOLUME_SIZE`] [`[--main-volume-throughput](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--main-volume-throughput)`=`MAIN_VOLUME_THROUGHPUT`] [`[--main-volume-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--main-volume-type)`=`MAIN_VOLUME_TYPE`] [`[--role-session-name](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--role-session-name)`=`ROLE_SESSION_NAME`] [`[--root-volume-iops](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--root-volume-iops)`=`ROOT_VOLUME_IOPS`] [`[--root-volume-kms-key-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--root-volume-kms-key-arn)`=`ROOT_VOLUME_KMS_KEY_ARN`] [`[--root-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--root-volume-size)`=`ROOT_VOLUME_SIZE`] [`[--root-volume-throughput](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--root-volume-throughput)`=`ROOT_VOLUME_THROUGHPUT`] [`[--root-volume-type](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--root-volume-type)`=`ROOT_VOLUME_TYPE`] [`[--security-group-ids](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--security-group-ids)`=[`SECURITY_GROUP_ID`,…]] [`[--ssh-ec2-key-pair](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--ssh-ec2-key-pair)`=`SSH_EC2_KEY_PAIR`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#TAG)`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--validate-only)`] [`[--proxy-secret-arn](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--proxy-secret-arn)`=`PROXY_SECRET_ARN` `[--proxy-secret-version-id](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--proxy-secret-version-id)`=`PROXY_SECRET_VERSION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Create an Anthos cluster on AWS.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To create a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container aws clusters create my-cluster --location=us-west1 --aws-region=AWS_REGION --cluster-version=CLUSTER_VERSION --database-encryption-kms-key-arn=KMS_KEY_ARN --iam-instance-profile=IAM_INSTANCE_PROFILE --pod-address-cidr-blocks=POD_ADDRESS_CIDR_BLOCKS --role-arn=ROLE_ARN --service-address-cidr-blocks=SERVICE_ADDRESS_CIDR_BLOCKS --subnet-ids=SUBNET_ID --vpc-id=VPC_ID
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to create. The arguments in this group can be used to
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

**REQUIRED FLAGS**

: **--aws-region**:
AWS region to deploy the cluster.

**--cluster-version**:
Kubernetes version to use for the cluster.

**--config-encryption-kms-key-arn**:
Amazon Resource Name (ARN) of the AWS KMS key to encrypt the user data.

**--database-encryption-kms-key-arn**:
Amazon Resource Name (ARN) of the AWS KMS key to encrypt the cluster secrets.

**--fleet-project**:
ID or number of the Fleet host project where the cluster is registered.

**--iam-instance-profile**:
Name or ARN of the IAM instance profile associated with the cluster.

**--pod-address-cidr-blocks**:
IP address range for the pods in this cluster in CIDR notation (e.g.
10.0.0.0/8).

**--role-arn**:
Amazon Resource Name (ARN) of the IAM role to assume when managing AWS
resources.

**--service-address-cidr-blocks**:
IP address range for the services IPs in CIDR notation (e.g. 10.0.0.0/8).

**--subnet-ids**:
Subnet ID of an existing VNET to use for the cluster control plane.

**--vpc-id**:
VPC associated with the cluster.

**OPTIONAL FLAGS**

: **--admin-groups**:
Groups of users that can perform operations as a cluster administrator.

**--admin-users**:
Users that can perform operations as a cluster administrator. If not specified,
the value of property core/account is used.

**--annotations**:
Annotations for the cluster.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--binauthz-evaluation-mode**:
Set Binary Authorization evaluation mode for this cluster.
`BINAUTHZ_EVALUATION_MODE` must be one of:
`DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`.

**--description**:
Description for the cluster.

**--disable-per-node-pool-sg-rules**:
Disable the default per node pool subnet security group rules on the control
plane security group. When disabled, at least one security group that allows
node pools to send traffic to the control plane on ports TCP/443 and TCP/8132
must be provided.

**--enable-managed-prometheus**:
Enables managed collection for Managed Service for Prometheus in the cluster.
See [https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke)
for more info.
Managed Prometheus is enabled by default for cluster versions 1.27 or greater,
use --no-enable-managed-prometheus to disable.

**--instance-type**:
AWS EC2 instance type for the control plane's nodes.

**--logging**:
Set the components that have logging enabled.
Examples:

```
gcloud container aws clusters create --logging=SYSTEM
gcloud container aws clusters create --logging=SYSTEM,WORKLOAD
```

`COMPONENT` must be one of: `SYSTEM`,
`WORKLOAD`.

**--main-volume-iops**:
Number of I/O operations per second (IOPS) to provision for the main volume.

**--main-volume-kms-key-arn**:
Amazon Resource Name (ARN) of the AWS KMS key to encrypt the main volume.

**--main-volume-size**:
Size of the main volume. The value must be a whole number followed by a size
unit of `GB` for gigabyte, or `TB` for terabyte. If no
size unit is specified, GB is assumed.

**--main-volume-throughput**:
Throughput to provision for the main volume, in MiB/s. Only valid if the volume
type is GP3. If volume type is GP3 and throughput is not provided, it defaults
to 125.

**--main-volume-type**:
Type of the main volume. `MAIN_VOLUME_TYPE` must be one
of: `gp2`, `gp3`.

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

**--security-group-ids**:
IDs of additional security groups to add to the control plane's nodes.

**--ssh-ec2-key-pair**:
Name of the EC2 key pair authorized to login to the control plane's nodes.

**--tags**:
Applies the given tags (comma separated) on the cluster. Example:

```
gcloud container aws clusters create EXAMPLE_CLUSTER --tags=tag1=one,tag2=two
```

**--validate-only**:
Validate the cluster to create, but don't actually perform it.

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
gcloud alpha container aws clusters create
```