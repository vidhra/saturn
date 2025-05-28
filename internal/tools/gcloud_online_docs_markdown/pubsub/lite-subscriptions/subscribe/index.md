# gcloud pubsub lite-subscriptions subscribe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe)*

**NAME**

: **gcloud pubsub lite-subscriptions subscribe - stream messages from a Pub/Sub Lite subscription**

**SYNOPSIS**

: **`gcloud pubsub lite-subscriptions subscribe` (`[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe#SUBSCRIPTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe#--location)`=`LOCATION`) [`[--auto-ack](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe#--auto-ack)`] [`[--num-messages](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe#--num-messages)`=`NUM_MESSAGES`; default=1] [`[--partitions](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe#--partitions)`=[`INT`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Streams messages from a Pub/Sub Lite subscription. This command requires Python
3.6 or greater, and requires the grpcio Python package to be installed.
For MacOS, Linux, and Cloud Shell users, to install the gRPC client libraries,
run:

```
sudo pip3 install grpcio
export CLOUDSDK_PYTHON_SITEPACKAGES=1
```

**EXAMPLES**

: To subscribe to a Pub/Sub Lite subscription and automatically acknowledge
messages, run:

```
gcloud pubsub lite-subscriptions subscribe mysubscription --location=us-central1-a --auto-ack
```

To subscribe to specific partitions in a subscription, run:

```
gcloud pubsub lite-subscriptions subscribe mysubscription --location=us-central1-a --partitions=0,1,2
```

**POSITIONAL ARGUMENTS**

: **Subscription resource - The Pub/Sub Lite subscription to receive messages from.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

**FLAGS**

: **--auto-ack**:
Automatically ACK every message received on this subscription.

**--num-messages**:
The number of messages to stream before exiting. This value must be less than or
equal to 1000.

**--partitions**:
The partitions this subscriber should connect to to receive messages. If empty,
partitions will be automatically assigned.

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
gcloud alpha pubsub lite-subscriptions subscribe
```

```
gcloud beta pubsub lite-subscriptions subscribe
```