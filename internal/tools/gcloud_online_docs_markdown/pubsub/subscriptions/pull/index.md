# gcloud pubsub subscriptions pull  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull)*

**NAME**

: **gcloud pubsub subscriptions pull - pulls one or more Cloud Pub/Sub messages from a subscription**

**SYNOPSIS**

: **`gcloud pubsub subscriptions pull` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#SUBSCRIPTION)` [`[--auto-ack](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#--auto-ack)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#--limit)`=`LIMIT`; default=1] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns one or more messages from the specified Cloud Pub/Sub subscription, if
there are any messages enqueued.
By default, this command returns only one message from the subscription. Use the
`--limit` flag to specify the max messages to return.
Please note that this command is not guaranteed to return all the messages in
your backlog or the maximum specified in the --limit argument. Receiving fewer
messages than available occasionally is normal.

**POSITIONAL ARGUMENTS**

: **Subscription resource - Name of the subscription to pull messages from. This
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

**FLAGS**

: **--auto-ack**:
Automatically ACK every message pulled from this subscription. Use --no-auto-ack
to disable this flag.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `1`. This flag
interacts with other flags that are applied in this order:
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

**--uri**:
Print a list of resource URIs instead of the default output, and change the
command output to a list of URIs. If this flag is used with
`--format`, the formatting is applied on this URI list. To display
URIs alongside other keys instead, use the `uri()` transform.

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
gcloud alpha pubsub subscriptions pull
```

```
gcloud beta pubsub subscriptions pull
```