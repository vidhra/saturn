# gcloud iam service-accounts keys list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list)*

**NAME**

: **gcloud iam service-accounts keys list - list the keys for a service account**

**SYNOPSIS**

: **`gcloud iam service-accounts keys list` `[--iam-account](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#--iam-account)`=`IAM_ACCOUNT` [`[--created-before](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#--created-before)`=`CREATED_BEFORE`] [`[--managed-by](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#--managed-by)`=`MANAGED_BY`; default="any"] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: To list all user-managed keys created before noon on July 19th, 2015 (to perform
key rotation, for example), run:

```
gcloud iam service-accounts keys list --iam-account=my-iam-account@my-project.iam.gserviceaccount.com --managed-by=user --created-before=2015-07-19T12:00:00Z
```

**REQUIRED FLAGS**

: **--iam-account**:
A textual name to display for the account.

**FLAGS**

: **--created-before**:
Return only keys created before the specified time. Common time formats are
accepted. This is equivalent to --filter="validAfterTime<DATE_TIME". See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--managed-by**:
The types of keys to list. `MANAGED_BY` must be one of:
`user`, `system`, `any`.

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
gcloud alpha iam service-accounts keys list
```

```
gcloud beta iam service-accounts keys list
```