# gcloud spanner instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update)*

**NAME**

: **gcloud spanner instances update - update a Cloud Spanner instance**

**SYNOPSIS**

: **`gcloud spanner instances update` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--async)`] [`[--default-backup-schedule-type](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--default-backup-schedule-type)`=`DEFAULT_BACKUP_SCHEDULE_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--description)`=`DESCRIPTION`] [`[--edition](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--edition)`=`EDITION`] [`[--expire-behavior](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--expire-behavior)`=`EXPIRE_BEHAVIOR`] [`[--instance-type](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--instance-type)`=`INSTANCE_TYPE`] [`[--nodes](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--nodes)`=`NODES`     | `[--processing-units](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--processing-units)`=`PROCESSING_UNITS`     | `[--autoscaling-high-priority-cpu-target](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--autoscaling-high-priority-cpu-target)`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET` `[--autoscaling-storage-target](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--autoscaling-storage-target)`=`AUTOSCALING_STORAGE_TARGET` `[--asymmetric-autoscaling-option](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--asymmetric-autoscaling-option)`=[`high_priority_cpu_target`=`HIGH_PRIORITY_CPU_TARGET`],[`location`=`LOCATION`],[`max_nodes`=`MAX_NODES`],[`max_processing_units`=`MAX_PROCESSING_UNITS`],[`min_nodes`=`MIN_NODES`],[`min_processing_units`=`MIN_PROCESSING_UNITS`]     | `[--clear-asymmetric-autoscaling-option](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--clear-asymmetric-autoscaling-option)`=`LOCATION`,[`[LOCATION](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#LOCATION)`,…] `[--autoscaling-max-nodes](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--autoscaling-max-nodes)`=`AUTOSCALING_MAX_NODES` `[--autoscaling-min-nodes](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--autoscaling-min-nodes)`=`AUTOSCALING_MIN_NODES`     | `[--autoscaling-max-processing-units](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--autoscaling-max-processing-units)`=`AUTOSCALING_MAX_PROCESSING_UNITS` `[--autoscaling-min-processing-units](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#--autoscaling-min-processing-units)`=`AUTOSCALING_MIN_PROCESSING_UNITS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Spanner instance.

**EXAMPLES**

: To update the display name of a Cloud Spanner instance, run:

```
gcloud spanner instances update my-instance-id --description=my-new-display-name
```

To update the node count of a Cloud Spanner instance, run:

```
gcloud spanner instances update my-instance-id --nodes=1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud Spanner instance ID.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--default-backup-schedule-type**:
The default backup schedule type that is used in the instance.
`DEFAULT_BACKUP_SCHEDULE_TYPE` must be one of:

**`AUTOMATIC`**:
A default backup schedule is created automatically when a new database is
created in an instance. You can edit or delete the default backup schedule once
it's created. The default backup schedule creates a full backup every 24 hours.
These full backups are retained for 7 days.

**`DEFAULT_BACKUP_SCHEDULE_TYPE_UNSPECIFIED`**:
Not specified.

**`NONE`**:
No default backup schedule is created automatically when a new database is
created in an instance.

**--description**:
Description of the instance.

**--edition**:
Spanner edition. You can upgrade your Standard edition instance to the
`ENTERPRISE` edition or `ENTERPRISE_PLUS` edition. You can
also upgrade your Enterprise edition instance to the
`ENTERPRISE_PLUS` edition. You can downgrade your
`ENTERPRISE_PLUS` edition instance to the `ENTERPRISE` or
`STANDARD` edition. You can also downgrade your
`ENTERPRISE` edition instance to the `STANDARD` edition.
You must stop using the higher-tier edition features in order to downgrade.
Otherwise, downgrade fails. For more information, see [Spanner editions
overview](https://cloud.google.com/spanner/docs/editions-overview).

**--expire-behavior**:
The expire behavior of a free trial instance.
`EXPIRE_BEHAVIOR` must be one of:

**`free-to-provisioned`**:
When the free trial instance expires, upgrade the instance to a provisioned
instance.

**`remove-after-grace-period`**:
When the free trial instance expires, disable the instance, and delete it after
the grace period passes if it has not been upgraded to a provisioned instance.

**--instance-type**:
Specifies the type for this instance. `INSTANCE_TYPE` must
be one of:

**`free-instance`**:
Free trial instances provide no guarantees for dedicated resources, both
node_count and processing_units should be 0. They come with stricter usage
limits and limited support.

**`provisioned`**:
Provisioned instances have dedicated resources, standard usage limits, and
support.

**--nodes**

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
gcloud alpha spanner instances update
```

```
gcloud beta spanner instances update
```