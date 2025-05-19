# gcloud alloydb clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create)*

**NAME**

: **gcloud alloydb clusters create - create a new AlloyDB cluster within a given project**

**SYNOPSIS**

: **`gcloud alloydb clusters create` `[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#CLUSTER)` `[--password](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--password)`=`PASSWORD` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--region)`=`REGION` [`[--allocated-ip-range-name](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--allocated-ip-range-name)`=`ALLOCATED_IP_RANGE_NAME`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--async)`] [`[--database-version](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--database-version)`=`DATABASE_VERSION`] [`[--enable-private-service-connect](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--enable-private-service-connect)`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--network)`=`NETWORK`] [`[--subscription-type](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--subscription-type)`=`SUBSCRIPTION_TYPE`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--tags)`=[`KEY`=`VALUE`,…]] [`[--continuous-backup-recovery-window-days](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--continuous-backup-recovery-window-days)`=`RECOVERY_PERIOD` `[--enable-continuous-backup](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--enable-continuous-backup)` [`[--continuous-backup-encryption-key](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--continuous-backup-encryption-key)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY` : `[--continuous-backup-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--continuous-backup-encryption-key-keyring)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_KEYRING` `[--continuous-backup-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--continuous-backup-encryption-key-location)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_LOCATION` `[--continuous-backup-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--continuous-backup-encryption-key-project)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_PROJECT`]] [`[--deny-maintenance-period-end-date](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--deny-maintenance-period-end-date)`=`DENY_MAINTENANCE_PERIOD_END_DATE` `[--deny-maintenance-period-start-date](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--deny-maintenance-period-start-date)`=`DENY_MAINTENANCE_PERIOD_START_DATE` `[--deny-maintenance-period-time](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--deny-maintenance-period-time)`=`DENY_MAINTENANCE_PERIOD_TIME`] [`[--disable-automated-backup](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--disable-automated-backup)`     | [`[--automated-backup-days-of-week](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-days-of-week)`=[`DAYS_OF_WEEK`,…] `[--automated-backup-start-times](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-start-times)`=[`START_TIMES`,…] : `[--automated-backup-window](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-window)`=`TIMEOUT_PERIOD` [`[--automated-backup-encryption-key](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-encryption-key)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY` : `[--automated-backup-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-encryption-key-keyring)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_KEYRING` `[--automated-backup-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-encryption-key-location)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_LOCATION` `[--automated-backup-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-encryption-key-project)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_PROJECT`] `[--automated-backup-retention-count](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-retention-count)`=`RETENTION_COUNT` | `[--automated-backup-retention-period](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--automated-backup-retention-period)`=`RETENTION_PERIOD`]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--kms-project)`=`KMS_PROJECT`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new AlloyDB cluster within a given project.

**EXAMPLES**

: To create a new cluster, run:

```
gcloud alloydb clusters create my-cluster --region=us-central1 --password=postgres
```

**POSITIONAL ARGUMENTS**

: **`CLUSTER`**:
AlloyDB cluster ID

**REQUIRED FLAGS**

: **--password**:
Initial postgres user password to set up during cluster creation.

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**OPTIONAL FLAGS**

: **--allocated-ip-range-name**:
Name of the allocated IP range for the private IP AlloyDB cluster, for example:
"google-managed-services-default". If set, the instance IPs for this cluster
will be created in the allocated range. The range name must comply with RFC
1035. Specifically, the name must be 1-63 characters long and match the regular
expression [a-z]([-a-z0-9]`[a-z0-9])?.`

**--async``**:
Return immediately, without waiting for the operation in progress to complete.

**--database-version`=`DATABASE_VERSION``**:
Database version of the cluster. `DATABASE_VERSION` must
be one of: POSTGRES_14`,`POSTGRES_15`,`POSTGRES_16`.`

**--enable-private-service-connect``**:
Enable Private Service Connect (PSC) connectivity for the cluster.

**--network`=`NETWORK``**:
Network in the current project that the instance will be part of. To specify
using a network with a shared VPC, use the full URL of the network. For an
example host project, `testproject`, and shared network,
`testsharednetwork`, this would be of the
form:`--network=projects/testproject/global/networks/testsharednetwork`

**--subscription-type`=`SUBSCRIPTION_TYPE``**:
Subscription type of the cluster. `SUBSCRIPTION_TYPE` must
be one of: STANDARD`,`TRIAL`.`

**--tags`=[`KEY`=`VALUE`,…]`**:
List of tags KEY=VALUE pairs to bind. Each item must be expressed as
`<tag-key-namespaced-name>=<tag-value-short-name>`.
Example: `123/environment=production,123/costCenter=marketing`

**Continuous Backup configuration. If unspecified, continuous backups are enabled.

**--continuous-backup-recovery-window-days`=`RECOVERY_PERIOD``**:
Recovery window of the log files and backups saved to support Continuous
Backups.

**--enable-continuous-backup``**:
Enables Continuous Backups on the cluster.

**Key resource - The Cloud KMS (Key Management Service) cryptokey that will be
used to protect the continuous backup. The 'AlloyDB Service Agent's service
account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The
arguments in this group can be used to specify the attributes of this resource.

**--continuous-backup-encryption-key`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY``**:
ID of the key or fully qualified identifier for the key.
To set the `kms-key` attribute:

- provide the argument `--continuous-backup-encryption-key` on the
command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--continuous-backup-encryption-key-keyring`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_KEYRING``**:
The KMS keyring of the key.
To set the `kms-keyring` attribute:

- provide the argument `--continuous-backup-encryption-key` on the
command line with a fully specified name;
- provide the argument `--continuous-backup-encryption-key-keyring` on
the command line.

**--continuous-backup-encryption-key-location`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_LOCATION``**:
The Google Cloud location for the key.
To set the `kms-location` attribute:

- provide the argument `--continuous-backup-encryption-key` on the
command line with a fully specified name;
- provide the argument `--continuous-backup-encryption-key-location` on
the command line.

**--continuous-backup-encryption-key-project`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_PROJECT``**:
The Google Cloud project for the key.
To set the `kms-project` attribute:

- provide the argument `--continuous-backup-encryption-key` on the
command line with a fully specified name;
- provide the argument `--continuous-backup-encryption-key-project` on
the command line;
- set the property `core/project`.****

**Specify preferred day and time for maintenance deny period.

**--deny-maintenance-period-end-date`=`DENY_MAINTENANCE_PERIOD_END_DATE``**:
Date when the deny maintenance period ends, that is 2020-11-01 or 11-01 for
recurring.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--deny-maintenance-period-start-date`=`DENY_MAINTENANCE_PERIOD_START_DATE``**:
Date when the deny maintenance period begins, that is 2020-11-01 or 11-01 for
recurring.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--deny-maintenance-period-time`=`DENY_MAINTENANCE_PERIOD_TIME``**:
Time when the deny maintenance period starts and ends, for example 05:00, in UTC
time zone.
This flag argument must be specified if any of the other arguments in this group
are specified.**

**Automated backup policy. If unspecified, automated backups are disabled.
At most one of these can be specified:

**--disable-automated-backup``**:
Disables automated backups on the cluster.

**Enable automated backup policy.

**--automated-backup-days-of-week`=[`DAYS_OF_WEEK`,…]`**:
Comma-separated list of days of the week to perform a backup. At least one day
of the week must be provided. (e.g.,
--automated-backup-days-of-week=MONDAY,WEDNESDAY,SUNDAY).
`DAYS_OF_WEEK` must be one of: MONDAY`,`TUESDAY`,`WEDNESDAY`,`THURSDAY`,`FRIDAY`,`SATURDAY`,`SUNDAY`.
This flag argument must be specified if any of the other arguments in this group
are specified.`

**--automated-backup-start-times`=[`START_TIMES`,…]`**:
Comma-separated list of times during the day to start a backup. At least one
start time must be provided. The start times are assumed to be in UTC and
required to be an exact hour in the format HH:00. (e.g.,
`--automated-backup-start-times=01:00,13:00`)
This flag argument must be specified if any of the other arguments in this group
are specified.

**--automated-backup-window`=`TIMEOUT_PERIOD``**:
Length of the time window beginning at start time during which a backup can be
taken. If a backup does not succeed within this time window, it will be canceled
and considered failed. The backup window must be at least 5 minutes long. There
is no upper bound on the window. If not set, it will default to 1 hour.

**Key resource - The Cloud KMS (Key Management Service) cryptokey that will be
used to protect the automated backups. The 'AlloyDB Service Agent' service
account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The
arguments in this group can be used to specify the attributes of this resource.

**--automated-backup-encryption-key`=`AUTOMATED_BACKUP_ENCRYPTION_KEY``**:
ID of the key or fully qualified identifier for the key.
To set the `kms-key` attribute:

- provide the argument `--automated-backup-encryption-key` on the
command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--automated-backup-encryption-key-keyring`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_KEYRING``**:
The KMS keyring of the key.
To set the `kms-keyring` attribute:

- provide the argument `--automated-backup-encryption-key` on the
command line with a fully specified name;
- provide the argument `--automated-backup-encryption-key-keyring` on
the command line.

**--automated-backup-encryption-key-location`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_LOCATION``**:
The Google Cloud location for the key.
To set the `kms-location` attribute:

- provide the argument `--automated-backup-encryption-key` on the
command line with a fully specified name;
- provide the argument `--automated-backup-encryption-key-location` on
the command line.

**--automated-backup-encryption-key-project`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_PROJECT``**:
The Google Cloud project for the key.
To set the `kms-project` attribute:

- provide the argument `--automated-backup-encryption-key` on the
command line with a fully specified name;
- provide the argument `--automated-backup-encryption-key-project` on
the command line;
- set the property `core/project`.**

**Retention policy. If no retention policy is provided, all automated backups will
be retained.
At most one of these can be specified:

**--automated-backup-retention-count`=`RETENTION_COUNT``**:
Number of most recent successful backups retained.

**--automated-backup-retention-period`=`RETENTION_PERIOD``**:
Retention period of the backup relative to creation time. See `$ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for information on duration formats.******

**Key resource - The Cloud KMS (Key Management Service) cryptokey that will be
used to protect the cluster. The 'AlloyDB Service Agent' service account must
hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this
group can be used to specify the attributes of this resource.

**--kms-key`=`KMS_KEY``**:
ID of the key or fully qualified identifier for the key.
To set the `kms-key` attribute:

- provide the argument `--kms-key` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--kms-keyring`=`KMS_KEYRING``**:
The KMS keyring of the key.
To set the `kms-keyring` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-keyring` on the command line.

**--kms-location`=`KMS_LOCATION``**:
The Google Cloud location for the key.
To set the `kms-location` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-location` on the command line.

**--kms-project`=`KMS_PROJECT``**:
The Google Cloud project for the key.
To set the `kms-project` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-project` on the command line;
- set the property `core/project`.**

**Specify preferred day and time for maintenance.

**--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY``**:
Day of week for maintenance window, in UTC time zone.
`MAINTENANCE_WINDOW_DAY` must be one of:
MONDAY`,`TUESDAY`,`WEDNESDAY`,`THURSDAY`,`FRIDAY`,`SATURDAY`,`SUNDAY`.
This flag argument must be specified if any of the other arguments in this group
are specified.`

**--maintenance-window-hour`=`MAINTENANCE_WINDOW_HOUR``**:
Hour of day for maintenance window, in UTC time zone.
This flag argument must be specified if any of the other arguments in this group
are specified.**

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
gcloud alpha alloydb clusters create
```

```
gcloud beta alloydb clusters create
```