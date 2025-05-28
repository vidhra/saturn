# gcloud storage objects list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/objects/list](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list)*

**NAME**

: **gcloud storage objects list - lists Cloud Storage objects**

**SYNOPSIS**

: **`gcloud storage objects list` `[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#URLS)` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#URLS)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--additional-headers)`=`HEADER`=`VALUE`] [`[--exhaustive](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--exhaustive)`] [`[--fetch-encrypted-object-hashes](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--fetch-encrypted-object-hashes)`] [`[--next-page-token](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--next-page-token)`=`NEXT_PAGE_TOKEN`] [`[--raw](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--raw)`] [`[--soft-deleted](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--soft-deleted)`] [`[--stat](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--stat)`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--decryption-keys)`=[`DECRYPTION_KEY`,…]] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/objects/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Cloud Storage objects.
Bucket URLs like `gs://bucket` match all the objects inside a bucket,
but `gs://b*` fails because it matches a list of buckets.

**EXAMPLES**

: List all objects in bucket ``my-bucket`` within
current directory level:

```
gcloud storage objects list gs://my-bucket
```

List all objects across nested directories using wildcards
(https://cloud.google.com/storage/docs/wildcards):

```
gcloud storage objects list gs://my-bucket/**
```

List all objects in bucket beginning with ``o´´:

```
gcloud storage objects list gs://my-bucket/o*
```

List all objects in bucket with JSON formatting, only returning the value of the
``name`` metadata field:

```
gcloud storage objects list gs://my-bucket --format="json(name)"
```

**POSITIONAL ARGUMENTS**

: **`URLS` [`URLS` …]**:
Specifies URL of objects to list.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--exhaustive**:
For features like soft delete, the API may return an empty list. If present,
continue querying. This may incur costs from repeated LIST calls and may not
return any additional objects.

**--fetch-encrypted-object-hashes**:
API requests to the LIST endpoint do not fetch the hashes for encrypted objects
by default. If this flag is set, a GET request is sent for each encrypted object
in order to fetch hashes. This can significantly increase the cost of the
command.

**--next-page-token**:
Page token for resuming LIST calls.

**--raw**:
Shows metadata in the format returned by the API instead of standardizing it.

**--soft-deleted**:
Displays soft-deleted resources only. For objects, it will exclude live and
noncurrent ones.

**--stat**:
Emulates gsutil stat-style behavior. Does not show past object versions and
changes output format.

**ENCRYPTION FLAGS**

: **--decryption-keys**:
A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4
base64-encoded AES256 strings) that will be used to decrypt Cloud Storage
objects. Data encrypted with a customer-managed encryption key (CMEK) is
decrypted automatically, so CMEKs do not need to be listed here.

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
gcloud alpha storage objects list
```