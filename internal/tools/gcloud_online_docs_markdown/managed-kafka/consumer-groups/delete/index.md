# gcloud managed-kafka consumer-groups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/delete](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/delete)*

**NAME**

: **gcloud managed-kafka consumer-groups delete - delete a Managed Service for Apache Kafka consumer group**

**SYNOPSIS**

: **`gcloud managed-kafka consumer-groups delete` (`[CONSUMER_GROUP](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/delete#CONSUMER_GROUP)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/delete#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Managed Service for Apache Kafka consumer group.

**EXAMPLES**

: To delete a consumer group in a cluster named mycluster located in us-central1,
run the following:

```
gcloud managed-kafka consumer-groups delete myconsumergroup --cluster=mycluster --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Consumer group resource - Identifies the consumer group for deletion. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `consumer_group` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONSUMER_GROUP`**:
ID of the consumer_group or fully qualified identifier for the consumer_group.
To set the `consumer_group` attribute:

- provide the argument `consumer_group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The cluster name.
To set the `cluster` attribute:

- provide the argument `consumer_group` on the command line with a
fully specified name;
- provide the argument `--cluster` on the command line.

**--location**:
ID of the location of the Managed Service for Apache Kafka resource. See [https://cloud.google.com/managed-service-for-apache-kafka/docs/locations](https://cloud.google.com/managed-service-for-apache-kafka/docs/locations)
for a list of supported locations.
To set the `location` attribute:

- provide the argument `consumer_group` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

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
gcloud alpha managed-kafka consumer-groups delete
```

```
gcloud beta managed-kafka consumer-groups delete
```