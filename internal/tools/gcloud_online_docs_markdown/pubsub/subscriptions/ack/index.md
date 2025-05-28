# gcloud pubsub subscriptions ack  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/ack](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/ack)*

**NAME**

: **gcloud pubsub subscriptions ack - acknowledges one or more messages on the specified subscription**

**SYNOPSIS**

: **`gcloud pubsub subscriptions ack` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/ack#SUBSCRIPTION)` `[--ack-ids](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/ack#--ack-ids)`=[`ACK_ID`,…] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/ack#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Acknowledges one or more messages as having been successfully received. If a
delivered message is not acknowledged within the Subscription's ack deadline,
Cloud Pub/Sub will attempt to deliver it again.
To automatically acknowledge messages when pulling from a Subscription, you can
use the `--auto-ack` flag on `[gcloud pubsub
subscriptions pull](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull)`.

**POSITIONAL ARGUMENTS**

: **Subscription resource - Name of the subscription to ACK messages on. This
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

: **--ack-ids**:
One or more ACK_IDs to acknowledge. An ACK_ID is a [string
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
gcloud alpha pubsub subscriptions ack
```

```
gcloud beta pubsub subscriptions ack
```