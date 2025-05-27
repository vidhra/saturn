# gcloud database-migration migration-jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create)*

**NAME**

: **gcloud database-migration migration-jobs create - create a Database Migration Service migration job**

**SYNOPSIS**

: **`gcloud database-migration migration-jobs create` (`[MIGRATION_JOB](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#MIGRATION_JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--region)`=`REGION`) `[--destination](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--destination)`=`DESTINATION` `[--source](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--source)`=`SOURCE` `[--type](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--type)`=`TYPE` [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--async)`] [`[--commit-id](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--commit-id)`=`COMMIT_ID`] [`[--conversion-workspace](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--conversion-workspace)`=`CONVERSION_WORKSPACE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--display-name)`=`DISPLAY_NAME`] [`[--dump-parallel-level](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--dump-parallel-level)`=`DUMP_PARALLEL_LEVEL`] [`[--dump-path](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--dump-path)`=`DUMP_PATH`] [`[--dump-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--dump-type)`=`DUMP_TYPE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--filter)`=`FILTER`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--all-databases](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--all-databases)`     | `[--databases-filter](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--databases-filter)`=`databaseName`,[…]] [`[--cmek-key](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--cmek-key)`=`CMEK_KEY` : `[--cmek-keyring](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--cmek-keyring)`=`CMEK_KEYRING` `[--cmek-project](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--cmek-project)`=`CMEK_PROJECT`] [`[--max-concurrent-cdc-connections](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--max-concurrent-cdc-connections)`=`MAX_CONCURRENT_CDC_CONNECTIONS` `[--max-concurrent-full-dump-connections](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--max-concurrent-full-dump-connections)`=`MAX_CONCURRENT_FULL_DUMP_CONNECTIONS` `[--skip-full-dump](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--skip-full-dump)` `[--oracle-cdc-start-position](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--oracle-cdc-start-position)`=`ORACLE_CDC_START_POSITION`     | `[--sqlserver-cdc-start-position](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--sqlserver-cdc-start-position)`=`SQLSERVER_CDC_START_POSITION` `[--max-concurrent-destination-connections](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--max-concurrent-destination-connections)`=`MAX_CONCURRENT_DESTINATION_CONNECTIONS` `[--transaction-timeout](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--transaction-timeout)`=`TRANSACTION_TIMEOUT`] [`[--peer-vpc](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--peer-vpc)`=`PEER_VPC`     | `[--static-ip](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--static-ip)`     | [`[--vm-ip](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm-ip)`=`VM_IP` `[--vm-port](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm-port)`=`VM_PORT` `[--vpc](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vpc)`=`VPC` : `[--vm](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm)`=`VM`]] [`[--sqlserver-databases](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--sqlserver-databases)`=`databaseName`,[…] : `[--sqlserver-diff-backup](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--sqlserver-diff-backup)` `[--sqlserver-encrypted-databases](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--sqlserver-encrypted-databases)`=`SQLSERVER_ENCRYPTED_DATABASES` `[--sqlserver-promote-when-ready](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--sqlserver-promote-when-ready)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration Service migration job. Recommended steps before
creating the migration job:

- Create a source connection profile. See prerequisites [here](https://cloud.google.com/database-migration/docs/mysql/configure-source-database).
- Create a destination connection profile. For migrating to Cloud SQL for MySQL or
Cloud SQL for PostgreSQL, use the cloudsql connection profile for DMS to create
the CloudSQL replica for you.
- Configure the connectivity method. See prerequisites [here](https://cloud.google.com/database-migration/docs/mysql/configure-connectivity).
- [Heterogeneous migrations only] Create a conversion workspace.

**EXAMPLES**

: To create a continuous migration job with IP allowlist connectivity:

```
gcloud database-migration migration-jobs create my-migration-job --region=us-central1 --type=CONTINUOUS --source=cp1 --destination=cp2
```

To create a continuous migration job with VPC peering connectivity:

```
gcloud database-migration migration-jobs create my-migration-job --region=us-central1 --type=CONTINUOUS --source=cp1 --destination=cp2 --peer-vpc=projects/my-project/global/networks/my-network
```

To create a one-time migration job with reverse-SSH tunnel connectivity:

```
gcloud database-migration migration-jobs create my-migration-job --region=us-central1 --type=ONE_TIME --source=cp1 --destination=cp2 --vm=vm1 --vm-ip=1.1.1.1 --vm-port=1111 --vpc=projects/my-project/global/networks/my-network
```

To create a heterogeneous continuous migration job:

```
gcloud database-migration migration-jobs create my-migration-job --region=us-central1 --type=CONTINUOUS --source=cp1 --destination=cp2 --conversion-workspace=cw
```

To create a continuous SQL Server to SQL Server homogeneous migration job with
differential backup enabled:
```
gcloud database-migration migration-jobs create my-migration-job --region=us-central1 --type=CONTINUOUS --source=cp1 --destination=cp2 --sqlserver-diff-backup --sqlserver-databases=db1,db2,db3
```

To create a continuous SQL Server to SQL Server homogeneous migration job with
encrypted databases:
```
gcloud database-migration migration-jobs create my-migration-job --region=us-central1 --type=CONTINUOUS --source=cp1 --destination=cp2 --sqlserver-databases=db1,db2,db3 --sqlserver-encrypted-databases=PATH/TO/ENCRYPTION/SETTINGS
```

**POSITIONAL ARGUMENTS**

: **Migration job resource - The migration job to create. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `migration_job` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MIGRATION_JOB`**:
ID of the migration_job or fully qualified identifier for the migration_job.
To set the `migration_job` attribute:

- provide the argument `migration_job` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the migration_job.
To set the `region` attribute:

- provide the argument `migration_job` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **Connection profile resource - ID of the destination connection profile,
representing the destination database. This represents a Cloud resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `--destination` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--destination` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.

This must be specified.

**--destination**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--destination` on the command line.**

**Connection profile resource - ID of the source connection profile, representing
the source database. This represents a Cloud resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--source` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.

This must be specified.

**--source**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--source` on the command line.**

**--type**:
Type of the migration job. `TYPE` must be one of:
`ONE_TIME`, `CONTINUOUS`.

**OPTIONAL FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--commit-id**:
Commit id for the conversion workspace to use for creating the migration job. If
not specified, the latest commit id will be used by default.

**Conversion workspace resource - Name of the conversion workspaces to be used for
the migration job This represents a Cloud resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--conversion-workspace` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--conversion-workspace` on the command line
with a fully specified name;
- provide the argument `--region` on the command line.

**--conversion-workspace**:
ID of the conversion_workspace or fully qualified identifier for the
conversion_workspace.
To set the `conversion_workspace` attribute:

- provide the argument `--conversion-workspace` on the command line.**

**--display-name**:
A user-friendly name for the migration job. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter.

**--dump-parallel-level**:
Parallelization level during initial dump of the migration job. If not
specified, will be defaulted to OPTIMAL.
`DUMP_PARALLEL_LEVEL` must be one of: `MIN`,
`OPTIMAL`, `MAX`.

**--dump-path**:
Path to the dump file in Google Cloud Storage, in the format:
`gs://[BUCKET_NAME]/[OBJECT_NAME]`.

**--dump-type**:
The type of the data dump. Currently applicable for MySQL to MySQL migrations
only. `DUMP_TYPE` must be one of: `LOGICAL`,
`PHYSICAL`.

**--filter**:
Filter the entities based on [AIP-160](https://google.aip.dev/160)
standard. Example: to filter all tables whose name start with "Employee" and are
present under schema "Company", use filter as "Company.Employee`*`
AND type=TABLE"

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--all-databases**

**Cmek key resource - Name of the CMEK (customer-managed encryption key) used for
the migration job The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `region` attribute:

- provide the argument `--cmek-key` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.

**--cmek-key**:
ID of the cmek-key or fully qualified identifier for the cmek-key.
To set the `cmek-key` attribute:

- provide the argument `--cmek-key` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--cmek-keyring**:
The CMEK keyring id of the cmek-key.
To set the `cmek-keyring` attribute:

- provide the argument `--cmek-key` on the command line with a fully
specified name;
- provide the argument `--cmek-keyring` on the command line.

**--cmek-project**:
The Cloud project id for the cmek-key.
To set the `cmek-project` attribute:

- provide the argument `--cmek-key` on the command line with a fully
specified name;
- provide the argument `--cmek-project` on the command line.**

**--max-concurrent-cdc-connections**

**--peer-vpc**

**--sqlserver-databases**

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
gcloud alpha database-migration migration-jobs create
```