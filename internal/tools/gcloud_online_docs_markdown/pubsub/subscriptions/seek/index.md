# gcloud pubsub subscriptions seek  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek)*

**NAME**

: **gcloud pubsub subscriptions seek - resets a subscription's backlog to a point in time or to a given snapshot**

**SYNOPSIS**

: **`gcloud pubsub subscriptions seek` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek#SUBSCRIPTION)` (`[--snapshot](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek#--snapshot)`=`SNAPSHOT`     | `[--time](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek#--time)`=`TIME`) [`[--snapshot-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek#--snapshot-project)`=`SNAPSHOT_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resets a subscription's backlog to a point in time or to a given snapshot.

**POSITIONAL ARGUMENTS**

: **Subscription resource - Name of the subscription to affect. This represents a
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

**REQUIRED FLAGS**

: **--snapshot**

**OPTIONAL FLAGS**

: **--snapshot-project**:
The name of the project the snapshot belongs to (if seeking to a snapshot). If
not set, it defaults to the currently selected cloud project.

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
gcloud alpha pubsub subscriptions seek
```

```
gcloud beta pubsub subscriptions seek
```