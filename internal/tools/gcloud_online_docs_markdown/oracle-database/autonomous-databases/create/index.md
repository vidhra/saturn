# gcloud oracle-database autonomous-databases create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create)*

**NAME**

: **gcloud oracle-database autonomous-databases create - create a new AutonomousDatabase**

**SYNOPSIS**

: **`gcloud oracle-database autonomous-databases create` `[AUTONOMOUS_DATABASE](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#AUTONOMOUS_DATABASE)` [`[--admin-password](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--admin-password)`=`ADMIN_PASSWORD`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--async)`] [`[--cidr](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--cidr)`=`CIDR`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--database)`=`DATABASE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--labels)`=[`LABELS`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--location)`=`LOCATION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--network)`=`NETWORK`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--request-id)`=`REQUEST_ID`] [[`[--properties-db-workload](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-db-workload)`=`PROPERTIES_DB_WORKLOAD` `[--properties-license-type](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-license-type)`=`PROPERTIES_LICENSE_TYPE` : `[--properties-allowlisted-ips](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-allowlisted-ips)`=[`PROPERTIES_ALLOWLISTED_IPS`,…] `[--properties-backup-retention-period-days](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-backup-retention-period-days)`=`PROPERTIES_BACKUP_RETENTION_PERIOD_DAYS` `[--properties-character-set](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-character-set)`=`PROPERTIES_CHARACTER_SET` `[--properties-compute-count](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-compute-count)`=`PROPERTIES_COMPUTE_COUNT` `[--properties-cpu-core-count](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-cpu-core-count)`=`PROPERTIES_CPU_CORE_COUNT` `[--properties-customer-contacts](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-customer-contacts)`=[`email`=`EMAIL`] `[--properties-data-storage-size-gb](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-data-storage-size-gb)`=`PROPERTIES_DATA_STORAGE_SIZE_GB` `[--properties-data-storage-size-tb](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-data-storage-size-tb)`=`PROPERTIES_DATA_STORAGE_SIZE_TB` `[--properties-db-edition](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-db-edition)`=`PROPERTIES_DB_EDITION` `[--properties-db-version](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-db-version)`=`PROPERTIES_DB_VERSION` `[--properties-is-auto-scaling-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-is-auto-scaling-enabled)` `[--properties-is-storage-auto-scaling-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-is-storage-auto-scaling-enabled)` `[--properties-maintenance-schedule-type](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-maintenance-schedule-type)`=`PROPERTIES_MAINTENANCE_SCHEDULE_TYPE` `[--properties-mtls-connection-required](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-mtls-connection-required)` `[--properties-n-character-set](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-n-character-set)`=`PROPERTIES_N_CHARACTER_SET` `[--properties-private-endpoint-ip](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-private-endpoint-ip)`=`PROPERTIES_PRIVATE_ENDPOINT_IP` `[--properties-private-endpoint-label](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-private-endpoint-label)`=`PROPERTIES_PRIVATE_ENDPOINT_LABEL` `[--properties-secret-id](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-secret-id)`=`PROPERTIES_SECRET_ID` `[--properties-vault-id](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--properties-vault-id)`=`PROPERTIES_VAULT_ID`]] [`[--source-config-automatic-backups-replication-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--source-config-automatic-backups-replication-enabled)` `[--source-config-autonomous-database](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#--source-config-autonomous-database)`=`SOURCE_CONFIG_AUTONOMOUS_DATABASE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new AutonomousDatabase.

**EXAMPLES**

: To create AutonomousDatabase with id `my-instance` in the location
`us-east4` with display-name `my instance`, network
`projects/my-project/locations/global/networks/default`, location
`us-east4`, database `testadb`, admin-password
`123Abpassdord`, cidr `12.2.0.0/24`,
properties-compute-count `2`, properties-db-version `19c`,
properties-license-type `LICENSE_INCLUDED`, properties-db-workload
`DW`. run:

```
gcloud oracle-database autonomous-databases create my-instance --location=us-east4 --display-name="my instance" --network=projects/my-project/locations/global/networks/default --cidr=12.2.0.0/24 --location=us-east4 --database=testadb --admin-password=123Abpassdord --properties-compute-count=2 --properties-db-version=19c --properties-license-type=LICENSE_INCLUDED --properties-db-workload=DW
```

**POSITIONAL ARGUMENTS**

: **AutonomousDatabase resource - Identifier. The name of the Autonomous Database
resource in the following format:
projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database}
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

**FLAGS**

: **--admin-password**:
The password for the default ADMIN user.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cidr**:
The subnet CIDR range for the Autonmous Database.

**--database**:
The name of the Autonomous Database. The database name must be unique in the
project. The name must begin with a letter and can contain a maximum of 30
alphanumeric characters.

**--display-name**:
The display name for the Autonomous Database. The name does not have to be
unique within your project.

**--labels**:
The labels or tags associated with the Autonomous Database.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--location**:
For resources [autonomousDatabase], provides fallback value for resource
location attribute. When the resource's full URI path is not provided, location
will fallback to this flag value.

**Network resource - The name of the VPC network used by the Autonomous Database
in the following format: projects/{project}/global/networks/{network} This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network` attribute:

- provide the argument `--network` on the command line.**

**--request-id**:
An optional ID to identify the request. This value is used to identify duplicate
requests. If you make a request with the same request ID and the original
request is still in progress or completed, the server ignores the second
request. This prevents clients from accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--properties-db-workload**

**--source-config-automatic-backups-replication-enabled**

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