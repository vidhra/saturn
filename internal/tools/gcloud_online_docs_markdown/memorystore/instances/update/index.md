# gcloud memorystore instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update)*

**NAME**

: **gcloud memorystore instances update - update the configuration of a Memorystore instance**

**SYNOPSIS**

: **`gcloud memorystore instances update` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--async)`] [`[--[no-]async-instance-endpoints-deletion-enabled](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--[no-]async-instance-endpoints-deletion-enabled)`] [`[--[no-]deletion-protection-enabled](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--[no-]deletion-protection-enabled)`] [`[--engine-version](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--engine-version)`=`ENGINE_VERSION`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--location)`=`LOCATION`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--mode)`=`MODE`] [`[--node-type](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--node-type)`=`NODE_TYPE`] [`[--[no-]ondemand-maintenance](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--[no-]ondemand-maintenance)`] [`[--replica-count](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--replica-count)`=`REPLICA_COUNT`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--request-id)`=`REQUEST_ID`] [`[--shard-count](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--shard-count)`=`SHARD_COUNT`] [`[--aof-config-append-fsync](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--aof-config-append-fsync)`=`AOF_CONFIG_APPEND_FSYNC` `[--clear-persistence-config](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-persistence-config)` `[--persistence-config-mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--persistence-config-mode)`=`PERSISTENCE_CONFIG_MODE` `[--rdb-config-snapshot-period](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--rdb-config-snapshot-period)`=`RDB_CONFIG_SNAPSHOT_PERIOD` `[--rdb-config-snapshot-start-time](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--rdb-config-snapshot-start-time)`=`RDB_CONFIG_SNAPSHOT_START_TIME`] [`[--automated-backup-config-mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--automated-backup-config-mode)`=`AUTOMATED_BACKUP_CONFIG_MODE` `[--automated-backup-config-retention](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--automated-backup-config-retention)`=`AUTOMATED_BACKUP_CONFIG_RETENTION` `[--clear-automated-backup-config](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-automated-backup-config)` `[--fixed-frequency-schedule-start-time-hours](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--fixed-frequency-schedule-start-time-hours)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_HOURS` `[--fixed-frequency-schedule-start-time-minutes](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--fixed-frequency-schedule-start-time-minutes)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_MINUTES` `[--fixed-frequency-schedule-start-time-nanos](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--fixed-frequency-schedule-start-time-nanos)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_NANOS` `[--fixed-frequency-schedule-start-time-seconds](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--fixed-frequency-schedule-start-time-seconds)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_SECONDS`] [`[--clear-cross-instance-replication-config](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-cross-instance-replication-config)` `[--cross-instance-replication-config-role](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--cross-instance-replication-config-role)`=`CROSS_INSTANCE_REPLICATION_CONFIG_ROLE` `[--clear-primary-instance](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-primary-instance)`     | `[--primary-instance](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--primary-instance)`=`PRIMARY_INSTANCE` `[--cross-instance-replication-config-secondary-instances](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--cross-instance-replication-config-secondary-instances)`=[`instance`=`INSTANCE`]     | `[--add-cross-instance-replication-config-secondary-instances](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--add-cross-instance-replication-config-secondary-instances)`=[`instance`=`INSTANCE`] `[--clear-cross-instance-replication-config-secondary-instances](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-cross-instance-replication-config-secondary-instances)`     | `[--remove-cross-instance-replication-config-secondary-instances](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--remove-cross-instance-replication-config-secondary-instances)`=[`instance`=`INSTANCE`]] [`[--clear-maintenance-policy](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-maintenance-policy)` `[--maintenance-policy-weekly-window](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--maintenance-policy-weekly-window)`=[`day`=`DAY`],[`startTime`=`STARTTIME`]     | `[--add-maintenance-policy-weekly-window](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--add-maintenance-policy-weekly-window)`=[`day`=`DAY`],[`startTime`=`STARTTIME`] `[--clear-maintenance-policy-weekly-window](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-maintenance-policy-weekly-window)`     | `[--remove-maintenance-policy-weekly-window](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--remove-maintenance-policy-weekly-window)`=[`day`=`DAY`],[`startTime`=`STARTTIME`]] [`[--endpoints](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--endpoints)`=[`connections`=`CONNECTIONS`]     | `[--add-endpoints](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--add-endpoints)`=[`connections`=`CONNECTIONS`] `[--clear-endpoints](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-endpoints)`     | `[--remove-endpoints](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--remove-endpoints)`=[`connections`=`CONNECTIONS`]] [`[--engine-configs](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--engine-configs)`=[`ENGINE_CONFIGS`,…]     | `[--update-engine-configs](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--update-engine-configs)`=[`UPDATE_ENGINE_CONFIGS`,…] `[--clear-engine-configs](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-engine-configs)`     | `[--remove-engine-configs](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--remove-engine-configs)`=[__REMOVE_ENGINE_CONFIGS,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the configuration of a Memorystore instance.

**EXAMPLES**

: To update Memorystore instance `my-instance` in project
`my-project` and location `us-central1` to six shards,
run:

```
gcloud memorystore instances update `my-instance` --project=my-project --location=us-central1 --shard-count=6
```

To update Memorystore instance `my-instance` in project
`my-project` and location `us-central1` to use a
maxmemory-policy of `allkeys-lru`, run:

```
gcloud memorystore instances update `my-instance` --project=my-project --location=us-central1 --update-engine-configs=maxmemory-policy=allkeys-lru
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Identifier. Unique name of the instance. Format:
projects/{project}/locations/{location}/instances/{instance} This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--[no-]async-instance-endpoints-deletion-enabled**

**--[no-]deletion-protection-enabled**

**--engine-version**:
Engine version of the instance.

**--location**:
For resources [instance], provides fallback value for resource location
attribute. When the resource's full URI path is not provided, location will
fallback to this flag value.

**--mode**:
The mode config for the instance. `MODE` must be one of:

**`cluster`**:
Instance is in cluster mode.

**`cluster-disabled`**:
Cluster mode is disabled for the instance.

**`standalone`**:
Deprecated: Use CLUSTER_DISABLED instead.

**--node-type**:
Machine type for individual nodes of the instance.
`NODE_TYPE` must be one of:

**`highmem-medium`**:
High memory medium.

**`highmem-xlarge`**:
High memory extra large.

**`shared-core-nano`**:
Shared core nano.

**`standard-small`**:
Standard small.

**--[no-]ondemand-maintenance**

**--replica-count**

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--shard-count**:
Number of shards for the instance.

**--aof-config-append-fsync**

**--automated-backup-config-mode**

**--clear-cross-instance-replication-config**

**--clear-maintenance-policy**

**--endpoints**

**--engine-configs**

**--labels**

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

: This command uses the `memorystore/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memorystore instances update
```

```
gcloud beta memorystore instances update
```