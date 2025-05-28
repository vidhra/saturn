# gcloud pubsub lite-subscriptions create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create)*

**NAME**

: **gcloud pubsub lite-subscriptions create - create a Pub/Sub Lite subscription**

**SYNOPSIS**

: **`gcloud pubsub lite-subscriptions create` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#SUBSCRIPTION)` `[--topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--topic)`=`TOPIC` [`[--delivery-requirement](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--delivery-requirement)`=`DELIVERY_REQUIREMENT`; default="deliver-immediately"] [`[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--location)`=`LOCATION`] [`[--event-time](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--event-time)`=`EVENT_TIME`     | `[--publish-time](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--publish-time)`=`PUBLISH_TIME`     | `[--starting-offset](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--starting-offset)`=`STARTING_OFFSET`; default="end"] [`[--export-pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--export-pubsub-topic)`=`EXPORT_PUBSUB_TOPIC` : `[--export-dead-letter-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--export-dead-letter-topic)`=`EXPORT_DEAD_LETTER_TOPIC` `[--export-desired-state](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#--export-desired-state)`=`EXPORT_DESIRED_STATE`; default="active"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Pub/Sub Lite subscription.

**EXAMPLES**

: To create a Pub/Sub Lite subscription, run:

```
gcloud pubsub lite-subscriptions create mysubscription --location=us-central1-a --topic=mytopic
```

To create a Pub/Sub Lite subscription at the offset of the oldest retained
message, run:

```
gcloud pubsub lite-subscriptions create mysubscription --location=us-central1-a --topic=mytopic --starting-offset=beginning
```

To create a Pub/Sub Lite subscription that exports messages from a Pub/Sub Lite
topic to a Pub/Sub topic, run:

```
gcloud pubsub lite-subscriptions create mysubscription --location=us-central1-a --topic=mytopic --export-pubsub-topic=pubsubtopic
```

**POSITIONAL ARGUMENTS**

: **`SUBSCRIPTION`**:
Subscription ID.

**REQUIRED FLAGS**

: **--topic**:
Topic ID associated with the subscription.

**OPTIONAL FLAGS**

: **--delivery-requirement**:
When this subscription should send messages to subscribers relative to messages
persistence in storage. See [https://cloud.google.com/pubsub/lite/docs/subscriptions#creating_lite_subscriptions](https://cloud.google.com/pubsub/lite/docs/subscriptions#creating_lite_subscriptions)
for more info. `DELIVERY_REQUIREMENT` must be one of:
`deliver-after-stored`, `deliver-immediately`.

**Location resource - Identifies the Cloud zone this command will be executed on.
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

**--event-time**

**--export-pubsub-topic**:
The name of the destination Pub/Sub topic to which messages are exported. Must
be the topic's fully specified path if it is not in the same project as the
subscription to be created.

**--export-dead-letter-topic**:
The name of the Pub/Sub Lite topic to write messages that cannot be exported.
Must be in the same project and location as the subscription to be created. Note
that this is a Lite topic.

**--export-desired-state**:
The desired state of the export. Process messages by setting the value to ACTIVE
or pause message processing by setting the value to PAUSED.
`EXPORT_DESIRED_STATE` must be one of:
`active`, `paused`.

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
gcloud alpha pubsub lite-subscriptions create
```

```
gcloud beta pubsub lite-subscriptions create
```