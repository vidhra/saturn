# gcloud database-migration migration-jobs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update)*

**NAME**

: **gcloud database-migration migration-jobs update - update a Database Migration Service migration job**

**SYNOPSIS**

: **`gcloud database-migration migration-jobs update` (`[MIGRATION_JOB](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#MIGRATION_JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--region)`=`REGION`) [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--async)`] [`[--commit-id](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--commit-id)`=`COMMIT_ID`] [`[--destination](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--destination)`=`DESTINATION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--display-name)`=`DISPLAY_NAME`] [`[--dump-parallel-level](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--dump-parallel-level)`=`DUMP_PARALLEL_LEVEL`] [`[--dump-path](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--dump-path)`=`DUMP_PATH`] [`[--dump-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--dump-type)`=`DUMP_TYPE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--filter)`=`FILTER`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--source)`=`SOURCE`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--type)`=`TYPE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--all-databases](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--all-databases)`     | `[--databases-filter](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--databases-filter)`=`databaseName`,[…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--remove-labels)`=[`KEY`,…]] [`[--max-concurrent-cdc-connections](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--max-concurrent-cdc-connections)`=`MAX_CONCURRENT_CDC_CONNECTIONS` `[--max-concurrent-full-dump-connections](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--max-concurrent-full-dump-connections)`=`MAX_CONCURRENT_FULL_DUMP_CONNECTIONS` `[--max-concurrent-destination-connections](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--max-concurrent-destination-connections)`=`MAX_CONCURRENT_DESTINATION_CONNECTIONS` `[--transaction-timeout](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--transaction-timeout)`=`TRANSACTION_TIMEOUT`] [`[--peer-vpc](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--peer-vpc)`=`PEER_VPC`     | `[--static-ip](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--static-ip)`     | `[--vm](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--vm)`=`VM` `[--vm-ip](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--vm-ip)`=`VM_IP` `[--vm-port](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--vm-port)`=`VM_PORT` `[--vpc](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--vpc)`=`VPC`] [`[--sqlserver-databases](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--sqlserver-databases)`=`databaseName`,[…] `[--sqlserver-diff-backup](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--sqlserver-diff-backup)` `[--sqlserver-encrypted-databases](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--sqlserver-encrypted-databases)`=`SQLSERVER_ENCRYPTED_DATABASES` `[--sqlserver-promote-when-ready](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#--sqlserver-promote-when-ready)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Database Migration Service migration job.

- Draft migration job: user can update all available flags.
- Any other state can only update flags: `--display-name`,
`--dump-path`, and connectivity method flags.

**EXAMPLES**

: To update the source and destination connection profiles of a draft migration
job:

```
gcloud database-migration migration-jobs update my-migration-job --region=us-central1 --source=new-src --destination=new-dest
```

To update the display name of a running migration job:

```
gcloud database-migration migration-jobs update my-migration-job --region=us-central1 --display-name=new-name
```

**POSITIONAL ARGUMENTS**

: **Migration job resource - The migration job to update. The arguments in this
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

**FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--commit-id**:
Commit id for the conversion workspace to use for creating the migration job. If
not specified, the latest commit id will be used by default.

**Connection profile resource - ID of the destination connection profile,
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

**--destination**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--destination` on the command line.**

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

**--source**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--source` on the command line.**

**--type**:
Type of the migration job. `TYPE` must be one of:
`ONE_TIME`, `CONTINUOUS`.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--all-databases**

**--clear-labels**

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
gcloud alpha database-migration migration-jobs update
```