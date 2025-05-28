# gcloud sql instances patch  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch)*

**NAME**

: **gcloud sql instances patch - updates the settings of a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql instances patch` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#INSTANCE)` [`[--activation-policy](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--activation-policy)`=`ACTIVATION_POLICY`] [`[--active-directory-domain](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--active-directory-domain)`=`ACTIVE_DIRECTORY_DOMAIN`] [`[--[no-]assign-ip](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]assign-ip)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--async)`] [`[--audit-bucket-path](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--audit-bucket-path)`=`AUDIT_BUCKET_PATH`] [`[--audit-retention-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--audit-retention-interval)`=`AUDIT_RETENTION_INTERVAL`] [`[--audit-upload-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--audit-upload-interval)`=`AUDIT_UPLOAD_INTERVAL`] [`[--availability-type](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--availability-type)`=`AVAILABILITY_TYPE`] [`[--clear-failover-dr-replica-name](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--clear-failover-dr-replica-name)`] [`[--clear-password-policy](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--clear-password-policy)`] [`[--connector-enforcement](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--connector-enforcement)`=`CONNECTOR_ENFORCEMENT`] [`[--cpu](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--cpu)`=`CPU`] [`[--database-version](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--database-version)`=`DATABASE_VERSION`] [`[--[no-]deletion-protection](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]deletion-protection)`] [`[--deny-maintenance-period-end-date](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--deny-maintenance-period-end-date)`=`DENY_MAINTENANCE_PERIOD_END_DATE`] [`[--deny-maintenance-period-start-date](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--deny-maintenance-period-start-date)`=`DENY_MAINTENANCE_PERIOD_START_DATE`] [`[--deny-maintenance-period-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--deny-maintenance-period-time)`=`DENY_MAINTENANCE_PERIOD_TIME`] [`[--diff](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--diff)`] [`[--edition](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--edition)`=`EDITION`] [`[--[no-]enable-bin-log](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]enable-bin-log)`] [`[--[no-]enable-data-cache](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]enable-data-cache)`] [`[--[no-]enable-database-replication](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]enable-database-replication)`] [`[--[no-]enable-dataplex-integration](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]enable-dataplex-integration)`] [`[--[no-]enable-google-ml-integration](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]enable-google-ml-integration)`] [`[--[no-]enable-google-private-path](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]enable-google-private-path)`] [`[--enable-password-policy](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--enable-password-policy)`] [`[--enable-point-in-time-recovery](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--enable-point-in-time-recovery)`] [`[--[no-]enable-private-service-connect](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]enable-private-service-connect)`] [`[--failover-dr-replica-name](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--failover-dr-replica-name)`=`FAILOVER_DR_REPLICA_NAME`] [`[--follow-gae-app](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--follow-gae-app)`=`FOLLOW_GAE_APP`] [`[--[no-]include-replicas-for-major-version-upgrade](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]include-replicas-for-major-version-upgrade)`] [`[--[no-]insights-config-query-insights-enabled](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]insights-config-query-insights-enabled)`] [`[--insights-config-query-plans-per-minute](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--insights-config-query-plans-per-minute)`=`INSIGHTS_CONFIG_QUERY_PLANS_PER_MINUTE`] [`[--insights-config-query-string-length](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--insights-config-query-string-length)`=`INSIGHTS_CONFIG_QUERY_STRING_LENGTH`] [`[--[no-]insights-config-record-application-tags](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]insights-config-record-application-tags)`] [`[--[no-]insights-config-record-client-address](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]insights-config-record-client-address)`] [`[--maintenance-release-channel](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--maintenance-release-channel)`=`MAINTENANCE_RELEASE_CHANNEL`] [`[--maintenance-version](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--maintenance-version)`=`MAINTENANCE_VERSION`] [`[--maintenance-window-any](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--maintenance-window-any)`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY`] [`[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--memory](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--memory)`=`MEMORY`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--network)`=`NETWORK`] [`[--password-policy-complexity](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--password-policy-complexity)`=`PASSWORD_POLICY_COMPLEXITY`] [`[--[no-]password-policy-disallow-username-substring](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]password-policy-disallow-username-substring)`] [`[--password-policy-min-length](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--password-policy-min-length)`=`PASSWORD_POLICY_MIN_LENGTH`] [`[--password-policy-password-change-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--password-policy-password-change-interval)`=`PASSWORD_POLICY_PASSWORD_CHANGE_INTERVAL`] [`[--password-policy-reuse-interval](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--password-policy-reuse-interval)`=`PASSWORD_POLICY_REUSE_INTERVAL`] [`[--pricing-plan](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--pricing-plan)`=`PRICING_PLAN`, `[-p](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#-p)` `[PRICING_PLAN](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#PRICING_PLAN)`] [`[--[no-]recreate-replicas-on-primary-crash](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]recreate-replicas-on-primary-crash)`] [`[--remove-deny-maintenance-period](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--remove-deny-maintenance-period)`] [`[--replication](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--replication)`=`REPLICATION`] [`[--[no-]require-ssl](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]require-ssl)`] [`[--[no-]retain-backups-on-delete](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]retain-backups-on-delete)`] [`[--simulate-maintenance-event](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--simulate-maintenance-event)`] [`[--ssl-mode](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--ssl-mode)`=`SSL_MODE`] [`[--[no-]storage-auto-increase](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--[no-]storage-auto-increase)`] [`[--storage-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--storage-provisioned-iops)`=`STORAGE_PROVISIONED_IOPS`] [`[--storage-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--storage-provisioned-throughput)`=`STORAGE_PROVISIONED_THROUGHPUT`] [`[--storage-size](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--storage-size)`=`STORAGE_SIZE`] [`[--switch-transaction-logs-to-cloud-storage](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--switch-transaction-logs-to-cloud-storage)`] [`[--threads-per-core](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--threads-per-core)`=`THREADS_PER_CORE`] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--tier)`=`TIER`, `[-t](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#-t)` `[TIER](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#TIER)`] [`[--time-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--time-zone)`=`TIME_ZONE`] [`[--upgrade-sql-network-architecture](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--upgrade-sql-network-architecture)`] [`[--allowed-psc-projects](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--allowed-psc-projects)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#PROJECT)`,…]     | `[--clear-allowed-psc-projects](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--clear-allowed-psc-projects)`] [`[--authorized-gae-apps](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--authorized-gae-apps)`=`APP`,[`[APP](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#APP)`,…]     | `[--clear-gae-apps](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--clear-gae-apps)`] [`[--authorized-networks](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--authorized-networks)`=`NETWORK`,[`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#NETWORK)`,…]     | `[--clear-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--clear-authorized-networks)`] [`[--clear-custom-subject-alternative-names](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--clear-custom-subject-alternative-names)`     | `[--custom-subject-alternative-names](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--custom-subject-alternative-names)`=`DNS`,[`[DNS](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#DNS)`,[`[DNS](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#DNS)`]]] [`[--clear-database-flags](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--clear-database-flags)`     | `[--database-flags](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--database-flags)`=`FLAG`=`VALUE`,[`[FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#FLAG)`=`VALUE`,…]] [`[--gce-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--gce-zone)`=`GCE_ZONE`     | `[--secondary-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--secondary-zone)`=`SECONDARY_ZONE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--zone)`=`ZONE`] [`[--no-backup](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--backup)`     | `[--backup-location](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--backup-location)`=`BACKUP_LOCATION` `[--backup-start-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--backup-start-time)`=`BACKUP_START_TIME` `[--retained-backups-count](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--retained-backups-count)`=`RETAINED_BACKUPS_COUNT` `[--retained-transaction-log-days](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--retained-transaction-log-days)`=`RETAINED_TRANSACTION_LOG_DAYS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the settings of a Cloud SQL instance.

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

**--availability-type**:
Specifies level of availability. `AVAILABILITY_TYPE` must
be one of:

**`regional`**:
Provides high availability and is recommended for production instances; instance
automatically fails over to another zone within your selected region.

**`zonal`**:
Provides no failover capability. This is the default.

**--clear-failover-dr-replica-name**:
Clear the DR replica setting for the primary instance. Flag is only available
for MySQL and PostgreSQL database instances.

**--clear-password-policy**:
Clear the existing password policy. This flag is only available for Postgres.

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

**--database-version**:
The database engine type and versions. If left unspecified, no changes occur.
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

**--diff**:
Show what changed as a result of the update.

**--edition**:
Specifies the edition of Cloud SQL instance. `EDITION`
must be one of: `enterprise`, `enterprise-plus`.

**--[no-]enable-bin-log**:
Allows for data recovery from a specific point in time, down to a fraction of a
second. Must have automatic backups enabled to use. Make sure storage can
support at least 7 days of logs. Use `--enable-bin-log` to enable and
`--no-enable-bin-log` to disable.

**--[no-]enable-data-cache**:
Enable use of data cache for accelerated read performance. This flag is only
available for Enterprise_Plus edition instances. Use
`--enable-data-cache` to enable and
`--no-enable-data-cache` to disable.

**--[no-]enable-database-replication**:
Enable database replication. Applicable only for read replica instance(s).
WARNING: Instance will be restarted. Use
`--enable-database-replication` to enable and
`--no-enable-database-replication` to disable.

**--[no-]enable-dataplex-integration**:
Enable Dataplex integration for Google Cloud SQL. Use
`--enable-dataplex-integration` to enable and
`--no-enable-dataplex-integration` to disable.

**--[no-]enable-google-ml-integration**:
Enable Vertex AI integration for Google Cloud SQL. You can integrate Vertex AI
with Cloud SQL for MySQL and Cloud SQL for PostgreSQL instances only. Use
`--enable-google-ml-integration` to enable and
`--no-enable-google-ml-integration` to disable.

**--[no-]enable-google-private-path**:
Enable a private path for Google Cloud services. This flag specifies whether the
instance is accessible to internal Google Cloud services such as BigQuery. This
is only applicable to MySQL and PostgreSQL instances that don't use public IP.
Currently, SQL Server isn't supported. Use
`--enable-google-private-path` to enable and
`--no-enable-google-private-path` to disable.

**--enable-password-policy**:
Enable the password policy, which enforces user password management with the
policies configured for the instance. This flag is only available for Postgres.

**--enable-point-in-time-recovery**:
Allows for data recovery from a specific point in time, down to a fraction of a
second, via write-ahead logs. Must have automatic backups enabled to use. Make
sure storage can support at least 7 days of logs.

**--[no-]enable-private-service-connect**:
Enable connecting to the Cloud SQL instance with Private Service Connect. Use
`--enable-private-service-connect` to enable and
`--no-enable-private-service-connect` to disable.

**--failover-dr-replica-name**:
Set a Disaster Recovery (DR) replica with the specified name for the primary
instance. This must be one of the existing cross region replicas of the primary
instance. Flag is only available for MySQL and PostgreSQL database instances.

**--follow-gae-app**:
First Generation instances only. The App Engine app this instance should follow.
It must be in the same region as the instance. WARNING: Instance may be
restarted.

**--[no-]include-replicas-for-major-version-upgrade**:
Enable the major version upgrade of replicas when the in-place major version
upgrade of a primary instance is initated with `--database-version`.
Use `--include-replicas-for-major-version-upgrade` to enable and
`--no-include-replicas-for-major--version-upgrade` to disable. Use
`--include-replicas-for-major-version-upgrade` to enable and
`--no-include-replicas-for-major-version-upgrade` to disable.

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

**--maintenance-version**:
The desired maintenance version of the instance.

**--maintenance-window-any**:
Removes the user-specified maintenance window.

**--maintenance-window-day**:
Day of week for maintenance window, in UTC time zone.
`MAINTENANCE_WINDOW_DAY` must be one of: `SUN`,
`MON`, `TUE`, `WED`, `THU`,
`FRI`, `SAT`.

**--maintenance-window-hour**:
Hour of day for maintenance window, in UTC time zone.

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

**--pricing-plan**:
First Generation instances only. The pricing plan for this instance.
`PRICING_PLAN` must be one of: `PER_USE`,
`PACKAGE`.

**--[no-]recreate-replicas-on-primary-crash**:
Allow/Disallow replica recreation when a primary MySQL instance operating in
reduced durability mode crashes. Not recreating the replicas might lead to data
inconsistencies between the primary and its replicas. This setting is only
applicable for MySQL instances and is enabled by default. Use
`--recreate-replicas-on-primary-crash` to enable and
`--no-recreate-replicas-on-primary-crash` to disable.

**--remove-deny-maintenance-period**:
Removes the user-specified deny maintenance period.

**--replication**:
Type of replication this instance uses. The default is synchronous.
`REPLICATION` must be one of: `synchronous`,
`asynchronous`.

**--[no-]require-ssl**:
mysqld should default to 'REQUIRE X509' for users connecting over IP. Use
`--require-ssl` to enable and `--no-require-ssl` to
disable.

**--[no-]retain-backups-on-delete**:
Retain automated/ondemand backups of the instance after the instance is deleted.
Use `--retain-backups-on-delete` to enable and
`--no-retain-backups-on-delete` to disable.

**--simulate-maintenance-event**:
Simulate a maintenance event without changing the version. Only applicable to
instances that support near-zero downtime planned maintenance.

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

**--switch-transaction-logs-to-cloud-storage**:
Switches the location of the transaction logs used for PITR from disk to Cloud
Storage.

**--threads-per-core**:
The number of threads per core. The value of this flag can be 1 or 2. To disable
SMT, set this flag to 1. Only available in Cloud SQL for SQL Server instances.

**--tier**:
Machine type for a shared-core instance e.g.
``db-g1-small``. For all other instances,
instead of using tiers, customize your instance by specifying its CPU and
memory. You can do so with the `--cpu` and `--memory`
flags. Learn more about how CPU and memory affects pricing: [https://cloud.google.com/sql/pricing](https://cloud.google.com/sql/pricing).
WARNING: Instance will be restarted.

**--time-zone**:
Set a non-default time zone. Only available for SQL Server instances.

**--upgrade-sql-network-architecture**:
Upgrade from old network architecture to new network architecture. The new
network architecture offers better isolation, reliability, and faster new
feature adoption.

**--allowed-psc-projects**

**--authorized-gae-apps**

**--authorized-networks**

**--clear-custom-subject-alternative-names**

**--clear-database-flags**

**--gce-zone**

**--no-backup**

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
gcloud alpha sql instances patch
```

```
gcloud beta sql instances patch
```