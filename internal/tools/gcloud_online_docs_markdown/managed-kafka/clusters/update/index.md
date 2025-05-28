# gcloud managed-kafka clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update)*

**NAME**

: **gcloud managed-kafka clusters update - update a Managed Service for Apache Kafka cluster**

**SYNOPSIS**

: **`gcloud managed-kafka clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#--location)`=`LOCATION`) (`[--auto-rebalance](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#--auto-rebalance)` `[--cpu](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#--cpu)`=`CPU` `[--labels](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#--labels)`=[`KEY`=`VALUE`,…] `[--memory](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#--memory)`=`MEMORY` `[--subnets](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#--subnets)`=[`SUBNETS`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Managed Service for Apache Kafka cluster.

**EXAMPLES**

: To update an attribute in a cluster named mycluster located in us-central1, such
as the CPU, run the following:

```
gcloud managed-kafka clusters update mycluster --location=us-central1 --cpu=3
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Identifies the cluster to be updated. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

: **--auto-rebalance**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha managed-kafka clusters update
```

```
gcloud beta managed-kafka clusters update
```