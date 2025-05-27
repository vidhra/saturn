# gcloud datastream connection-profiles discover  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover)*

**NAME**

: **gcloud datastream connection-profiles discover - discover a Datastream connection profile**

**SYNOPSIS**

: **`gcloud datastream connection-profiles discover` `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--location)`=`LOCATION` (`[--connection-profile-name](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--connection-profile-name)`=`CONNECTION_PROFILE_NAME`     | `[--connection-profile-object-file](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--connection-profile-object-file)`=`CONNECTION_PROFILE_OBJECT_FILE`) [`[--full-hierarchy](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--full-hierarchy)`     | `[--hierarchy-depth](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--hierarchy-depth)`=`HIERARCHY_DEPTH`] [`[--mysql-rdbms-file](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--mysql-rdbms-file)`=`MYSQL_RDBMS_FILE`     | `[--oracle-rdbms-file](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--oracle-rdbms-file)`=`ORACLE_RDBMS_FILE`     | `[--postgresql-rdbms-file](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--postgresql-rdbms-file)`=`POSTGRESQL_RDBMS_FILE`     | `[--sqlserver-rdbms-file](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--sqlserver-rdbms-file)`=`SQLSERVER_RDBMS_FILE`] [`[--recursive](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--recursive)`     | `[--recursive-depth](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#--recursive-depth)`=`RECURSIVE_DEPTH`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Discover data objects accessible from a Datastream connection profile

**EXAMPLES**

: To discover an existing connection profile:

```
gcloud datastream connection-profiles discover CONNECTION_PROFILE --location=us-central1 --connection-profile-name=some-cp --recursive=true
```

To discover a non-existing connection profile:

```
gcloud datastream connection-profiles discover CONNECTION_PROFILE --location=us-central1 --connection-profile-object-file=path/to/yaml/or/json/file
```

**REQUIRED FLAGS**

: **Location resource - The location you want to list the connection profiles for.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

**Exactly one of these must be specified:

**Connection profile resource - Resource ID of the connection profile. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--connection-profile-name` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--connection-profile-name` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.

**--connection-profile-name**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--connection-profile-name` on the command line.**

**--connection-profile-object-file**:
Path to a YAML (or JSON) file containing the configuration for a connection
profile object. If you pass - as the value of the flag the file content will be
read from stdin.**

**OPTIONAL FLAGS**

: **--full-hierarchy**

**--mysql-rdbms-file**

**--recursive**

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
gcloud beta datastream connection-profiles discover
```