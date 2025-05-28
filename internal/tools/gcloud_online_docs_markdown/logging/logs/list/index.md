# gcloud logging logs list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/logs/list](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list)*

**NAME**

: **gcloud logging logs list - list your project's logs**

**SYNOPSIS**

: **`gcloud logging logs list` [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list#--bucket)`=`BUCKET` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list#--location)`=`LOCATION` `[--view](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list#--view)`=`VIEW`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list#--limit)`=`LIMIT`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Only logs that contain log entries are listed.

**EXAMPLES**

: To list all logs in current project:

```
gcloud logging logs list
```

To list all logs for a view:

```
gcloud logging logs list --bucket=[BUCKET_ID] --location=[LOCATION] --view=[VIEW_ID]
```

**FLAGS**

: **--bucket**

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

**NOTES**

: These variants are also available:

```
gcloud alpha logging logs list
```

```
gcloud beta logging logs list
```