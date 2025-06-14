# gcloud endpoints operations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list)*

**NAME**

: **gcloud endpoints operations list - list operations for a project**

**SYNOPSIS**

: **`gcloud endpoints operations list` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list#--filter)`=`EXPRESSION`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list#--service)`=`SERVICE`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/operations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will list operations for a service, optionally matching a
particular filter.

**EXAMPLES**

: To list all operations for a service named
`api.endpoints.proj.cloud.goog`, run:

```
gcloud endpoints operations list --service=api.endpoints.proj.cloud.goog
```

To list only operations which are complete, add the `--filter`
argument with a status filter:

```
gcloud endpoints operations list --service=api.endpoints.proj.cloud.goog --filter='done = true'
```

To list only operations begun after a certain point in time, add the
`--filter` argument with an ISO 8601 datetime startTime filter:

```
gcloud endpoints operations list --service=api.endpoints.proj.cloud.goog --filter='startTime >= "2017-02-01"'
```

**FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates as True then that item is listed.
The available filter fields are startTime and done. Unrecognized fields will
cause an error.
startTime is an ISO 8601 datetime and supports >=, >, <=, and <
operators. The datetime value must be wrapped in quotation marks. For example:

```
--filter='startTime < "2017-03-20T16:02:32"'
```

done is a boolean value and supports = and != operators.

**--service**:
The name of the service for which to list operations.

**LIST COMMAND FLAGS**

: **--limit**:
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

: These variants are also available:

```
gcloud alpha endpoints operations list
```

```
gcloud beta endpoints operations list
```