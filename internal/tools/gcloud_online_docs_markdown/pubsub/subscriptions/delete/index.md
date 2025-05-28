# gcloud pubsub subscriptions delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/delete](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/delete)*

**NAME**

: **gcloud pubsub subscriptions delete - deletes one or more Cloud Pub/Sub subscriptions**

**SYNOPSIS**

: **`gcloud pubsub subscriptions delete` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/delete#SUBSCRIPTION)` [`[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/delete#SUBSCRIPTION)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes one or more Cloud Pub/Sub subscriptions.

**POSITIONAL ARGUMENTS**

: **Subscription resource - One or more subscriptions to delete. This represents a
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
gcloud alpha pubsub subscriptions delete
```

```
gcloud beta pubsub subscriptions delete
```