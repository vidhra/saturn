# gcloud pubsub subscriptions create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create)*

**NAME**

: **gcloud pubsub subscriptions create - creates one or more Cloud Pub/Sub subscriptions**

**SYNOPSIS**

: **`gcloud pubsub subscriptions create` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#SUBSCRIPTION)` [`[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#SUBSCRIPTION)` …] (`[--topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--topic)`=`TOPIC` : `[--topic-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--topic-project)`=`TOPIC_PROJECT`) [`[--ack-deadline](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--ack-deadline)`=`ACK_DEADLINE`] [`[--enable-exactly-once-delivery](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--enable-exactly-once-delivery)`] [`[--enable-message-ordering](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--enable-message-ordering)`] [`[--expiration-period](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--expiration-period)`=`EXPIRATION_PERIOD`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--message-filter](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--message-filter)`=`MESSAGE_FILTER`] [`[--message-retention-duration](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--message-retention-duration)`=`MESSAGE_RETENTION_DURATION`] [`[--message-transforms-file](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--message-transforms-file)`=`MESSAGE_TRANSFORMS_FILE`] [`[--retain-acked-messages](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--retain-acked-messages)`] [[`[--bigquery-table](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--bigquery-table)`=`BIGQUERY_TABLE` : `[--bigquery-service-account-email](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--bigquery-service-account-email)`=`BIGQUERY_SERVICE_ACCOUNT_EMAIL` `[--drop-unknown-fields](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--drop-unknown-fields)` `[--write-metadata](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--write-metadata)` `[--use-table-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--use-table-schema)` | `[--use-topic-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--use-topic-schema)`]     | [`[--cloud-storage-bucket](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-bucket)`=`CLOUD_STORAGE_BUCKET` : `[--cloud-storage-file-datetime-format](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-file-datetime-format)`=`CLOUD_STORAGE_FILE_DATETIME_FORMAT` `[--cloud-storage-file-prefix](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-file-prefix)`=`CLOUD_STORAGE_FILE_PREFIX` `[--cloud-storage-file-suffix](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-file-suffix)`=`CLOUD_STORAGE_FILE_SUFFIX` `[--cloud-storage-max-bytes](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-max-bytes)`=`CLOUD_STORAGE_MAX_BYTES` `[--cloud-storage-max-duration](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-max-duration)`=`CLOUD_STORAGE_MAX_DURATION` `[--cloud-storage-max-messages](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-max-messages)`=`CLOUD_STORAGE_MAX_MESSAGES` `[--cloud-storage-output-format](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-output-format)`=`OUTPUT_FORMAT`; default="text" `[--cloud-storage-service-account-email](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-service-account-email)`=`CLOUD_STORAGE_SERVICE_ACCOUNT_EMAIL` `[--cloud-storage-use-topic-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-use-topic-schema)` `[--cloud-storage-write-metadata](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--cloud-storage-write-metadata)`]] [`[--max-delivery-attempts](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--max-delivery-attempts)`=`MAX_DELIVERY_ATTEMPTS` [`[--dead-letter-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--dead-letter-topic)`=`DEAD_LETTER_TOPIC` : `[--dead-letter-topic-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--dead-letter-topic-project)`=`DEAD_LETTER_TOPIC_PROJECT`]] [`[--max-retry-delay](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--max-retry-delay)`=`MAX_RETRY_DELAY` `[--min-retry-delay](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--min-retry-delay)`=`MIN_RETRY_DELAY`] [`[--push-auth-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--push-auth-service-account)`=`SERVICE_ACCOUNT_EMAIL` `[--push-auth-token-audience](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--push-auth-token-audience)`=`OPTIONAL_AUDIENCE_OVERRIDE` `[--push-endpoint](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--push-endpoint)`=`PUSH_ENDPOINT` [`[--push-no-wrapper](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--push-no-wrapper)` : `[--push-no-wrapper-write-metadata](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#--push-no-wrapper-write-metadata)`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates one or more Cloud Pub/Sub subscriptions for a given topic. The new
subscription defaults to a PULL subscription unless a push endpoint is
specified.

**POSITIONAL ARGUMENTS**

: **Subscription resource - One or more subscriptions to create. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `subscription` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SUBSCRIPTION` [`SUBSCRIPTION` …]**:
IDs of the subscriptions or fully qualified identifiers for the subscriptions.
To set the `subscription` attribute:

- provide the argument `subscription` on the command line.**

**REQUIRED FLAGS**

: **--topic**

**OPTIONAL FLAGS**

: **--ack-deadline**:
The number of seconds the system will wait for a subscriber to acknowledge
receiving a message before re-attempting delivery.

**--enable-exactly-once-delivery**:
Whether or not to enable exactly-once delivery on the subscription. If true,
Pub/Sub provides the following guarantees for the delivery of a message with a
given value of `message_id` on this subscription: The message sent to
a subscriber is guaranteed not to be resent before the message's acknowledgment
deadline expires. An acknowledged message will not be resent to a subscriber.
Use --no-enable-exactly-once-delivery to disable this flag.

**--enable-message-ordering**:
Whether to receive messages with the same ordering key in order. If set,
messages with the same ordering key are sent to subscribers in the order that
Pub/Sub receives them. Use --no-enable-message-ordering to disable this flag.

**--expiration-period**:
The subscription will expire if it is inactive for the given period. Valid
values are strings of the form INTEGER[UNIT], where UNIT is one of "s", "m",
"h", and "d" for seconds, minutes, hours, and days, respectively. If the unit is
omitted, seconds is assumed. This flag additionally accepts the special value
"never" to indicate that the subscription will never expire.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--message-filter**:
Expression to filter messages. If set, Pub/Sub only delivers the messages that
match the filter. The expression must be a non-empty string in the [Pub/Sub filtering
language](https://cloud.google.com/pubsub/docs/filtering).

**--message-retention-duration**:
How long to retain unacknowledged messages in the subscription's backlog, from
the moment a message is published. If --retain-acked-messages is true, this also
configures the retention of acknowledged messages. The default value is 7 days,
the minimum is 10 minutes, and the maximum is 31 days. Valid values are strings
of the form INTEGER[UNIT], where UNIT is one of "s", "m", "h", and "d" for
seconds, minutes, hours, and days, respectively. If the unit is omitted, seconds
is assumed.

**--message-transforms-file**:
Path to YAML or JSON file containing message transforms.

**--retain-acked-messages**:
Whether or not to retain acknowledged messages. If true, messages are not
expunged from the subscription's backlog until they fall out of the
--message-retention-duration window. Acknowledged messages are not retained by
default. Use --no-retain-acked-messages to disable this flag.

**--bigquery-table**

**--max-delivery-attempts**

**--max-retry-delay**

**--push-auth-service-account**

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
gcloud alpha pubsub subscriptions create
```

```
gcloud beta pubsub subscriptions create
```