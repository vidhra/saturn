# gcloud alpha alloydb clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update)*

**NAME**

: **gcloud alpha alloydb clusters update - update an AlloyDB cluster within a given project and region**

**SYNOPSIS**

: **`gcloud alpha alloydb clusters update` `[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#CLUSTER)` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--region)`=`REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--async)`] [`[--subscription-type](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--subscription-type)`=`SUBSCRIPTION_TYPE`] [`[--clear-automated-backup](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--clear-automated-backup)`     | `[--disable-automated-backup](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--disable-automated-backup)`     | `[--automated-backup-days-of-week](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-days-of-week)`=[`DAYS_OF_WEEK`,…] `[--automated-backup-start-times](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-start-times)`=[`START_TIMES`,…] `[--automated-backup-window](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-window)`=`TIMEOUT_PERIOD` [`[--automated-backup-encryption-key](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-encryption-key)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY` : `[--automated-backup-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-encryption-key-keyring)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_KEYRING` `[--automated-backup-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-encryption-key-location)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_LOCATION` `[--automated-backup-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-encryption-key-project)`=`AUTOMATED_BACKUP_ENCRYPTION_KEY_PROJECT`] `[--automated-backup-retention-count](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-retention-count)`=`RETENTION_COUNT`     | `[--automated-backup-retention-period](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--automated-backup-retention-period)`=`RETENTION_PERIOD`] [`[--continuous-backup-recovery-window-days](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--continuous-backup-recovery-window-days)`=`RECOVERY_PERIOD` `[--enable-continuous-backup](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--enable-continuous-backup)` `[--clear-continuous-backup-encryption-key](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--clear-continuous-backup-encryption-key)`     | [`[--continuous-backup-encryption-key](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--continuous-backup-encryption-key)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY` : `[--continuous-backup-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--continuous-backup-encryption-key-keyring)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_KEYRING` `[--continuous-backup-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--continuous-backup-encryption-key-location)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_LOCATION` `[--continuous-backup-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--continuous-backup-encryption-key-project)`=`CONTINUOUS_BACKUP_ENCRYPTION_KEY_PROJECT`]] [`[--maintenance-window-any](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--maintenance-window-any)`     | `[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--remove-deny-maintenance-period](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--remove-deny-maintenance-period)`     | `[--deny-maintenance-period-end-date](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--deny-maintenance-period-end-date)`=`DENY_MAINTENANCE_PERIOD_END_DATE` `[--deny-maintenance-period-start-date](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--deny-maintenance-period-start-date)`=`DENY_MAINTENANCE_PERIOD_START_DATE` `[--deny-maintenance-period-time](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#--deny-maintenance-period-time)`=`DENY_MAINTENANCE_PERIOD_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an AlloyDB cluster within a given project and
region.

**EXAMPLES**

: To update a cluster, run:

```
gcloud alpha alloydb clusters update my-cluster --region=us-central1 --automated-backup-start-times=12:00 --automated-backup-days-of-week=MONDAY --automated-backup-retention-count=10
```

**POSITIONAL ARGUMENTS**

: **`CLUSTER`**:
AlloyDB cluster ID

**REQUIRED FLAGS**

: **--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--subscription-type**:
Subscription type of the cluster. `SUBSCRIPTION_TYPE` must
be one of: `STANDARD`, `TRIAL`.

**--clear-automated-backup**

**--continuous-backup-recovery-window-days**

**--maintenance-window-any**

**--remove-deny-maintenance-period**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb clusters update
```

```
gcloud beta alloydb clusters update
```