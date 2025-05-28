# gcloud spanner instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create)*

**NAME**

: **gcloud spanner instances create - create a Cloud Spanner instance**

**SYNOPSIS**

: **`gcloud spanner instances create` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#INSTANCE)` `[--config](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--config)`=`CONFIG` `[--description](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--description)`=`DESCRIPTION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--async)`] [`[--default-backup-schedule-type](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--default-backup-schedule-type)`=`DEFAULT_BACKUP_SCHEDULE_TYPE`] [`[--edition](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--edition)`=`EDITION`] [`[--expire-behavior](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--expire-behavior)`=`EXPIRE_BEHAVIOR`] [`[--instance-type](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--instance-type)`=`INSTANCE_TYPE`] [`[--nodes](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--nodes)`=`NODES`     | `[--processing-units](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--processing-units)`=`PROCESSING_UNITS`     | [`[--autoscaling-high-priority-cpu-target](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--autoscaling-high-priority-cpu-target)`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET` `[--autoscaling-storage-target](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--autoscaling-storage-target)`=`AUTOSCALING_STORAGE_TARGET` (`[--autoscaling-max-nodes](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--autoscaling-max-nodes)`=`AUTOSCALING_MAX_NODES` `[--autoscaling-min-nodes](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--autoscaling-min-nodes)`=`AUTOSCALING_MIN_NODES` | `[--autoscaling-max-processing-units](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--autoscaling-max-processing-units)`=`AUTOSCALING_MAX_PROCESSING_UNITS` `[--autoscaling-min-processing-units](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--autoscaling-min-processing-units)`=`AUTOSCALING_MIN_PROCESSING_UNITS`) : `[--asymmetric-autoscaling-option](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#--asymmetric-autoscaling-option)`=[`high_priority_cpu_target`=`HIGH_PRIORITY_CPU_TARGET`],[`location`=`LOCATION`],[`max_nodes`=`MAX_NODES`],[`max_processing_units`=`MAX_PROCESSING_UNITS`],[`min_nodes`=`MIN_NODES`],[`min_processing_units`=`MIN_PROCESSING_UNITS`]]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Spanner instance.

**EXAMPLES**

: To create a Cloud Spanner instance, run:

```
gcloud spanner instances create my-instance-id --config=regional-us-east1 --description=my-instance-display-name --nodes=3
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud Spanner instance ID.

**REQUIRED FLAGS**

: **--config**:
Instance configuration defines the geographic placement and replication of the
databases in that instance. Available configurations can be found by running
"gcloud spanner instance-configs list"

**--description**:
Description of the instance.

**OPTIONAL FLAGS**

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

**--edition**:
Spanner edition. `EDITION` must be one of:

**`EDITION_UNSPECIFIED`**:
Spanner's legacy pricing model. For more information, see the [Spanner editions
overview](https://cloud.google.com/spanner/docs/editions-overview)

**`ENTERPRISE`**:
Enterprise edition

**`ENTERPRISE_PLUS`**:
Enterprise Plus edition

**`STANDARD`**:
Standard edition

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
gcloud alpha spanner instances create
```

```
gcloud beta spanner instances create
```