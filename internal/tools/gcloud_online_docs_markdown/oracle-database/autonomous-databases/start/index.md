# gcloud oracle-database autonomous-databases start  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/start](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/start)*

**NAME**

: **gcloud oracle-database autonomous-databases start - starts an AutonomousDatabase**

**SYNOPSIS**

: **`gcloud oracle-database autonomous-databases start` (`[AUTONOMOUS_DATABASE](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/start#AUTONOMOUS_DATABASE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/start#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/start#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/start#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Starts an AutonomousDatabase which is in Stopped state.

**EXAMPLES**

: To start an AutonomousDatabase with id `my-instance` in the location
`us-east4`, run:

```
gcloud oracle-database autonomous-databases start my-instance --location=us-east4
```

**POSITIONAL ARGUMENTS**

: **AutonomousDatabase resource - The name of the Autonomous Database in the
following format:
projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `autonomous_database` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`AUTONOMOUS_DATABASE`**:
ID of the autonomousDatabase or fully qualified identifier for the
autonomousDatabase.
To set the `autonomous_database` attribute:

- provide the argument `autonomous_database` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the autonomousDatabase resource.
To set the `location` attribute:

- provide the argument `autonomous_database` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

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

: This command uses the `oracledatabase/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/oracle/database/docs](https://cloud.google.com/oracle/database/docs)