# gcloud sql databases patch  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch)*

**NAME**

: **gcloud sql databases patch - patches the settings of a Cloud SQL database**

**SYNOPSIS**

: **`gcloud sql databases patch` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#DATABASE)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#INSTANCE)` [`[--charset](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#--charset)`=`CHARSET`] [`[--collation](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#--collation)`=`COLLATION`] [`[--diff](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#--diff)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/databases/patch#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Patches the settings of a Cloud SQL database.

**POSITIONAL ARGUMENTS**

: **`DATABASE`**:
Cloud SQL database name.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

**OPTIONAL FLAGS**

: **--charset**:
Cloud SQL database charset setting, which specifies the set of symbols and
encodings used to store the data in your database. Each database version may
support a different set of charsets.

**--collation**:
Cloud SQL database collation setting, which specifies the set of rules for
comparing characters in a character set. Each database version may support a
different set of collations. This flag can't be used with PostgreSQL instances.

**--diff**:
Show what changed as a result of the patch.

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
gcloud alpha sql databases patch
```

```
gcloud beta sql databases patch
```