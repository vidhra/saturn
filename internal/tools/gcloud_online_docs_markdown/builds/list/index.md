# gcloud builds list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/list](https://cloud.google.com/sdk/gcloud/reference/builds/list)*

**NAME**

: **gcloud builds list - list builds**

**SYNOPSIS**

: **`gcloud builds list` [`[--ongoing](https://cloud.google.com/sdk/gcloud/reference/builds/list#--ongoing)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/builds/list#--region)`=`REGION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/builds/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/builds/list#--limit)`=`LIMIT`; default=50] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/builds/list#--page-size)`=`PAGE_SIZE`; default=20] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/builds/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/builds/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List builds.

**EXAMPLES**

: To list all completed builds in the current project:

```
gcloud builds list
```

To list all builds in the current project in QUEUED or WORKING status.:

```
gcloud builds list --ongoing
```

**FLAGS**

: **--ongoing**:
Only list builds that are currently QUEUED or WORKING.

**--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`. Note:
Region must be specified in 2nd gen repo; `global` is not supported.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter EXPRESSION to each resource item to be listed. If the
expression evaluates True, then that item is listed. For more details and
examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order: --flatten, --sort-by,
--filter, --limit.

**--limit**:
Maximum number of resources to list. The default is `50`. This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is `20`. Paging may
be applied before or after `--filter` and `--limit`
depending on the service.

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
gcloud alpha builds list
```

```
gcloud beta builds list
```