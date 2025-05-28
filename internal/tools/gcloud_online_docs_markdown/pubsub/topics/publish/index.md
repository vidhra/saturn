# gcloud pubsub topics publish  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish)*

**NAME**

: **gcloud pubsub topics publish - publishes a message to the specified topic**

**SYNOPSIS**

: **`gcloud pubsub topics publish` `[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish#TOPIC)` [`[--attribute](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish#--attribute)`=[`ATTRIBUTE`,…]] [`[--message](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish#--message)`=`MESSAGE`] [`[--ordering-key](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish#--ordering-key)`=`ORDERING_KEY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Publishes a message to the specified topic name for testing and troubleshooting.
Use with caution: all associated subscribers must be able to consume and
acknowledge any message you publish, otherwise the system will continuously
re-attempt delivery of the bad message for 7 days.

**EXAMPLES**

: To publish messages in a batch to a specific Cloud Pub/Sub topic, run:

```
gcloud pubsub topics publish mytopic --message="Hello World!" --attribute=KEY1=VAL1,KEY2=VAL2
```

**POSITIONAL ARGUMENTS**

: **Topic resource - Name of the topic to publish messages to. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TOPIC`**:
ID of the topic or fully qualified identifier for the topic.
To set the `topic` attribute:

- provide the argument `topic` on the command line.**

**FLAGS**

: **--attribute**:
Comma-separated list of attributes. Each ATTRIBUTE has the form name="value".
You can specify up to 100 attributes.

**--message**:
The body of the message to publish to the given topic name. Information on
message formatting and size limits can be found at: [https://cloud.google.com/pubsub/docs/publisher#publish](https://cloud.google.com/pubsub/docs/publisher#publish)

**--ordering-key**:
The key for ordering delivery to subscribers. All messages with the same
ordering key are sent to subscribers in the order that Pub/Sub receives them.

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

: These variants are also available:

```
gcloud alpha pubsub topics publish
```

```
gcloud beta pubsub topics publish
```