# gcloud pubsub lite-subscriptions seek  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek)*

**NAME**

: **gcloud pubsub lite-subscriptions seek - seek a Pub/Sub Lite subscription**

**SYNOPSIS**

: **`gcloud pubsub lite-subscriptions seek` (`[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek#SUBSCRIPTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek#--location)`=`LOCATION`) (`[--event-time](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek#--event-time)`=`EVENT_TIME`     | `[--publish-time](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek#--publish-time)`=`PUBLISH_TIME`     | `[--starting-offset](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek#--starting-offset)`=`STARTING_OFFSET`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Initiate an out-of-band seek operation for a Pub/Sub Lite subscription to a
specified target, which may be timestamps or named locations within the message
backlog.
The seek operation will complete once subscriber clients react to the seek for
all partitions of the topic. Note that the seek operation will not complete
until subscribers are online. It may take some time (usually within 30 seconds)
for the seek to propagate if subscribers are online. Use the --async flag if
it's not necessary to wait for completion.

**EXAMPLES**

: To seek a Pub/Sub Lite subscription to the beginning of the message backlog,
run:

```
gcloud pubsub lite-subscriptions seek mysubscription --location=us-central1-a --starting-offset=beginning
```

To seek a Pub/Sub Lite subscription to a publish time without waiting for the
operation to complete, run:

```
gcloud pubsub lite-subscriptions seek mysubscription --location=us-central1-a --publish-time="2021-01-01T12:00:00Z" --async
```

**POSITIONAL ARGUMENTS**

: **Subscription resource - Subscription to seek. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--event-time**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha pubsub lite-subscriptions seek
```

```
gcloud beta pubsub lite-subscriptions seek
```