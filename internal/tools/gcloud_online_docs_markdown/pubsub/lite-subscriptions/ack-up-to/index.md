# gcloud pubsub lite-subscriptions ack-up-to  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/ack-up-to](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/ack-up-to)*

**NAME**

: **gcloud pubsub lite-subscriptions ack-up-to - acknowledge messages on a Pub/Sub Lite subscription**

**SYNOPSIS**

: **`gcloud pubsub lite-subscriptions ack-up-to` (`[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/ack-up-to#SUBSCRIPTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/ack-up-to#--location)`=`LOCATION`) `[--offset](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/ack-up-to#--offset)`=`OFFSET` `[--partition](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/ack-up-to#--partition)`=`PARTITION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/ack-up-to#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Acknowledge all messages on a Pub/Sub Lite subscription up to the provided
offset. The message corresponding to the provided offset will be included in the
list of messages that are acknowledged.

**EXAMPLES**

: To acknowledge messages on a Pub/Sub Lite subscription, run:

```
gcloud pubsub lite-subscriptions ack-up-to mysubscription --location=us-central1-a --partition=0 --offset=10
```

**POSITIONAL ARGUMENTS**

: **Subscription resource - Subscription on which to acknowledge messages. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `subscription` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SUBSCRIPTION`**:
ID of the subscription or fully qualified identifier for the subscription.
To set the `subscription` attribute:

- provide the argument `subscription` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location of the Pub/Sub Lite resource.
To set the `location` attribute:

- provide the argument `subscription` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--offset**:
The offset of a message within a topic partition. Must be greater than or equal
to 0.

**--partition**:
The topic partition. Partitions are zero indexed, so the partition must be in
the range [0, topic.num_partitions). If you do not know your
topic.num_partitions, run `gcloud pubsub lite-topic describe TOPIC
--location=ZONE`.

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
gcloud alpha pubsub lite-subscriptions ack-up-to
```

```
gcloud beta pubsub lite-subscriptions ack-up-to
```