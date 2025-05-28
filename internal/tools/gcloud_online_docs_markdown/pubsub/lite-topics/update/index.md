# gcloud pubsub lite-topics update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update)*

**NAME**

: **gcloud pubsub lite-topics update - update a Pub/Sub Lite topic**

**SYNOPSIS**

: **`gcloud pubsub lite-topics update` (`[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#TOPIC)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#--location)`=`LOCATION`) (`[--message-retention-period](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#--message-retention-period)`=`MESSAGE_RETENTION_PERIOD` `[--partitions](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#--partitions)`=`PARTITIONS` `[--per-partition-bytes](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#--per-partition-bytes)`=`PER_PARTITION_BYTES` `[--per-partition-publish-mib](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#--per-partition-publish-mib)`=`PER_PARTITION_PUBLISH_MIB` `[--per-partition-subscribe-mib](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#--per-partition-subscribe-mib)`=`PER_PARTITION_SUBSCRIBE_MIB` `[--throughput-reservation](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#--throughput-reservation)`=`THROUGHPUT_RESERVATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Pub/Sub Lite topic.

**EXAMPLES**

: To update a Pub/Sub Lite topic, run:

```
gcloud pubsub lite-topics update mytopic --location=us-central1-a --per-partition-publish-mib=10
```

**POSITIONAL ARGUMENTS**

: **Topic resource - Topic to update. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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

**--location**:
ID of the location of the Pub/Sub Lite resource.
To set the `location` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--message-retention-period**

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
gcloud alpha pubsub lite-topics update
```

```
gcloud beta pubsub lite-topics update
```