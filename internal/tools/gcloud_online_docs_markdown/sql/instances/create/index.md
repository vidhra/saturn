# gcloud sql instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/create](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create)*

**NAME**

: **gcloud sql instances create - creates a new Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql instances create` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#INSTANCE)` [`[--activation-policy](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--activation-policy)`=`ACTIVATION_POLICY`] [`[--active-directory-domain](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--active-directory-domain)`=`ACTIVE_DIRECTORY_DOMAIN`] [`[--[no-]assign-ip](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]assign-ip)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--async)`] [`[--audit-bucket-path](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--audit-bucket-path)`=`AUDIT_BUCKET_PATH`] [`[--audit-retention-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--audit-retention-interval)`=`AUDIT_RETENTION_INTERVAL`] [`[--audit-upload-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--audit-upload-interval)`=`AUDIT_UPLOAD_INTERVAL`] [`[--authorized-networks](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--authorized-networks)`=`NETWORK`,[`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#NETWORK)`,…]] [`[--availability-type](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--availability-type)`=`AVAILABILITY_TYPE`] [`[--no-backup](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--backup)`] [`[--backup-location](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--backup-location)`=`BACKUP_LOCATION`] [`[--backup-start-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--backup-start-time)`=`BACKUP_START_TIME`] [`[--cascadable-replica](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--cascadable-replica)`] [`[--collation](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--collation)`=`COLLATION`] [`[--connector-enforcement](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--connector-enforcement)`=`CONNECTOR_ENFORCEMENT`] [`[--cpu](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--cpu)`=`CPU`] [`[--custom-subject-alternative-names](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--custom-subject-alternative-names)`=`DNS`,[`[DNS](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#DNS)`,[`[DNS](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#DNS)`]]] [`[--database-flags](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-flags)`=`FLAG`=`VALUE`,[`[FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#FLAG)`=`VALUE`,…]] [`[--database-version](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-version)`=`DATABASE_VERSION`; default=`"MYSQL_8_0"`] [`[--[no-]deletion-protection](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]deletion-protection)`] [`[--deny-maintenance-period-end-date](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--deny-maintenance-period-end-date)`=`DENY_MAINTENANCE_PERIOD_END_DATE`] [`[--deny-maintenance-period-start-date](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--deny-maintenance-period-start-date)`=`DENY_MAINTENANCE_PERIOD_START_DATE`] [`[--deny-maintenance-period-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--deny-maintenance-period-time)`=`DENY_MAINTENANCE_PERIOD_TIME`] [`[--edition](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--edition)`=`EDITION`] [`[--enable-bin-log](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--enable-bin-log)`] [`[--[no-]enable-data-cache](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]enable-data-cache)`] [`[--[no-]enable-dataplex-integration](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]enable-dataplex-integration)`] [`[--[no-]enable-google-ml-integration](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]enable-google-ml-integration)`] [`[--enable-google-private-path](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--enable-google-private-path)`] [`[--enable-password-policy](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--enable-password-policy)`] [`[--enable-point-in-time-recovery](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--enable-point-in-time-recovery)`] [`[--failover-replica-name](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--failover-replica-name)`=`FAILOVER_REPLICA_NAME`] [`[--[no-]insights-config-query-insights-enabled](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]insights-config-query-insights-enabled)`] [`[--insights-config-query-plans-per-minute](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--insights-config-query-plans-per-minute)`=`INSIGHTS_CONFIG_QUERY_PLANS_PER_MINUTE`] [`[--insights-config-query-string-length](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--insights-config-query-string-length)`=`INSIGHTS_CONFIG_QUERY_STRING_LENGTH`] [`[--[no-]insights-config-record-application-tags](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]insights-config-record-application-tags)`] [`[--[no-]insights-config-record-client-address](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]insights-config-record-client-address)`] [`[--maintenance-release-channel](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--maintenance-release-channel)`=`MAINTENANCE_RELEASE_CHANNEL`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY`] [`[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--master-instance-name](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--master-instance-name)`=`MASTER_INSTANCE_NAME`] [`[--memory](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--memory)`=`MEMORY`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--network)`=`NETWORK`] [`[--password-policy-complexity](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--password-policy-complexity)`=`PASSWORD_POLICY_COMPLEXITY`] [`[--[no-]password-policy-disallow-username-substring](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]password-policy-disallow-username-substring)`] [`[--password-policy-min-length](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--password-policy-min-length)`=`PASSWORD_POLICY_MIN_LENGTH`] [`[--password-policy-password-change-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--password-policy-password-change-interval)`=`PASSWORD_POLICY_PASSWORD_CHANGE_INTERVAL`] [`[--password-policy-reuse-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--password-policy-reuse-interval)`=`PASSWORD_POLICY_REUSE_INTERVAL`] [`[--psc-auto-connections](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--psc-auto-connections)`=[`network`=`NETWORK`],[`project`=`PROJECT`]] [`[--[no-]recreate-replicas-on-primary-crash](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]recreate-replicas-on-primary-crash)`] [`[--replica-type](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--replica-type)`=`REPLICA_TYPE`] [`[--replication](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--replication)`=`REPLICATION`] [`[--require-ssl](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--require-ssl)`] [`[--[no-]retain-backups-on-delete](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]retain-backups-on-delete)`] [`[--retained-backups-count](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--retained-backups-count)`=`RETAINED_BACKUPS_COUNT`] [`[--retained-transaction-log-days](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--retained-transaction-log-days)`=`RETAINED_TRANSACTION_LOG_DAYS`] [`[--root-password](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--root-password)`=`ROOT_PASSWORD`] [`[--server-ca-mode](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--server-ca-mode)`=`SERVER_CA_MODE`] [`[--server-ca-pool](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--server-ca-pool)`=`SERVER_CA_POOL`] [`[--ssl-mode](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--ssl-mode)`=`SSL_MODE`] [`[--[no-]storage-auto-increase](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--[no-]storage-auto-increase)`] [`[--storage-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--storage-provisioned-iops)`=`STORAGE_PROVISIONED_IOPS`] [`[--storage-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--storage-provisioned-throughput)`=`STORAGE_PROVISIONED_THROUGHPUT`] [`[--storage-size](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--storage-size)`=`STORAGE_SIZE`] [`[--storage-type](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--storage-type)`=`STORAGE_TYPE`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--tags)`=`TAG`=`VALUE`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#TAG)`=`VALUE`,…]] [`[--threads-per-core](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--threads-per-core)`=`THREADS_PER_CORE`] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--tier)`=`TIER`, `[-t](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#-t)` `[TIER](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#TIER)`] [`[--time-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--time-zone)`=`TIME_ZONE`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--timeout)`=`TIMEOUT`; default=3600] [`[--allowed-psc-projects](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--allowed-psc-projects)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#PROJECT)`,…] `[--enable-private-service-connect](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--enable-private-service-connect)`] [`[--disk-encryption-key](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--disk-encryption-key)`=`DISK_ENCRYPTION_KEY` : `[--disk-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--disk-encryption-key-keyring)`=`DISK_ENCRYPTION_KEY_KEYRING` `[--disk-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--disk-encryption-key-location)`=`DISK_ENCRYPTION_KEY_LOCATION` `[--disk-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--disk-encryption-key-project)`=`DISK_ENCRYPTION_KEY_PROJECT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--region)`=`REGION`; default="us-central"     | `[--gce-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--gce-zone)`=`GCE_ZONE`     | `[--secondary-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--secondary-zone)`=`SECONDARY_ZONE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new Cloud SQL instance.

**EXAMPLES**

: To create a MySQL 8.0 instance with ID
``prod-instance`` that has 2 CPUs, 4 GB of RAM,
and is in the region ``us-central1`` (a zone
will be auto-assigned), where the 'root' user has its password set to
``password123``, run:

```
gcloud sql instances create prod-instance --database-version=MYSQL_8_0 --cpu=2 --memory=4GB --region=us-central1 --root-password=password123
```

To create a Postgres 15 instance with ID
``prod-instance`` that has 2 CPUs, 8 GiB of
RAM, and is in the zone ``us-central1-a``,
where the 'postgres' user has its password set to
``password123``, run:

```
gcloud sql instances create prod-instance --database-version=POSTGRES_15 --cpu=2 --memory=8GiB --zone=us-central1-a --root-password=password123
```

To create a SQL Server 2022 Express instance with ID
``prod-instance`` that has 2 CPUs, 3840MiB of
RAM, and is in the zone ``us-central1-a``,
where the 'sqlserver' user has its password set to
``password123``, run:

```
gcloud sql instances create prod-instance --database-version=SQLSERVER_2022_EXPRESS --cpu=2 --memory=3840MiB --zone=us-central1-a --root-password=password123
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**FLAGS**

: **--activation-policy**:
Activation policy for this instance. This specifies when the instance should be
activated and is applicable only when the instance state is
`RUNNABLE`. The default is `always`. More information on
activation policies can be found here: [https://cloud.google.com/sql/docs/mysql/start-stop-restart-instance#activation_policy](https://cloud.google.com/sql/docs/mysql/start-stop-restart-instance#activation_policy).
`ACTIVATION_POLICY` must be one of: `always`,
`never`.

**--active-directory-domain**:
Managed Service for Microsoft Active Directory domain this instance is joined
to. Only available for SQL Server instances.

**--[no-]assign-ip**:
Assign a public IP address to the instance. This is a public, externally
available IPv4 address that you can use to connect to your instance when
properly authorized. Use `--assign-ip` to enable and
`--no-assign-ip` to disable.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--audit-bucket-path**:
The location, as a Cloud Storage bucket, to which audit files are uploaded. The
URI is in the form gs://bucketName/folderName. Only available for SQL Server
instances.

**--audit-retention-interval**:
The number of days for audit log retention on disk, for example, 3dfor 3 days.
Only available for SQL Server instances.

**--audit-upload-interval**:
How often to upload audit logs (audit files), for example, 30mfor 30 minutes.
Only available for SQL Server instances.

**--authorized-networks**:
The list of external networks that are allowed to connect to the instance.
Specified in CIDR notation, also known as 'slash' notation (e.g.
192.168.100.0/24).

**--availability-type**:
Specifies level of availability. `AVAILABILITY_TYPE` must
be one of:

**`regional`**:
Provides high availability and is recommended for production instances; instance
automatically fails over to another zone within your selected region.

**`zonal`**:
Provides no failover capability. This is the default.

**--backup**:
Enables daily backup. Enabled by default, use `--no-backup` to
disable.

**--backup-location**:
Choose where to store your backups. Backups are stored in the closest
multi-region location to you by default. Only customize if needed.

**--backup-start-time**:
Start time of daily backups, specified in the HH:MM format, in the UTC timezone.

**--cascadable-replica**:
Specifies whether a SQL Server replica is a cascadable replica. A cascadable
replica is a SQL Server cross-region replica that supports replica(s) under it.
This flag only takes effect when the `--master-instance-name` flag is
set, and the replica under creation is in a different region than the primary
instance.

**--collation**:
Cloud SQL server-level collation setting, which specifies the set of rules for
comparing characters in a character set.

**--connector-enforcement**:
Cloud SQL Connector enforcement mode. It determines how Cloud SQL Connectors are
used in the connection. See the list of modes [here](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#connectorenforcement).
`CONNECTOR_ENFORCEMENT` must be one of:

**`CONNECTOR_ENFORCEMENT_UNSPECIFIED`**:
The requirement for Cloud SQL connectors is unknown.

**`NOT_REQUIRED`**:
Does not require Cloud SQL connectors.

**`REQUIRED`**:
Requires all connections to use Cloud SQL connectors, including the Cloud SQL
Auth Proxy and Cloud SQL Java, Python, and Go connectors. Note: This disables
all existing authorized networks.

**--cpu**:
Whole number value indicating how many cores are desired in the machine. Both
--cpu and --memory must be specified if a custom machine type is desired, and
the --tier flag must be omitted.--cpu and --memory flags are not compatible with
the Enterprise Plus edition. These flags should not be used when creating an
Enterprise Plus edition, as the machine configuration is determined by the
--tier flag instead.

**--custom-subject-alternative-names**:
A comma-separated list of DNS names to add to the instance's SSL certificate. A
custom SAN is a structured way to add additional DNS names (host names) that are
not managed by Cloud SQL to an instance. It allows for hostname verification
during establishment of a database connection using the DNS name over SSL/TLS.
When you create and/or update an instance, you can add a comma-separated list of
up to three DNS names to the server certificate of your instance.

**--database-flags**:
Comma-separated list of database flags to set on the instance. Use an equals
sign to separate flag name and value. Flags without values, like
skip_grant_tables, can be written out without a value after, e.g.,
`skip_grant_tables=`. Use on/off for booleans. View the Instance
Resource API for allowed flags. (e.g., `--database-flags
max_allowed_packet=55555,skip_grant_tables=,log_output=1`)

**--database-version**:
The database engine type and versions. If left unspecified, MYSQL_8_0 is used.
See the list of database versions at [https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion).
Apart from listed major versions, DATABASE_VERSION also accepts supported minor
versions. `DATABASE_VERSION` must be one of:
`MYSQL_5_6`, `MYSQL_5_7`, `MYSQL_8_0`,
`MYSQL_8_4`, `POSTGRES_9_6`, `POSTGRES_10`,
`POSTGRES_11`, `POSTGRES_12`, `POSTGRES_13`,
`POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`,
`POSTGRES_17`, `SQLSERVER_2017_EXPRESS`,
`SQLSERVER_2017_WEB`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`,
`SQLSERVER_2019_WEB`, `SQLSERVER_2019_STANDARD`,
`SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2022_EXPRESS`,
`SQLSERVER_2022_WEB`, `SQLSERVER_2022_STANDARD`,
`SQLSERVER_2022_ENTERPRISE`.

**--[no-]deletion-protection**:
Enable deletion protection on a Cloud SQL instance. Use
`--deletion-protection` to enable and
`--no-deletion-protection` to disable.

**--deny-maintenance-period-end-date**:
Date when the deny maintenance period ends, that is
``2021-01-10``.

**--deny-maintenance-period-start-date**:
Date when the deny maintenance period begins, that is
``2020-11-01``.

**--deny-maintenance-period-time**:
Time when the deny maintenance period starts or ends, that is
``05:00:00``.

**--edition**:
Specifies the edition of Cloud SQL instance. `EDITION`
must be one of: `enterprise`, `enterprise-plus`.

**--enable-bin-log**:
Allows for data recovery from a specific point in time, down to a fraction of a
second. Must have automatic backups enabled to use. Make sure storage can
support at least 7 days of logs.

**--[no-]enable-data-cache**:
Enable use of data cache for accelerated read performance. This flag is only
available for Enterprise_Plus edition instances. Use
`--enable-data-cache` to enable and
`--no-enable-data-cache` to disable.

**--[no-]enable-dataplex-integration**:
Enable Dataplex integration for Google Cloud SQL. Use
`--enable-dataplex-integration` to enable and
`--no-enable-dataplex-integration` to disable.

**--[no-]enable-google-ml-integration**:
Enable Vertex AI integration for Google Cloud SQL. You can integrate Vertex AI
with Cloud SQL for MySQL and Cloud SQL for PostgreSQL instances only. Use
`--enable-google-ml-integration` to enable and
`--no-enable-google-ml-integration` to disable.

**--enable-google-private-path**:
Enable a private path for Google Cloud services. This flag specifies whether the
instance is accessible to internal Google Cloud services such as BigQuery. This
is only applicable to MySQL and PostgreSQL instances that don't use public IP.
Currently, SQL Server isn't supported.

**--enable-password-policy**:
Enable the password policy, which enforces user password management with the
policies configured for the instance. This flag is only available for Postgres.

**--enable-point-in-time-recovery**:
Allows for data recovery from a specific point in time, down to a fraction of a
second, via write-ahead logs. Must have automatic backups enabled to use. Make
sure storage can support at least 7 days of logs.

**--failover-replica-name**:
Also create a failover replica with the specified name.

**--[no-]insights-config-query-insights-enabled**:
Enable query insights feature to provide query and query plan analytics.
Use `--insights-config-query-insights-enabled` to enable and
`--no-insights-config-query-insights-enabled` to disable.

**--insights-config-query-plans-per-minute**:
Number of query plans to sample every minute. Default value is 5. Allowed range:
0 to 20.

**--insights-config-query-string-length**:
Query string length in bytes to be stored by the query insights feature. Default
length is 1024 bytes. Allowed range: 256 to 4500 bytes.

**--[no-]insights-config-record-application-tags**:
Allow application tags to be recorded by the query insights feature.
Use `--insights-config-record-application-tags` to enable and
`--no-insights-config-record-application-tags` to disable.

**--[no-]insights-config-record-client-address**:
Allow the client address to be recorded by the query insights feature.
Use `--insights-config-record-client-address` to enable and
`--no-insights-config-record-client-address` to disable.

**--maintenance-release-channel**:
Which channel's updates to apply during the maintenance window. If not
specified, Cloud SQL chooses the timing of updates to your instance.
`MAINTENANCE_RELEASE_CHANNEL` must be one of:

**`preview`**:
Preview updates release prior to production updates. You may wish to use the
preview channel for dev/test applications so that you can preview their
compatibility with your application prior to the production release.

**`production`**:
Production updates are stable and recommended for applications in production.

**`week5`**:
week5 updates release after the production updates. Use the week5 channel to
receive a 5 week advance notification about the upcoming maintenance, so you can
prepare your application for the release.

**--maintenance-window-day**:
Day of week for maintenance window, in UTC time zone.
`MAINTENANCE_WINDOW_DAY` must be one of: `SUN`,
`MON`, `TUE`, `WED`, `THU`,
`FRI`, `SAT`.

**--maintenance-window-hour**:
Hour of day for maintenance window, in UTC time zone.

**--master-instance-name**:
Name of the instance which will act as master in the replication setup. The
newly created instance will be a read replica of the specified master instance.

**--memory**:
Whole number value indicating how much memory is desired in the machine. A size
unit should be provided (eg. 3072MiB or 9GiB) - if no units are specified, GiB
is assumed. Both --cpu and --memory must be specified if a custom machine type
is desired, and the --tier flag must be omitted. --cpu and --memory flags are
not compatible with the Enterprise Plus edition. These flags should not be used
when creating an Enterprise Plus edition, as the machine configuration is
determined by the --tier flag instead.

**--network**:
Network in the current project that the instance will be part of. To specify
using a network with a shared VPC, use the full URL of the network. For an
example host project, 'testproject', and shared network, 'testsharednetwork',
this would use the form:
`--network`=`projects/testproject/global/networks/testsharednetwork`

**--password-policy-complexity**:
The complexity of the password. This flag is available only for PostgreSQL.
`PASSWORD_POLICY_COMPLEXITY` must be one of:

**`COMPLEXITY_DEFAULT`**:
A combination of lowercase, uppercase, numeric, and non-alphanumeric characters.

**`COMPLEXITY_UNSPECIFIED`**:
The default value if COMPLEXITY_DEFAULT is not specified. It implies that
complexity check is not enabled.

**--[no-]password-policy-disallow-username-substring**:
Disallow username as a part of the password. Use
`--password-policy-disallow-username-substring` to enable and
`--no-password-policy-disallow-username-substring` to disable.

**--password-policy-min-length**:
Minimum number of characters allowed in the password.

**--password-policy-password-change-interval**:
Minimum interval after which the password can be changed, for example, 2m for 2
minutes. See <a href="/sdk/gcloud/reference/topic/datetimes"> $ [gcloud topic](https://cloud.google.com/sdk/gcloud/reference/topic) datetimes</a> for
information on duration formats. This flag is available only for PostgreSQL.

**--password-policy-reuse-interval**:
Number of previous passwords that cannot be reused. The valid range is 0 to 100.

**--psc-auto-connections**:
A comma-separated list of networks or a comma-separated list of network-project
pairs. Each project in this list is represented by a project number (numeric) or
by a project ID (alphanumeric). This allows Private Service Connect connections
to be created automatically for the specified networks. For example, this
connection uses "the form
`psc-auto-connections`=`network=projects/testproject1/global/networks/testnetwork1`"
or "the form
`psc-auto-connections`=`project=testproject1,network=projects/testproject1/global/networks/testnetwork1`".
Sets `psc_auto_connections` value.

**`network`**:
Required, sets `network` value.

**`project`**:
Sets `project` value.

`Shorthand Example:`

```
--psc-auto-connections=network=string,project=string
```

`JSON Example:`

```
--psc-auto-connections='{"network": "string", "project": "string"}'
```

`File Example:`

```
--psc-auto-connections=path_to_file.(yaml|json)
```

**--[no-]recreate-replicas-on-primary-crash**:
Allow/Disallow replica recreation when a primary MySQL instance operating in
reduced durability mode crashes. Not recreating the replicas might lead to data
inconsistencies between the primary and its replicas. This setting is only
applicable for MySQL instances and is enabled by default. Use
`--recreate-replicas-on-primary-crash` to enable and
`--no-recreate-replicas-on-primary-crash` to disable.

**--replica-type**:
The type of replica to create. `REPLICA_TYPE` must be one
of: `READ`, `FAILOVER`.

**--replication**:
Type of replication this instance uses. The default is synchronous.
`REPLICATION` must be one of: `synchronous`,
`asynchronous`.

**--require-ssl**:
Specified if users connecting over IP must use SSL.

**--[no-]retain-backups-on-delete**:
Retain automated/ondemand backups of the instance after the instance is deleted.
Use `--retain-backups-on-delete` to enable and
`--no-retain-backups-on-delete` to disable.

**--retained-backups-count**:
How many backups to keep. The valid range is between 1 and 365. Default value is
7 for Enterprise edition instances. For Enterprise_Plus, default value is 15.
Applicable only if --no-backups is not specified.

**--retained-transaction-log-days**:
How many days of transaction logs to keep. The valid range is between 1 and 35.
Only use this option when point-in-time recovery is enabled. If logs are stored
on disk, storage size for transaction logs could increase when the number of
days for log retention increases. For Enterprise, default and max retention
values are 7 and 7 respectively. For Enterprise_Plus, default and max retention
values are 14 and 35.

**--root-password**:
Root Cloud SQL user's password.

**--server-ca-mode**:
Set the server CA mode of the instance. `SERVER_CA_MODE`
must be one of:

**`CUSTOMER_MANAGED_CAS_CA`**:
Customer-managed CA hosted on Google Cloud's Certificate Authority Service
(CAS).

**`GOOGLE_MANAGED_CAS_CA`**:
Google-managed regional CA part of root CA hierarchy hosted on Google Cloud's
Certificate Authority Service (CAS).

**`GOOGLE_MANAGED_INTERNAL_CA`**:
Google-managed self-signed internal CA.

**--server-ca-pool**:
Set the server CA pool of the instance.

**--ssl-mode**:
Set the SSL mode of the instance. `SSL_MODE` must be one
of:

**`ALLOW_UNENCRYPTED_AND_ENCRYPTED`**:
Allow non-SSL and SSL connections. For SSL connections, client certificate will
not be verified.

**`ENCRYPTED_ONLY`**:
Only allow connections encrypted with SSL/TLS.

**`TRUSTED_CLIENT_CERTIFICATE_REQUIRED`**:
Only allow connections encrypted with SSL/TLS and with valid client
certificates.

**--[no-]storage-auto-increase**:
Storage size can be increased, but it cannot be decreased; storage increases are
permanent for the life of the instance. With this setting enabled, a spike in
storage requirements can result in permanently increased storage costs for your
instance. However, if an instance runs out of available space, it can result in
the instance going offline, dropping existing connections. This setting is
enabled by default. Use `--storage-auto-increase` to enable and
`--no-storage-auto-increase` to disable.

**--storage-provisioned-iops**:
Indicates how many IOPS to provision for the data disk. This sets the number of
I/O operations per second that the disk can handle.

**--storage-provisioned-throughput**:
Indicates how much throughput to provision for the data disk. This sets the
throughput in MB per second that the disk can handle.

**--storage-size**:
Amount of storage allocated to the instance. Must be an integer number of GB.
The default is 10GB. Information on storage limits can be found here: [https://cloud.google.com/sql/docs/quotas#storage_limits](https://cloud.google.com/sql/docs/quotas#storage_limits)

**--storage-type**:
The storage type for the instance. The default is SSD.
`STORAGE_TYPE` must be one of: `SSD`,
`HDD`, `HYPERDISK_BALANCED`.

**--tags**:
Comma-separated list of tags to set on the instance. Use an equals signto
separate tag name and value.(e.g., `--tags tag1:value1,tag2=value2`)

**--threads-per-core**:
The number of threads per core. The value of this flag can be 1 or 2. To disable
SMT, set this flag to 1. Only available in Cloud SQL for SQL Server instances.

**--tier**:
Machine type for a shared-core instance e.g.
``db-g1-small``. For all other instances,
instead of using tiers, customize your instance by specifying its CPU and
memory. You can do so with the `--cpu` and `--memory`
flags. Learn more about how CPU and memory affects pricing: [https://cloud.google.com/sql/pricing](https://cloud.google.com/sql/pricing).

**--time-zone**:
Set a non-default time zone. Only available for SQL Server instances.

**--timeout**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --async flag is specified. By
default, set to 3600s. To wait indefinitely, set to `unlimited`.

**--allowed-psc-projects**:
A comma-separated list of projects. Each project in this list might be
represented by a project number (numeric) or by a project ID (alphanumeric).
This allows Private Service Connect connections to be established from specified
consumer projects.

**--enable-private-service-connect**:
Enable connecting to the Cloud SQL instance with Private Service Connect.

**--disk-encryption-key**

**--region**

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

: These variants are also available:

```
gcloud alpha sql instances create
```

```
gcloud beta sql instances create
```