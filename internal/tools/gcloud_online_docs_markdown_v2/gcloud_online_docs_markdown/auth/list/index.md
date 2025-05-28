# gcloud auth list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/auth/list](https://cloud.google.com/sdk/gcloud/reference/auth/list)*

**NAME**

: **gcloud auth list - lists credentialed accounts**

**SYNOPSIS**

: **`gcloud auth list` [`[--filter-account](https://cloud.google.com/sdk/gcloud/reference/auth/list#--filter-account)`=`FILTER_ACCOUNT`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/auth/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/auth/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/auth/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/auth/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/auth/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Lists accounts whose credentials have been obtained using `[gcloud init](https://cloud.google.com/sdk/gcloud/reference/init)`, `[gcloud auth login](https://cloud.google.com/sdk/gcloud/reference/auth/login)` and
`[gcloud auth
activate-service-account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)`, and shows which account is active. The
active account is used by gcloud and other Google Cloud CLI tools to access
Google Cloud Platform. While there is no limit on the number of accounts with
stored credentials, there is only one active account.

**EXAMPLES**

: To set an existing account to be the current active account, run:

```
gcloud config set core/account your-email-account@gmail.com
```

If you don't have an existing account, create one using:

```
gcloud init
```

To list the active account name:

```
gcloud auth list --filter=status:ACTIVE --format="value(account)"
```

To list the inactive account names with prefix `test`:

```
gcloud auth list --filter="-status:ACTIVE account:test*" --format="value(account)"
```

**FLAGS**

: **--filter-account**:
List only credentials for one account. Use
--filter="account~`PATTERN`" to select accounts that match
`PATTERN`.

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
gcloud alpha auth list
```

```
gcloud beta auth list
```