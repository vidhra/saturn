# gcloud iam workforce-pools list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list)*

**NAME**

: **gcloud iam workforce-pools list - list the workforce pools for an organization**

**SYNOPSIS**

: **`gcloud iam workforce-pools list` `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#--organization)`=`ORGANIZATION` [`[--show-deleted](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#--show-deleted)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Lists all of the workforce pools for an organization given a valid organization
ID.
This command can fail for the following reasons:

- The organization specified does not exist.
- The active account does not have permission to access the organization.

**EXAMPLES**

: The following command lists the workforce pools for an organization with the ID
``12345``, including soft-deleted pools:

```
gcloud iam workforce-pools list --organization=12345 --location=global --show-deleted
```

**REQUIRED FLAGS**

: **--location**:
The location of the workforce pools to list.

**--organization**:
The parent organization of the workforce pools to list.

**FLAGS**

: **--show-deleted**:
Show soft-deleted workforce pools by specifying this flag.

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

**NOTES**

: These variants are also available:

```
gcloud alpha iam workforce-pools list
```

```
gcloud beta iam workforce-pools list
```