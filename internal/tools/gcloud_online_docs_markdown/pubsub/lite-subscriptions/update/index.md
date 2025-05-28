# gcloud pubsub lite-subscriptions update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update)*

**NAME**

: **gcloud pubsub lite-subscriptions update - update a Pub/Sub Lite subscription**

**SYNOPSIS**

: **`gcloud pubsub lite-subscriptions update` (`[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update#SUBSCRIPTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update#--location)`=`LOCATION`) (`[--delivery-requirement](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update#--delivery-requirement)`=`DELIVERY_REQUIREMENT` `[--export-dead-letter-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update#--export-dead-letter-topic)`=`EXPORT_DEAD_LETTER_TOPIC` `[--export-desired-state](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update#--export-desired-state)`=`EXPORT_DESIRED_STATE` `[--export-pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update#--export-pubsub-topic)`=`EXPORT_PUBSUB_TOPIC`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Pub/Sub Lite subscription.

**EXAMPLES**

: To update a Pub/Sub Lite subscription, run:

```
gcloud pubsub lite-subscriptions update mysubscription --location=us-central1-a --delivery-requirement=DELIVER_IMMEDIATELY
```

**POSITIONAL ARGUMENTS**

: **Subscription resource - Subscription to update. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
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

: **--delivery-requirement**

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
gcloud alpha pubsub lite-subscriptions update
```

```
gcloud beta pubsub lite-subscriptions update
```