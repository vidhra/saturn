# gcloud spanner databases get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy)*

**NAME**

: **gcloud spanner databases get-iam-policy - get the IAM policy for a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner databases get-iam-policy` (`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy#DATABASE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy#--instance)`=`INSTANCE`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the IAM policy for a Cloud Spanner database.

**EXAMPLES**

: To print the IAM policy for a given Cloud Spanner database, run:

```
gcloud spanner databases get-iam-policy my-database-id
```

**POSITIONAL ARGUMENTS**

: **Database resource - The Cloud Spanner database to get IAM policy binding for.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `database` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATABASE`**:
ID of the database or fully qualified identifier for the database.
To set the `database` attribute:

- provide the argument `database` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
The Cloud Spanner instance for the database.
To set the `instance` attribute:

- provide the argument `database` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

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
gcloud alpha spanner databases get-iam-policy
```

```
gcloud beta spanner databases get-iam-policy
```