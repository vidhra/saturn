# gcloud managed-kafka topics create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create)*

**NAME**

: **gcloud managed-kafka topics create - create a Managed Service for Apache Kafka topic**

**SYNOPSIS**

: **`gcloud managed-kafka topics create` (`[TOPIC](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create#TOPIC)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create#--location)`=`LOCATION`) `[--partitions](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create#--partitions)`=`PARTITIONS` `[--replication-factor](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create#--replication-factor)`=`REPLICATION_FACTOR` [`[--configs](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create#--configs)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Managed Service for Apache Kafka topic.

**EXAMPLES**

: To create a topic in a cluster named mycluster located in us-central1, run the
following:

```
gcloud managed-kafka topics create mytopic --cluster=mycluster --location=us-central1 --partitions=1 --replication-factor=3
```

**POSITIONAL ARGUMENTS**

: **Topic resource - Identifies the name of the topic that this command creates. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TOPIC`**:
ID of the topic or fully qualified identifier for the topic.
To set the `topic` attribute:

- provide the argument `topic` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The cluster name.
To set the `cluster` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--location**:
ID of the location of the Managed Service for Apache Kafka resource. See [https://cloud.google.com/managed-service-for-apache-kafka/docs/locations](https://cloud.google.com/managed-service-for-apache-kafka/docs/locations)
for a list of supported locations.
To set the `location` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--partitions**:
The number of partitions in a topic. You can increase the partition count for a
topic, but you cannot decrease it. Increasing partitions for a topic that uses a
key might change how messages are distributed.

**--replication-factor**:
The number of replicas of each partition. A replication factor of 3 is
recommended for high availability.

**OPTIONAL FLAGS**

: **--configs**:
Configuration for the topic that are overridden from the cluster defaults. The
key of the map is a Kafka topic property name, for example:
`cleanup.policy=compact`,`compression.type=producer`. If
you provide a map with a key that already exists, only that configuration is
updated. If the map contains a key that does not exist, the entry is appended to
the topic configuration.

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
gcloud alpha managed-kafka topics create
```

```
gcloud beta managed-kafka topics create
```