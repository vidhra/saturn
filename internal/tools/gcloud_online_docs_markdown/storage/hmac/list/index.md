# gcloud storage hmac list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list)*

**NAME**

: **gcloud storage hmac list - list service account HMAC keys**

**SYNOPSIS**

: **`gcloud storage hmac list` [`[--all](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--all)`, `[-a](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#-a)`] [`[--long](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--long)`, `[-l](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#-l)`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--service-account)`=`SERVICE_ACCOUNT`, `[-u](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#-u)` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#SERVICE_ACCOUNT)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage hmac list` lists the HMAC key metadata for keys in
the current project.

**EXAMPLES**

: To show metadata for all keys, including recently deleted keys:

```
gcloud storage hmac list --all --long
```

To list only HMAC keys belonging to the service account
``test.sa@test.iam.gserviceaccount.com``:

```
gcloud storage hmac list --service-account=test.sa@test.iam.gserviceaccount.com
```

**FLAGS**

: **--all**:
Shows all keys, including recently deleted keys.

**--long**:
Use long listing format, showing the full metadata for each key excluding the
secret.

**--service-account**:
Filter keys for the provided service account email.

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

: This variant is also available:

```
gcloud alpha storage hmac list
```