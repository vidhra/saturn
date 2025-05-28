# gcloud sql databases create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/databases/create](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create)*

**NAME**

: **gcloud sql databases create - creates a database for a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql databases create` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#DATABASE)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#--async)`] [`[--charset](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#--charset)`=`CHARSET`] [`[--collation](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#--collation)`=`COLLATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/databases/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a database for a Cloud SQL instance.

**POSITIONAL ARGUMENTS**

: **`DATABASE`**:
Cloud SQL database name.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--charset**:
Cloud SQL database charset setting, which specifies the set of symbols and
encodings used to store the data in your database. Each database version may
support a different set of charsets.

**--collation**:
Cloud SQL database collation setting, which specifies the set of rules for
comparing characters in a character set. Each database version may support a
different set of collations. For PostgreSQL database versions, this may only be
set to the collation of the template database.

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
gcloud alpha sql databases create
```

```
gcloud beta sql databases create
```