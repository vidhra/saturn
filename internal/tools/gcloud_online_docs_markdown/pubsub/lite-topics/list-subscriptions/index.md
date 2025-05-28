# gcloud pubsub lite-topics list-subscriptions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions)*

**NAME**

: **gcloud pubsub lite-topics list-subscriptions - list Pub/Sub Lite subscriptions for a given Lite topic**

**SYNOPSIS**

: **`gcloud pubsub lite-topics list-subscriptions` (`[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions#TOPIC)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Pub/Sub Lite subscriptions for a given Lite topic.

**EXAMPLES**

: To list Pub/Sub Lite subscriptions for a given Lite topic, run:

```
gcloud pubsub lite-topics list-subscriptions mytopic --location=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **Topic resource - Topic to list subscriptions for. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TOPIC`**:
ID of the topic or fully qualified identifier for the topic.
To set the `topic` attribute:

- provide the argument `topic` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location of the Pub/Sub Lite resource.
To set the `location` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- provide the argument `--zone` on the command line.**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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
gcloud alpha pubsub lite-topics list-subscriptions
```

```
gcloud beta pubsub lite-topics list-subscriptions
```