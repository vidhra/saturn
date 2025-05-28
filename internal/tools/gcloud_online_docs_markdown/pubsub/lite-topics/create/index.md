# gcloud pubsub lite-topics create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create)*

**NAME**

: **gcloud pubsub lite-topics create - create a Pub/Sub Lite topic**

**SYNOPSIS**

: **`gcloud pubsub lite-topics create` `[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#TOPIC)` `[--partitions](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#--partitions)`=`PARTITIONS` `[--per-partition-bytes](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#--per-partition-bytes)`=`PER_PARTITION_BYTES` [`[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#--location)`=`LOCATION`] [`[--message-retention-period](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#--message-retention-period)`=`MESSAGE_RETENTION_PERIOD`] [`[--per-partition-publish-mib](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#--per-partition-publish-mib)`=`PER_PARTITION_PUBLISH_MIB`] [`[--per-partition-subscribe-mib](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#--per-partition-subscribe-mib)`=`PER_PARTITION_SUBSCRIBE_MIB`] [`[--throughput-reservation](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#--throughput-reservation)`=`THROUGHPUT_RESERVATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Pub/Sub Lite topic.

**EXAMPLES**

: To create a Pub/Sub lite-topic, run:

```
gcloud pubsub lite-topics create mytopic --location=us-central1-a --partitions=1 --per-partition-bytes=30GiB --message-retention-period=2w
```

**POSITIONAL ARGUMENTS**

: **`TOPIC`**:
Topic ID.

**REQUIRED FLAGS**

: **--partitions**:
Number of partitions in the topic.

**--per-partition-bytes**:
Provisioned storage, in bytes, per partition. If the number of bytes stored in
any of the topic's partitions exceeds this value, older messages will be dropped
to make room for newer ones, regardless of the value of
`message-retention-period`. A valid example value of this flag would
be `per-partition-bytes=30GiB`.

**OPTIONAL FLAGS**

: **Location resource - Identifies the Cloud zone this command will be executed on.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- provide the argument `--zone` on the command line.**

**--message-retention-period**:
How long a published message is retained. If unset, messages will only be
dropped to make space for new ones once the `per-partition-bytes`
limit is reached. A valid example value of this flag would be
`message-retention-period="2w"`.

**--per-partition-publish-mib**:
Topic partition publish throughput capacity in MiB/s. Must be between 4 and 16.

**--per-partition-subscribe-mib**:
Topic partition subscribe throughput capacity in MiB/s. Must be between 4 and
32.

**--throughput-reservation**:
Reservation ID to use for topic throughput.

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

: This command uses the `pubsublite/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/pubsub/lite/docs](https://cloud.google.com/pubsub/lite/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha pubsub lite-topics create
```

```
gcloud beta pubsub lite-topics create
```