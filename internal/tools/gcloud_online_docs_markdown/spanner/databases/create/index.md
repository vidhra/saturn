# gcloud spanner databases create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create)*

**NAME**

: **gcloud spanner databases create - create a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner databases create` (`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#DATABASE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--instance)`=`INSTANCE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--async)`] [`[--database-dialect](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--database-dialect)`=`DATABASE_DIALECT`] [`[--ddl](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--ddl)`=`DDL`] [`[--ddl-file](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--ddl-file)`=`DDL_FILE`] [`[--proto-descriptors-file](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--proto-descriptors-file)`=`PROTO_DESCRIPTORS_FILE`] [`[--kms-keys](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--kms-keys)`=[`KMS_KEYS`,…]     | [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#--kms-project)`=`KMS_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Spanner database.

**EXAMPLES**

: To create an empty Cloud Spanner database, run:

```
gcloud spanner databases create testdb --instance=my-instance-id
```

To create a Cloud Spanner database with populated schema, run:

```
gcloud spanner databases create testdb --instance=my-instance-id --ddl='CREATE TABLE mytable (a INT64, b INT64) PRIMARY KEY(a)'
```

To create a Cloud Spanner database with the PostgreSQL dialect, run:

```
gcloud spanner databases create testdb --instance=my-instance-id --database-dialect=POSTGRESQL
```

**POSITIONAL ARGUMENTS**

: **Database resource - The Cloud Spanner database to create. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--database-dialect**:
The SQL dialect of the Cloud Spanner Database. GOOGLE_STANDARD_SQL is the
default. `DATABASE_DIALECT` must be one of:
`POSTGRESQL`, `GOOGLE_STANDARD_SQL`.

**--ddl**:
Semi-colon separated DDL (data definition language) statements to run inside the
newly created database. If there is an error in any statement, the database is
not created. This option is not supported for the PostgreSQL dialect. Full DDL
specification is at [https://cloud.google.com/spanner/docs/data-definition-language](https://cloud.google.com/spanner/docs/data-definition-language)

**--ddl-file**:
Path of a file that contains semi-colon separated DDL (data definition language)
statements to run inside the newly created database. If there is an error in any
statement, the database is not created. This option is not supported for the
PostgreSQL dialect. Full DDL specification is at [https://cloud.google.com/spanner/docs/data-definition-language](https://cloud.google.com/spanner/docs/data-definition-language).
If --ddl_file is set, --ddl is ignored. One line comments starting with -- are
ignored.

**--proto-descriptors-file**:
Path of a file that contains a protobuf-serialized
google.protobuf.FileDescriptorSet message. To generate it, install and run
`protoc` with --include_imports and --descriptor_set_out.

**KMS key name group
At most one of these can be specified:

**Key resource - Cloud KMS key(s) to be used to create the Cloud Spanner database.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `kms-project` attribute:

- provide the argument `--kms-keys` on the command line with a fully
specified name.

To set the `kms-location` attribute:

- provide the argument `--kms-keys` on the command line with a fully
specified name.

To set the `kms-keyring` attribute:

- provide the argument `--kms-keys` on the command line with a fully
specified name.

**--kms-keys**:
IDs of the keys or fully qualified identifiers for the keys.
To set the `kms-key` attribute:

- provide the argument `--kms-keys` on the command line.**

**--kms-key****

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
gcloud alpha spanner databases create
```

```
gcloud beta spanner databases create
```