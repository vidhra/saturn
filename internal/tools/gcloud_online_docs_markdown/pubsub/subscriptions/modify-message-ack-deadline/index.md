# gcloud pubsub subscriptions modify-message-ack-deadline  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-message-ack-deadline](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-message-ack-deadline)*

**NAME**

: **gcloud pubsub subscriptions modify-message-ack-deadline - modifies the ACK deadline for a specific Cloud Pub/Sub message**

**SYNOPSIS**

: **`gcloud pubsub subscriptions modify-message-ack-deadline` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-message-ack-deadline#SUBSCRIPTION)` `[--ack-deadline](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-message-ack-deadline#--ack-deadline)`=`ACK_DEADLINE` `[--ack-ids](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-message-ack-deadline#--ack-ids)`=[`ACK_ID`,…] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-message-ack-deadline#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This method is useful to indicate that more time is needed to process a message
by the subscriber, or to make the message available for redelivery if the
processing was interrupted.

**POSITIONAL ARGUMENTS**

: **Subscription resource - Name of the subscription messages belong to. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--ack-deadline**:
The number of seconds the system will wait for a subscriber to acknowledge
receiving a message before re-attempting delivery.

**--ack-ids**:
One or more ACK_IDs to modify the deadline for. An ACK_ID is a [string
that is returned to subscribers](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.ReceivedMessage). along with the message. The ACK_ID is
different from the [message
ID](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage).

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
gcloud alpha pubsub subscriptions modify-message-ack-deadline
```

```
gcloud beta pubsub subscriptions modify-message-ack-deadline
```