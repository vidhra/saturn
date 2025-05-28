# gcloud sql backups restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore)*

**NAME**

: **gcloud sql backups restore - restores a backup of a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql backups restore` `[ID](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#ID)` `[--restore-instance](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--restore-instance)`=`RESTORE_INSTANCE` [`[--activation-policy](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--activation-policy)`=`ACTIVATION_POLICY`] [`[--active-directory-domain](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--active-directory-domain)`=`ACTIVE_DIRECTORY_DOMAIN`] [`[--[no-]assign-ip](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--[no-]assign-ip)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--async)`] [`[--audit-bucket-path](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--audit-bucket-path)`=`AUDIT_BUCKET_PATH`] [`[--audit-retention-interval](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--audit-retention-interval)`=`AUDIT_RETENTION_INTERVAL`] [`[--audit-upload-interval](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--audit-upload-interval)`=`AUDIT_UPLOAD_INTERVAL`] [`[--authorized-networks](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--authorized-networks)`=`NETWORK`,[`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#NETWORK)`,…]] [`[--availability-type](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--availability-type)`=`AVAILABILITY_TYPE`] [`[--no-backup](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--backup)`] [`[--backup-instance](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--backup-instance)`=`BACKUP_INSTANCE`] [`[--backup-location](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--backup-location)`=`BACKUP_LOCATION`] [`[--backup-project](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--backup-project)`=`BACKUP_PROJECT`] [`[--backup-start-time](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--backup-start-time)`=`BACKUP_START_TIME`] [`[--collation](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--collation)`=`COLLATION`] [`[--connector-enforcement](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--connector-enforcement)`=`CONNECTOR_ENFORCEMENT`] [`[--cpu](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--cpu)`=`CPU`] [`[--database-version](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--database-version)`=`DATABASE_VERSION`] [`[--[no-]deletion-protection](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--[no-]deletion-protection)`] [`[--deny-maintenance-period-end-date](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--deny-maintenance-period-end-date)`=`DENY_MAINTENANCE_PERIOD_END_DATE`] [`[--deny-maintenance-period-start-date](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--deny-maintenance-period-start-date)`=`DENY_MAINTENANCE_PERIOD_START_DATE`] [`[--deny-maintenance-period-time](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--deny-maintenance-period-time)`=`DENY_MAINTENANCE_PERIOD_TIME`] [`[--edition](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--edition)`=`EDITION`] [`[--enable-bin-log](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--enable-bin-log)`] [`[--enable-google-private-path](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--enable-google-private-path)`] [`[--enable-point-in-time-recovery](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--enable-point-in-time-recovery)`] [`[--insights-config-query-insights-enabled](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--insights-config-query-insights-enabled)`] [`[--insights-config-query-plans-per-minute](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--insights-config-query-plans-per-minute)`=`INSIGHTS_CONFIG_QUERY_PLANS_PER_MINUTE`] [`[--insights-config-query-string-length](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--insights-config-query-string-length)`=`INSIGHTS_CONFIG_QUERY_STRING_LENGTH`] [`[--insights-config-record-application-tags](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--insights-config-record-application-tags)`] [`[--insights-config-record-client-address](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--insights-config-record-client-address)`] [`[--maintenance-release-channel](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--maintenance-release-channel)`=`MAINTENANCE_RELEASE_CHANNEL`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY`] [`[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--memory](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--memory)`=`MEMORY`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--network)`=`NETWORK`] [`[--require-ssl](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--require-ssl)`] [`[--retained-backups-count](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--retained-backups-count)`=`RETAINED_BACKUPS_COUNT`] [`[--retained-transaction-log-days](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--retained-transaction-log-days)`=`RETAINED_TRANSACTION_LOG_DAYS`] [`[--ssl-mode](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--ssl-mode)`=`SSL_MODE`] [`[--[no-]storage-auto-increase](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--[no-]storage-auto-increase)`] [`[--storage-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--storage-provisioned-iops)`=`STORAGE_PROVISIONED_IOPS`] [`[--storage-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--storage-provisioned-throughput)`=`STORAGE_PROVISIONED_THROUGHPUT`] [`[--storage-size](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--storage-size)`=`STORAGE_SIZE`] [`[--storage-type](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--storage-type)`=`STORAGE_TYPE`] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--tier)`=`TIER`, `[-t](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#-t)` `[TIER](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#TIER)`] [`[--time-zone](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--time-zone)`=`TIME_ZONE`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--timeout)`=`TIMEOUT`; default=3600] [`[--allowed-psc-projects](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--allowed-psc-projects)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#PROJECT)`,…] `[--enable-private-service-connect](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--enable-private-service-connect)`] [`[--disk-encryption-key](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--disk-encryption-key)`=`DISK_ENCRYPTION_KEY` : `[--disk-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--disk-encryption-key-keyring)`=`DISK_ENCRYPTION_KEY_KEYRING` `[--disk-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--disk-encryption-key-location)`=`DISK_ENCRYPTION_KEY_LOCATION` `[--disk-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--disk-encryption-key-project)`=`DISK_ENCRYPTION_KEY_PROJECT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--region)`=`REGION`     | `[--gce-zone](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--gce-zone)`=`GCE_ZONE`     | `[--secondary-zone](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--secondary-zone)`=`SECONDARY_ZONE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/backups/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The command lets you restore to an existing instance using ID. When backup Name
is used for restore it lets you restore to an existing instance or a new
instance. When restoring to new instance, optional flags can be used to
customize the new instance.

**POSITIONAL ARGUMENTS**

: **`ID`**:
The ID of the backup run to restore from or the backup NAME for restore to
existing/new instance. To find the NAME, run the following command: $ [gcloud sql backups list](https://cloud.google.com/sdk/gcloud/reference/sql/backups/list)
--filter=instance:{instance}

**REQUIRED FLAGS**

: **--restore-instance**:
The ID of the target Cloud SQL instance that the backup is restored to.

**OPTIONAL FLAGS**

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

**--backup-instance**:
The ID of the instance that the backup was taken from. This argument must be
specified when the backup instance is different from the restore instance. If it
is not specified, the backup instance is considered the same as the restore
instance. This flag is not supported when restore happens from backup name, only
supported when restore happens from backup ID in timestamp format.

**--backup-location**:
Choose where to store your backups. Backups are stored in the closest
multi-region location to you by default. Only customize if needed.

**--backup-project**:
The project of the instance to which the backup belongs. If it isn't specified,
backup and restore instances are in the same project. This flag is not supported
when restore happens from backup name, only supported when restore happens from
backup ID in timestamp format.

**--backup-start-time**:
Start time of daily backups, specified in the HH:MM format, in the UTC timezone.

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

**--database-version**:
The database engine type and versions. If left unspecified, no changes occur.
See the list of database versions at [https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion).
Note for restore to new instance major version upgrades are not supported. Only
minor version upgrades are allowed.

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

**--enable-google-private-path**:
Enable a private path for Google Cloud services. This flag specifies whether the
instance is accessible to internal Google Cloud services such as BigQuery. This
is only applicable to MySQL and PostgreSQL instances that don't use public IP.
Currently, SQL Server isn't supported.

**--enable-point-in-time-recovery**:
Allows for data recovery from a specific point in time, down to a fraction of a
second, via write-ahead logs. Must have automatic backups enabled to use. Make
sure storage can support at least 7 days of logs.

**--insights-config-query-insights-enabled**:
Enable query insights feature to provide query and query plan analytics.

**--insights-config-query-plans-per-minute**:
Number of query plans to sample every minute. Default value is 5. Allowed range:
0 to 20.

**--insights-config-query-string-length**:
Query string length in bytes to be stored by the query insights feature. Default
length is 1024 bytes. Allowed range: 256 to 4500 bytes.

**--insights-config-record-application-tags**:
Allow application tags to be recorded by the query insights feature.

**--insights-config-record-client-address**:
Allow the client address to be recorded by the query insights feature.

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

**--require-ssl**:
Specified if users connecting over IP must use SSL.

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
gcloud alpha sql backups restore
```

```
gcloud beta sql backups restore
```