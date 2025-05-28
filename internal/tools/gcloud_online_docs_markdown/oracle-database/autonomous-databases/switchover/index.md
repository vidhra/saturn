# gcloud oracle-database autonomous-databases switchover  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/switchover](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/switchover)*

**NAME**

: **gcloud oracle-database autonomous-databases switchover - switchovers an AutonomousDatabase to a new primary**

**SYNOPSIS**

: **`gcloud oracle-database autonomous-databases switchover` `[AUTONOMOUS_DATABASE](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/switchover#AUTONOMOUS_DATABASE)` `[--peer-autonomous-database](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/switchover#--peer-autonomous-database)`=`PEER_AUTONOMOUS_DATABASE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/switchover#--async)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/switchover#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/switchover#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Switchovers an AutonomousDatabase from a standby database to a new primary.

**EXAMPLES**

: To switchover an AutonomousDatabase with id `my-instance` in the
location `us-east4` with primary database name as
'projects/project-id/locations/us-west3/autonomousDatabases/my-instance' run:

```
gcloud oracle-database autonomous-databases switchover my-instance --location=us-east4 --peer-autonomous-database=projects/project-id/locations/us-west3/autonomousDatabases/my-instance
```

**POSITIONAL ARGUMENTS**

: **AutonomousDatabase resource - The name of the Autonomous Database in the
following format:
projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `autonomous_database` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `autonomous_database` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

This must be specified.

**`AUTONOMOUS_DATABASE`**:
ID of the autonomousDatabase or fully qualified identifier for the
autonomousDatabase.
To set the `autonomous_database` attribute:

- provide the argument `autonomous_database` on the command line.**

**REQUIRED FLAGS**

: **AutonomousDatabase resource - The peer database name to switch over to. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--peer-autonomous-database` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--peer-autonomous-database` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.

This must be specified.

**--peer-autonomous-database**:
ID of the autonomousDatabase or fully qualified identifier for the
autonomousDatabase.
To set the `autonomous-database` attribute:

- provide the argument `--peer-autonomous-database` on the command
line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--location**:
For resources [autonomousDatabase], provides fallback value for resource
location attribute. When the resource's full URI path is not provided, location
will fallback to this flag value.

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

: This command uses the `oracledatabase/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/oracle/database/docs](https://cloud.google.com/oracle/database/docs)