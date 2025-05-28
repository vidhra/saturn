# gcloud metastore services move-table-to-database  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database](https://cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database)*

**NAME**

: **gcloud metastore services move-table-to-database - move table to another database**

**SYNOPSIS**

: **`gcloud metastore services move-table-to-database` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database#--location)`=`LOCATION`) `--destination_db_name`=`DESTINATION_DB_NAME` `--source_db_name`=`SOURCE_DB_NAME` `--table_name`=`TABLE_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Move table to another database from a Dataproc Metastore service's underlying
metadata store.
If run asynchronously with `--async`, exits after printing one
operation name that can be used to poll the status of the creation via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To move table to database with the table_name, source_db_name, and
destination_db_name in location `us-central`, run:

```
gcloud metastore services move-table-to-database my-metastore-service --location=us-central1 --table_name=table_name_to_move --source_db_name=database_name_to_move --destination_db_name=destination_database_name
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the table and the
destination database you want to move to. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataproc Metastore service.
If not specified, will use `default` metastore/location.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.**

**REQUIRED FLAGS**

: **--destination_db_name**:
The name of the database where the table should be moved.

**--source_db_name**:
The name of the database where the table resides.

**--table_name**:
The name of the table to be moved.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**API REFERENCE**

: This command uses the `metastore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataproc-metastore/docs](https://cloud.google.com/dataproc-metastore/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha metastore services move-table-to-database
```

```
gcloud beta metastore services move-table-to-database
```