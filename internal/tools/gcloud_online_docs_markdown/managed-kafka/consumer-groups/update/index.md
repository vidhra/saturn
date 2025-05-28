# gcloud managed-kafka consumer-groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update)*

**NAME**

: **gcloud managed-kafka consumer-groups update - update a Managed Service for Apache Kafka consumer group**

**SYNOPSIS**

: **`gcloud managed-kafka consumer-groups update` (`[CONSUMER_GROUP](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update#CONSUMER_GROUP)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update#--location)`=`LOCATION`) `[--topics-file](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update#--topics-file)`=`JSON`|`[YAML](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update#YAML)`|`[FILE](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update#FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Managed Service for Apache Kafka consumer group.

**EXAMPLES**

: To specify a file for updating the topics of a consumer group, run the
following:

```
$gcloud managed-kafka consumer-groups update myconsumergroup |
    --cluster=mycluster \
    --location=us-central1 \
    --topics-file=topics.json
```

To update the topics of a consumer group with inline JSON, run the following:

```
$gcloud managed-kafka consumer-groups update myconsumergroup |
    --cluster=mycluster \
    --location=us-central1 \
    --topics-file='{"topic":{"partitions":{"0":{"offset":1,"metadata":"metadata"}}}}'
```

**POSITIONAL ARGUMENTS**

: **Consumer group resource - Identifies the consumer group to be updated. The
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

**REQUIRED FLAGS**

: **--topics-file**:
The path to the JSON or YAML file containing the configuration of the topics to
be updated for the consumer group. This also supports inline JSON or YAML.
Required, sets `topics_file` value.
`Input Example:`

```
--topics-file=string
```

`File Example:`

```
--topics-file=path_to_file.(yaml|json)
```

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
gcloud alpha managed-kafka consumer-groups update
```

```
gcloud beta managed-kafka consumer-groups update
```