# gcloud managed-kafka clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create)*

**NAME**

: **gcloud managed-kafka clusters create - create a Managed Service for Apache Kafka cluster**

**SYNOPSIS**

: **`gcloud managed-kafka clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--location)`=`LOCATION`) `[--cpu](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--cpu)`=`CPU` `[--memory](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--memory)`=`MEMORY` `[--subnets](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--subnets)`=[`SUBNETS`,…] [`[--async](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--async)`] [`[--no-auto-rebalance](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--auto-rebalance)`] [`[--encryption-key](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--encryption-key)`=`ENCRYPTION_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Managed Service for Apache Kafka cluster.

**EXAMPLES**

: To create a cluster, run the following:

```
gcloud managed-kafka clusters create mycluster --location=us-central1 --cpu=3 --memory=3GiB --subnets=projects/PROJECT_ID/regions/us-central1/subnetworks/default
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Identifies the cluster for which the command runs. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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
ID of the location of the Managed Service for Apache Kafka resource. See [https://cloud.google.com/managed-service-for-apache-kafka/docs/locations](https://cloud.google.com/managed-service-for-apache-kafka/docs/locations)
for a list of supported locations.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--cpu**:
The number of vCPUs to provision for the cluster. The minimum is 3.

**--memory**:
The memory to provision for the cluster in bytes. The value must be between 1
GiB and 8 GiB per vCPU. Ex. 1024Mi, 4Gi.

**--subnets**:
A comma-separated list of VPC subnets from which the cluster is accessible. Both
broker and bootstrap server IP addresses and DNS entries are automatically
created in each subnet. Only one subnet per network is allowed, and the subnet
must be located in the same region as the cluster. The project may differ. A
minimum of 1 subnet is required. A maximum of 10 subnets can be specified. Use
commas to separate multiple subnets. The name of the subnet must be in the
format
projects/``PROJECT_ID``/regions/``REGION``/subnetworks/``SUBNET``.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--auto-rebalance**:
Whether the automatic rebalancing is enabled. If automatic rebalancing is
enabled, topic partitions are rebalanced among brokers when the number of CPUs
in the cluster changes. Automatic rebalancing is enabled by default. Use
--no-auto-rebalance to disable this flag. Enabled by default, use
`--no-auto-rebalance` to disable.

**--encryption-key**:
The relative resource path of the Cloud KMS key to use for encryption in the
form:
projects/``PROJECT_ID``/locations/``LOCATION``/keyRings/``KEY_RING``/cryptoKeys/``KEY``.
The key must be located in the same region as the cluster. The key cannot be
changed once set.

**--labels**:
List of label KEY=VALUE pairs to add. Keys must start with a lowercase character
and contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers. Values must contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

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

**API REFERENCE**

: This command uses the `managedkafka/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/managed-service-for-apache-kafka/docs](https://cloud.google.com/managed-service-for-apache-kafka/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha managed-kafka clusters create
```

```
gcloud beta managed-kafka clusters create
```