# gcloud datastream streams update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update)*

**NAME**

: **gcloud datastream streams update - updates a Datastream stream**

**SYNOPSIS**

: **`gcloud datastream streams update` (`[STREAM](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#STREAM)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--location)`=`LOCATION`) [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--display-name)`=`DISPLAY_NAME`] [`[--state](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--state)`=`STATE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--update-mask)`=`UPDATE_MASK`] [`[--backfill-none](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--backfill-none)`     | `[--backfill-all](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--backfill-all)` `[--mongodb-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--mongodb-excluded-objects)`=`MONGODB_EXCLUDED_OBJECTS`     | `[--mysql-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--mysql-excluded-objects)`=`MYSQL_EXCLUDED_OBJECTS`     | `[--oracle-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--oracle-excluded-objects)`=`ORACLE_EXCLUDED_OBJECTS`     | `[--postgresql-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--postgresql-excluded-objects)`=`POSTGRESQL_EXCLUDED_OBJECTS`     | `[--salesforce-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--salesforce-excluded-objects)`=`SALESFORCE_EXCLUDED_OBJECTS`     | `[--sqlserver-excluded-objects](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--sqlserver-excluded-objects)`=`SQLSERVER_EXCLUDED_OBJECTS`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--remove-labels)`=[`KEY`,…]] [`[--destination](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--destination)`=`DESTINATION` `[--bigquery-destination-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--bigquery-destination-config)`=`BIGQUERY_DESTINATION_CONFIG`     | `[--gcs-destination-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--gcs-destination-config)`=`GCS_DESTINATION_CONFIG`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--force)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--validate-only)`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--source)`=`SOURCE` `[--mongodb-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--mongodb-source-config)`=`MONGODB_SOURCE_CONFIG`     | `[--mysql-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--mysql-source-config)`=`MYSQL_SOURCE_CONFIG`     | `[--oracle-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--oracle-source-config)`=`ORACLE_SOURCE_CONFIG`     | `[--postgresql-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--postgresql-source-config)`=`POSTGRESQL_SOURCE_CONFIG`     | `[--salesforce-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--salesforce-source-config)`=`SALESFORCE_SOURCE_CONFIG`     | `[--sqlserver-source-config](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#--sqlserver-source-config)`=`SQLSERVER_SOURCE_CONFIG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Datastream stream. If successful, the response body contains a newly
created instance of Operation. To get the operation result, call: describe
OPERATION

**EXAMPLES**

: To update a stream with a new source and new display name:

```
gcloud datastream streams update STREAM --location=us-central1 --display-name=my-stream --source=source --update-mask=display_name,source
```

To update a stream's state to RUNNING:

```
gcloud datastream streams update STREAM --location=us-central1 --state=RUNNING --update-mask=state
```

To update a stream's oracle source config:

```
gcloud datastream streams update STREAM --location=us-central1 --oracle-source-config=good_oracle_cp.json --update-mask=oracle_source_config.include_objects
```

**POSITIONAL ARGUMENTS**

: **Stream resource - The stream to update. The arguments in this group can be used
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

**FLAGS**

: **--display-name**:
Friendly name for the stream.

**--state**:
Stream state, can be set to: "RUNNING" or "PAUSED".

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--update-mask**:
Used to specify the fields to be overwritten in the stream resource by the
update. If the update mask is used, then a field will be overwritten only if it
is in the mask. If the user does not provide a mask then all fields will be
overwritten. This is a comma-separated list of fully qualified names of fields,
written as snake_case or camelCase. Example: "display_name,
source_config.oracle_source_config".

**--backfill-none**

**--clear-labels**

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

**--destination**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--destination` on the command line.**

**--bigquery-destination-config**

**--force**

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

**--source**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--source` on the command line.**

**--mongodb-source-config**

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
gcloud beta datastream streams update
```