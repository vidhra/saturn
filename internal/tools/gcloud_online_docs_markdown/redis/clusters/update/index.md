# gcloud redis clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update)*

**NAME**

: **gcloud redis clusters update - update Memorystore Cluster for Redis instance**

**SYNOPSIS**

: **`gcloud redis clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--region)`=`REGION`) [`[--aof-append-fsync](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--aof-append-fsync)`=`AOF_APPEND_FSYNC`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--async)`] [`[--automated-backup-mode](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--automated-backup-mode)`=`AUTOMATED_BACKUP_MODE`] [`[--automated-backup-start-time](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--automated-backup-start-time)`=`AUTOMATED_BACKUP_START_TIME`] [`[--automated-backup-ttl](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--automated-backup-ttl)`=`AUTOMATED_BACKUP_TTL`] [`[--deletion-protection](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--deletion-protection)`] [`[--node-type](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--node-type)`=`NODE_TYPE`] [`[--ondemand-maintenance](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--ondemand-maintenance)`] [`[--persistence-mode](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--persistence-mode)`=`PERSISTENCE_MODE`] [`[--rdb-snapshot-period](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--rdb-snapshot-period)`=`RDB_SNAPSHOT_PERIOD`] [`[--rdb-snapshot-start-time](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--rdb-snapshot-start-time)`=`RDB_SNAPSHOT_START_TIME`] [`[--remove-redis-config](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--remove-redis-config)`=[`KEY`,…]] [`[--replica-count](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--replica-count)`=`REPLICA_COUNT`] [`[--shard-count](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--shard-count)`=`SHARD_COUNT`] [`[--update-redis-config](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--update-redis-config)`=`KEY`=`VALUE`] [`[--maintenance-window-any](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--maintenance-window-any)`     | `[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the metadata and/or configuration parameters of a Redis cluster.
This command can fail for the following reasons:

- The cluster specified does not exist.
- The active account does not have permission to update the given cluster.

**EXAMPLES**

: To update a Redis cluster with 5 shard and 2 replica, run:

```
gcloud redis clusters update my-redis-cluster --shard-count=5 --replica-count=2
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Arguments and flags that specify the Memorystore Redis
cluster you want to update. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Redis region of the cluster. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**FLAGS**

: **--aof-append-fsync**:
Fsync configuration. `AOF_APPEND_FSYNC` must be one of:

**`always`**:
Redis explicitly calls fsync for every write command.

**`everysec`**:
(default) Redis explicitly calls fsync every second.

**`no`**:
Redis will not explicitly call fsync.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--automated-backup-mode**:
Automated backup mode. `AUTOMATED_BACKUP_MODE` must be one
of:

**`disabled`**:
(default) Automated backup is disabled.

**`enabled`**:
Automated backup is enabled.

**--automated-backup-start-time**:
One-hour window when you want automated-backup operations to start. Specify the
time in the format HH:00 on a 24-hour cycle in UTC time.

**--automated-backup-ttl**:
Time to live for automated backups. A backup will be deleted automatically after
the TTL is reached. It ranges from 1 day to 365 days. For example, "10d" for 10
days. If not specified, the default value is 35 days.

**--deletion-protection**:
Enable deletion protection for the Redis Cluster. Use
`--deletion-protection`/`--no-deletion-protection` to
enable/disable it.

**--node-type**:
Node Type of the redis cluster Node. `NODE_TYPE` must be
one of: `redis-highmem-medium`, `redis-highmem-xlarge`,
`redis-shared-core-nano`, `redis-standard-small`.

**--ondemand-maintenance**:
Trigger an on-demand maintenance.

**--persistence-mode**:
Operation mode for persistence. `PERSISTENCE_MODE` must be
one of:

**`aof`**:
AOF-based persistence

**`disabled`**:
Persistence mode is disabled

**`rdb`**:
RDB-based persistence

**--rdb-snapshot-period**:
Attempted period between RDB snapshots.
`RDB_SNAPSHOT_PERIOD` must be one of:

**`12h`**:
12 hours

**`1h`**:
1 hour

**`24h`**:
(default) 24 hours

**`6h`**:
6 hours

**--rdb-snapshot-start-time**:
Date and time of the first snapshot in the ISO 1801 format, and alignment time
for future snapshots. For example, 2024-01-01T01:00:00Z. If not specified, the
current time will be used.

**--remove-redis-config**:
A list of Redis Cluster config parameters to remove. Removing a non-existent
config parameter is silently ignored.

**--replica-count**:
The replica count of each shard.

**--shard-count**:
The shard count of the cluster.

**--update-redis-config**:
A list of Redis Cluster config KEY=VALUE pairs to update. If a config parameter
is already set, its value is modified; otherwise a new Redis config parameter is
added.

**--maintenance-window-any**

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

: This command uses the `redis/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/memorystore/docs/redis/](https://cloud.google.com/memorystore/docs/redis/)

**NOTES**

: These variants are also available:

```
gcloud alpha redis clusters update
```

```
gcloud beta redis clusters update
```