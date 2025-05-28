# gcloud pubsub lite-operations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list)*

**NAME**

: **gcloud pubsub lite-operations list - list Pub/Sub Lite operations**

**SYNOPSIS**

: **`gcloud pubsub lite-operations list` `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#--location)`=`LOCATION` [`[--done](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#--done)`=`DONE`] [`[--subscription](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#--subscription)`=`SUBSCRIPTION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Pub/Sub Lite operations.
The optional `--subscription` flag can be used to filter operations
for a Pub/Sub Lite subscription. The optional `--done` flag can be
used to filter by operation completion status. These flags are ignored if
`--filter` is set.
To describe a listed operation, run:

```
gcloud pubsub lite-operations list operation-id --location=us-central1-a
```

**EXAMPLES**

: To list Pub/Sub Lite operations, run:

```
gcloud pubsub lite-operations list --location=us-central1-a --limit=50
```

To list incomplete Pub/Sub Lite operations, run:

```
gcloud pubsub lite-operations list --location=us-central1-a --done=false
```

To list Pub/Sub Lite operations for a subscription, run:

```
gcloud pubsub lite-operations list --location=us-central1-a --subscription=my-subscription --limit=50
```

To list incomplete Pub/Sub Lite operations for a subscription, run:

```
gcloud pubsub lite-operations list --location=us-central1-a --subscription=my-subscription --done=false
```

**REQUIRED FLAGS**

: **Location resource - Location to list operations for. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

**FLAGS**

: **--done**:
Filter operations by completion status. This flag is ignored if
`--filter` is set. `DONE` must be one of:
`false`, `true`.

**--subscription**:
Filter operations by target subscription. This flag is ignored if
`--filter` is set.

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
gcloud alpha pubsub lite-operations list
```

```
gcloud beta pubsub lite-operations list
```