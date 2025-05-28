# gcloud sql flags list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/flags/list](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list)*

**NAME**

: **gcloud sql flags list - list customizable flags for Google Cloud SQL instances**

**SYNOPSIS**

: **`gcloud sql flags list` [`[--database-version](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list#--database-version)`=`DATABASE_VERSION`; default=`"MYSQL_8_0"`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/flags/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List customizable flags for Google Cloud SQL instances.

**FLAGS**

: **--database-version**:
The database engine type and versions. If left unspecified, MYSQL_8_0 is used.
See the list of database versions at [https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion).
Apart from listed major versions, DATABASE_VERSION also accepts supported minor
versions. `DATABASE_VERSION` must be one of:
`MYSQL_5_6`, `MYSQL_5_7`, `MYSQL_8_0`,
`MYSQL_8_4`, `POSTGRES_9_6`, `POSTGRES_10`,
`POSTGRES_11`, `POSTGRES_12`, `POSTGRES_13`,
`POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`,
`POSTGRES_17`, `SQLSERVER_2017_EXPRESS`,
`SQLSERVER_2017_WEB`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`,
`SQLSERVER_2019_WEB`, `SQLSERVER_2019_STANDARD`,
`SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2022_EXPRESS`,
`SQLSERVER_2022_WEB`, `SQLSERVER_2022_STANDARD`,
`SQLSERVER_2022_ENTERPRISE`.

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

: These variants are also available:

```
gcloud alpha sql flags list
```

```
gcloud beta sql flags list
```