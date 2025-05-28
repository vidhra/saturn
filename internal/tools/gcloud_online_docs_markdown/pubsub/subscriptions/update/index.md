# gcloud pubsub subscriptions update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update)*

**NAME**

: **gcloud pubsub subscriptions update - updates an existing Cloud Pub/Sub subscription**

**SYNOPSIS**

: **`gcloud pubsub subscriptions update` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#SUBSCRIPTION)` [`[--ack-deadline](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--ack-deadline)`=`ACK_DEADLINE`] [`[--enable-exactly-once-delivery](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--enable-exactly-once-delivery)`] [`[--expiration-period](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--expiration-period)`=`EXPIRATION_PERIOD`] [`[--message-retention-duration](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--message-retention-duration)`=`MESSAGE_RETENTION_DURATION`] [`[--retain-acked-messages](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--retain-acked-messages)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-bigquery-config](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--clear-bigquery-config)`     | [`[--bigquery-table](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--bigquery-table)`=`BIGQUERY_TABLE` : `[--bigquery-service-account-email](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--bigquery-service-account-email)`=`BIGQUERY_SERVICE_ACCOUNT_EMAIL` `[--drop-unknown-fields](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--drop-unknown-fields)` `[--write-metadata](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--write-metadata)` `[--use-table-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--use-table-schema)` | `[--use-topic-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--use-topic-schema)`]     | `[--clear-cloud-storage-config](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--clear-cloud-storage-config)`     | [`[--cloud-storage-bucket](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-bucket)`=`CLOUD_STORAGE_BUCKET` : `[--cloud-storage-file-datetime-format](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-file-datetime-format)`=`CLOUD_STORAGE_FILE_DATETIME_FORMAT` `[--cloud-storage-file-prefix](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-file-prefix)`=`CLOUD_STORAGE_FILE_PREFIX` `[--cloud-storage-file-suffix](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-file-suffix)`=`CLOUD_STORAGE_FILE_SUFFIX` `[--cloud-storage-max-bytes](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-max-bytes)`=`CLOUD_STORAGE_MAX_BYTES` `[--cloud-storage-max-duration](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-max-duration)`=`CLOUD_STORAGE_MAX_DURATION` `[--cloud-storage-max-messages](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-max-messages)`=`CLOUD_STORAGE_MAX_MESSAGES` `[--cloud-storage-output-format](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-output-format)`=`OUTPUT_FORMAT`; default="text" `[--cloud-storage-service-account-email](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-service-account-email)`=`CLOUD_STORAGE_SERVICE_ACCOUNT_EMAIL` `[--cloud-storage-use-topic-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-use-topic-schema)` `[--cloud-storage-write-metadata](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--cloud-storage-write-metadata)`]] [`[--clear-dead-letter-policy](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--clear-dead-letter-policy)`     | `[--max-delivery-attempts](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--max-delivery-attempts)`=`MAX_DELIVERY_ATTEMPTS` [`[--dead-letter-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--dead-letter-topic)`=`DEAD_LETTER_TOPIC` : `[--dead-letter-topic-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--dead-letter-topic-project)`=`DEAD_LETTER_TOPIC_PROJECT`]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--remove-labels)`=[`KEY`,…]] [`[--clear-message-transforms](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--clear-message-transforms)`     | `[--message-transforms-file](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--message-transforms-file)`=`MESSAGE_TRANSFORMS_FILE`] [`[--clear-retry-policy](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--clear-retry-policy)`     | `[--max-retry-delay](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--max-retry-delay)`=`MAX_RETRY_DELAY` `[--min-retry-delay](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--min-retry-delay)`=`MIN_RETRY_DELAY`] [`[--push-auth-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--push-auth-service-account)`=`SERVICE_ACCOUNT_EMAIL` `[--push-auth-token-audience](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--push-auth-token-audience)`=`OPTIONAL_AUDIENCE_OVERRIDE` `[--push-endpoint](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--push-endpoint)`=`PUSH_ENDPOINT` `[--clear-push-no-wrapper-config](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--clear-push-no-wrapper-config)`     | [`[--push-no-wrapper](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--push-no-wrapper)` : `[--push-no-wrapper-write-metadata](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#--push-no-wrapper-write-metadata)`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates an existing Cloud Pub/Sub subscription.

**POSITIONAL ARGUMENTS**

: **Subscription resource - Name of the subscription to update. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `subscription` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SUBSCRIPTION`**:
ID of the subscription or fully qualified identifier for the subscription.
To set the `subscription` attribute:

- provide the argument `subscription` on the command line.**

**FLAGS**

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

**--expiration-period**:
The subscription will expire if it is inactive for the given period. Valid
values are strings of the form INTEGER[UNIT], where UNIT is one of "s", "m",
"h", and "d" for seconds, minutes, hours, and days, respectively. If the unit is
omitted, seconds is assumed. This flag additionally accepts the special value
"never" to indicate that the subscription will never expire.

**--message-retention-duration**:
How long to retain unacknowledged messages in the subscription's backlog, from
the moment a message is published. If --retain-acked-messages is true, this also
configures the retention of acknowledged messages. Specify "default" to use the
default value of 7 days. The minimum is 10 minutes, and the maximum is 31 days.
Valid values are strings of the form INTEGER[UNIT], where UNIT is one of "s",
"m", "h", and "d" for seconds, minutes, hours, and days, respectively. If the
unit is omitted, seconds is assumed.

**--retain-acked-messages**:
Whether or not to retain acknowledged messages. If true, messages are not
expunged from the subscription's backlog until they fall out of the
--message-retention-duration window. Acknowledged messages are not retained by
default. Use --no-retain-acked-messages to disable this flag.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-bigquery-config**

**--clear-dead-letter-policy**

**--clear-labels**

**--clear-message-transforms**

**--clear-retry-policy**

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
gcloud alpha pubsub subscriptions update
```

```
gcloud beta pubsub subscriptions update
```