# gcloud pubsub snapshots create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create](https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create)*

**NAME**

: **gcloud pubsub snapshots create - creates one or more Cloud Pub/Sub snapshots**

**SYNOPSIS**

: **`gcloud pubsub snapshots create` `[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create#SNAPSHOT)` [`[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create#SNAPSHOT)` …] `[--subscription](https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create#--subscription)`=`SUBSCRIPTION` [`[--labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--subscription-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create#--subscription-project)`=`SUBSCRIPTION_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates one or more Cloud Pub/Sub snapshots.

**POSITIONAL ARGUMENTS**

: **`SNAPSHOT` [`SNAPSHOT` …]**:
One or more snapshot names to create.

**REQUIRED FLAGS**

: **--subscription**:
The subscription whose backlog the snapshot retains. Specifically, the created
snapshot is guaranteed to retain a) The existing backlog on the subscription,
i.e., the set of messages in the subscription that are unacknowledged upon the
successful completion of the create snapshot request, b) Any messages published
to the subscription's topic following the successful creation of the snapshot.

**OPTIONAL FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--subscription-project**:
The name of the project the provided subscription belongs to. If not set, it
defaults to the currently selected cloud project.

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
gcloud alpha pubsub snapshots create
```

```
gcloud beta pubsub snapshots create
```