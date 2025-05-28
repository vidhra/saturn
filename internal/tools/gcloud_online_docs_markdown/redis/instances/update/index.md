# gcloud redis instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/instances/update](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update)*

**NAME**

: **gcloud redis instances update - update Memorystore Redis instances**

**SYNOPSIS**

: **`gcloud redis instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--display-name)`=`DISPLAY_NAME`] [`[--enable-auth](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--enable-auth)`] [`[--maintenance-version](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--maintenance-version)`=`MAINTENANCE_VERSION`] [`[--persistence-mode](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--persistence-mode)`=`PERSISTENCE_MODE`] [`[--rdb-snapshot-period](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--rdb-snapshot-period)`=`RDB_SNAPSHOT_PERIOD`] [`[--rdb-snapshot-start-time](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--rdb-snapshot-start-time)`=`RDB_SNAPSHOT_START_TIME`] [`[--read-replicas-mode](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--read-replicas-mode)`=`READ_REPLICAS_MODE`] [`[--remove-redis-config](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--remove-redis-config)`=[`KEY`,…]] [`[--replica-count](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--replica-count)`=`REPLICA_COUNT`] [`[--secondary-ip-range](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--secondary-ip-range)`=`SECONDARY_IP_RANGE`] [`[--size](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--size)`=`SIZE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--update-redis-config](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--update-redis-config)`=`KEY`=`VALUE`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--remove-labels)`=[`KEY`,…]] [`[--maintenance-window-any](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--maintenance-window-any)`     | `[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the metadata and/or configuration parameters of a Redis instance.
This command can fail for the following reasons:

- The instance specified does not exist.
- The active account does not have permission to update the given instance.

**EXAMPLES**

: To update a Redis instance with the name `my-redis-instance` to have
the display name "Cache for Foo Service", and add the two labels,
`env` and `service`, run:

```
gcloud redis instances update my-redis-instance --display-name="Cache for Foo Service" --update-labels=env=test,service=foo
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Memorystore Redis
instance you want to update. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Redis region of the instance. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
A human-readable name for the instance.

**--enable-auth**:
Enables Redis AUTH for the instance.

**--maintenance-version**:
Specifies which maintenance version to apply to your instance during
self-service maintenance. To view the available maintenance versions for your
instance, run `gcloud redis instances describe [INSTANCE_ID]`.
Acceptable values for this flag are either `current_default` or one
of the specific versions listed by the describe command. If you pass the value
`current_default`, the Memorystore updates to the most recent
available maintenance version during self service maintenance.

**--persistence-mode**:
Operation mode for automated persistence.
`PERSISTENCE_MODE` must be one of:

**`disabled`**:
RDB mode is disabled

**`rdb`**:
Automatic RDB persistence

**--rdb-snapshot-period**:
The attempted period between RDB snapshots.
`RDB_SNAPSHOT_PERIOD` must be one of:

**`12h`**:
12 hours

**`1h`**:
1 hour

**`24h`**:
24 hours

**`6h`**:
6 hours

**--rdb-snapshot-start-time**:
Date and time of the first snapshot in the ISO 1801 format, and alignment time
for future snapshots. For example, 2022-11-02T03:00:00Z.

**--read-replicas-mode**:
Read replicas mode used by the instance. Only works against standard tier
instances with 5GB and above provisioned capacity and Redis version 5.0 and
above. This is an irreversible update i.e. Read replicas can not be disabled for
the instance once it is enabled. Also this update is exclusive and cannot be
clubbed with other update operations. `READ_REPLICAS_MODE`
must be one of:

**`read-replicas-disabled`**:
If read replica is not enabled on the instance, no changes are done. If read
replica is enabled for the instance, update operation fails

**`read-replicas-enabled`**:
Read replica is enabled for the instance if not already enabled. Read endpoint
will be provided and the instance can scale up and down the number of replicas.

**--remove-redis-config**:
A list of Redis config parameters to remove. Removing a non-existent config
parameter is silently ignored.

**--replica-count**:
The replica count of the instance. Valid from 0 to 5.

**--secondary-ip-range**:
Required only when read-replicas-mode is enabled on the instance. The CIDR range
of internal addresses that are reserved for this instance. For example,
10.0.0.0/28 or 192.168.0.0/28. Range must be unique and non-overlapping with
existing ranges in the network. If value 'auto' passed, the service will
automatically pick an available range.

**--size**:
The memory size of the instance in GiB.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--update-redis-config**:
A list of Redis config KEY=VALUE pairs to update according to [http://cloud.google.com/memorystore/docs/reference/redis-configs](http://cloud.google.com/memorystore/docs/reference/redis-configs).
If a config parameter is already set, its value is modified; otherwise a new
Redis config parameter is added. Currently, the only supported parameters are:
Redis version 3.2 and newer: maxmemory-policy, notify-keyspace-events, timeout.
Redis version 4.0 and newer: activedefrag, lfu-decay-time, lfu-log-factor,
maxmemory-gb.
Redis version 5.0 and newer: stream-node-max-bytes, stream-node-max-entries.
Redis version 7.0 and newer: maxmemory-clients, lazyfree-lazy-eviction,
lazyfree-lazy-expire, lazyfree-lazy-user-del, lazyfree-lazy-user-flush.

**--clear-labels**

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
gcloud alpha redis instances update
```

```
gcloud beta redis instances update
```