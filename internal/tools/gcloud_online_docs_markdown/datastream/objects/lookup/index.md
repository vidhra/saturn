# gcloud datastream objects lookup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup)*

**NAME**

: **gcloud datastream objects lookup - lookup a Datastream stream object**

**SYNOPSIS**

: **`gcloud datastream objects lookup` (`[--salesforce-object-name](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--salesforce-object-name)`=`SALESFORCE_OBJECT_NAME`     | `[--mysql-database](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--mysql-database)`=`MYSQL_DATABASE` `[--mysql-table](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--mysql-table)`=`MYSQL_TABLE`     | `[--oracle-schema](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--oracle-schema)`=`ORACLE_SCHEMA` `[--oracle-table](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--oracle-table)`=`ORACLE_TABLE`     | `[--postgresql-schema](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--postgresql-schema)`=`POSTGRESQL_SCHEMA` `[--postgresql-table](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--postgresql-table)`=`POSTGRESQL_TABLE`     | `[--sqlserver-schema](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--sqlserver-schema)`=`SQLSERVER_SCHEMA` `[--sqlserver-table](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--sqlserver-table)`=`SQLSERVER_TABLE`) (`[--stream](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--stream)`=`STREAM` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/objects/lookup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Lookup a stream object by its source object identifier (e.g. schema.table)

**EXAMPLES**

: To lookup an existing Mysql stream object:

```
gcloud datastream objects lookup --stream=my-stream --location=us-central1 --mysql-database=my-db --mysql-table=my-table
```

To lookup an existing Oracle stream object:

```
gcloud datastream objects lookup --stream=my-stream --location=us-central1 --oracle-schema=my-schema --oracle-table=my-table
```

To lookup an existing PostgreSQL stream object:

```
gcloud datastream objects lookup --stream=my-stream --location=us-central1 --postgresql-schema=my-schema --postgresql-table=my-table
```

To lookup an existing SQL Server stream object:

```
gcloud datastream objects lookup --stream=my-stream --location=us-central1 --sqlserver-schema=my-schema --sqlserver-table=my-table
```

To lookup an existing Salesforce stream object:

```
gcloud datastream objects lookup --stream=my-stream --location=us-central1 --salesforce-object-name=my-object
```

**REQUIRED FLAGS**

: **--salesforce-object-name**

**Stream resource - The stream to list objects for. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--stream` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--stream**:
ID of the stream or fully qualified identifier for the stream.
To set the `stream` attribute:

- provide the argument `--stream` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
The Cloud location for the stream.
To set the `location` attribute:

- provide the argument `--stream` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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