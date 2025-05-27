# gcloud datastream streams create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create)*

**NAME**

: **gcloud datastream streams create - create a Datastream stream**

**SYNOPSIS**

: **`gcloud datastream streams create` (`[STREAM](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#STREAM)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--location)`=`LOCATION`) `[--display-name](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--display-name)`=`DISPLAY_NAME` (`[--backfill-none](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--backfill-none)`     | `[--backfill-all](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--backfill-all)` `[--mongodb-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--mongodb-excluded-objects)`=`MONGODB_EXCLUDED_OBJECTS`     | `[--mysql-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--mysql-excluded-objects)`=`MYSQL_EXCLUDED_OBJECTS`     | `[--oracle-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--oracle-excluded-objects)`=`ORACLE_EXCLUDED_OBJECTS`     | `[--postgresql-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--postgresql-excluded-objects)`=`POSTGRESQL_EXCLUDED_OBJECTS`     | `[--salesforce-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--salesforce-excluded-objects)`=`SALESFORCE_EXCLUDED_OBJECTS`     | `[--sqlserver-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--sqlserver-excluded-objects)`=`SQLSERVER_EXCLUDED_OBJECTS`) (`[--destination](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--destination)`=`DESTINATION` (`[--bigquery-destination-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--bigquery-destination-config)`=`BIGQUERY_DESTINATION_CONFIG` | `[--gcs-destination-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--gcs-destination-config)`=`GCS_DESTINATION_CONFIG`)) (`[--source](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--source)`=`SOURCE` (`[--mongodb-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--mongodb-source-config)`=`MONGODB_SOURCE_CONFIG` | `[--mysql-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--mysql-source-config)`=`MYSQL_SOURCE_CONFIG` | `[--oracle-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--oracle-source-config)`=`ORACLE_SOURCE_CONFIG` | `[--postgresql-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--postgresql-source-config)`=`POSTGRESQL_SOURCE_CONFIG` | `[--salesforce-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--salesforce-source-config)`=`SALESFORCE_SOURCE_CONFIG` | `[--sqlserver-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--sqlserver-source-config)`=`SQLSERVER_SOURCE_CONFIG`)) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--force](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--force)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Datastream stream. If successful, the response body contains a newly
created instance of Operation. To get the operation result, call: describe
OPERATION

**EXAMPLES**

: To create a stream with an Oracle source and a Google Cloud Storage destination:

```
gcloud datastream streams create STREAM --location=us-central1 --display-name=my-stream --source=source --oracle-source-config=source_config.json --destination=destination --gcs-destination-config=destination_config.json --backfill-none
```

To create a stream with a MySQL source and a Cloud Storage destination and that
excludes some objects from being backfilled:

```
gcloud datastream streams create STREAM --location=us-central1 --display-name=my-stream --source=source --mysql-source-config=source_config.json --destination=destination --gcs-destination-config=destination_config.json --backfill-all --mysql-excluded-objects=excluded_objects.json
```

To create a stream with an Oracle source and a BigQuery destination:

```
gcloud datastream streams create STREAM --location=us-central1 --display-name=my-stream --source=source --oracle-source-config=source_config.json --destination=destination --bigquery-destination-config=destination_config.json --backfill-none
```

To create a stream with a PostgreSQL source and a BigQuery destination:

```
gcloud datastream streams create STREAM --location=us-central1 --display-name=my-stream --source=source --postgresql-source-config=source_config.json --destination=destination --bigquery-destination-config=destination_config.json --backfill-none
```

To create a stream with a MongoDB source and a Cloud Storage destination and
that excludes some objects from being backfilled:

```
gcloud datastream streams create STREAM --location=us-central1 --display-name=my-stream --source=source --mongodb-source-config=source_config.json --destination=destination --gcs-destination-config=destination_config.json --backfill-all --mongodb-excluded-objects=excluded_objects.json
```

**POSITIONAL ARGUMENTS**

: **Stream resource - The stream to create. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `stream` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`STREAM`**:
ID of the stream or fully qualified identifier for the stream.
To set the `stream` attribute:

- provide the argument `stream` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the stream.
To set the `location` attribute:

- provide the argument `stream` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--display-name**:
Friendly name for the stream.

**--backfill-none**

**This must be specified.

**Connection profile resource - Resource ID of the destination connection profile.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--destination` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--destination` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

This must be specified.

**--destination**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--destination` on the command line.**

**--bigquery-destination-config****

**This must be specified.

**Connection profile resource - Resource ID of the source connection profile. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--source` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

This must be specified.

**--source**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--source` on the command line.**

**--mongodb-source-config****

**OPTIONAL FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--force**

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

: This variant is also available:

```
gcloud beta datastream streams create
```