# gcloud memcache instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create)*

**NAME**

: **gcloud memcache instances create - create a Memorystore Memcached instance**

**SYNOPSIS**

: **`gcloud memcache instances create` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--region)`=`REGION`) `[--node-count](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--node-count)`=`NODE_COUNT` `[--node-cpu](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--node-cpu)`=`NODE_CPU` `[--node-memory](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--node-memory)`=`NODE_MEMORY` [`[--async](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--async)`] [`[--authorized-network](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--authorized-network)`=`AUTHORIZED_NETWORK`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY`] [`[--maintenance-window-duration](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--maintenance-window-duration)`=`MAINTENANCE_WINDOW_DURATION`] [`[--maintenance-window-start-time](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--maintenance-window-start-time)`=`MAINTENANCE_WINDOW_START_TIME`] [`[--memcached-version](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--memcached-version)`=`MEMCACHED_VERSION`] [`[--parameters](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--parameters)`=`KEY`=`VALUE`] [`[--reserved-ip-range-id](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--reserved-ip-range-id)`=[`RESERVED_IP_RANGE_ID`,…]] [`[--zones](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#--zones)`=[`ZONES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Memorystore Memcached instance.
This command can fail for the following reasons:

- An instance with the same name already exists.
- The active account does not have the necessary permissions to create instances.

**EXAMPLES**

: To create a Memcached instance named 'my-memcache-instance' in region
'us-central1' with 3 nodes, each with 2 CPUs and 2GB of memory, run:

```
gcloud memcache instances create my-memcache-instance --region=us-central1 --node-count=3 --node-cpu=2 --node-memory=2GB
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Memcached instance to
create. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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
The name of the Memcached region of the instance. Overrides the default
memcache/region property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `memcache/region`.**

**REQUIRED FLAGS**

: **--node-count**:
Number of memcache nodes in this instance. Valid values range from 1 to 20.

**--node-cpu**:
Number of cpus per node in this instance. Valid values are 1 or even number
between 2-32. Value of 1 is not supported in all regions.

**--node-memory**:
Amount of memory allocated per node in this instance. The value must be a whole
number followed by a size unit of 'MB' for megabyte, or 'GB' for gigabyte, ie
'3072MB' or '9GB'. The value must be between 1024MB and 307200MB.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--authorized-network**:
Full name of the Google Compute Engine network to which the instance is
connected. If unspecified, the default network will be used.

**--display-name**:
An arbitrary and optional user provided name for the instance.

**--labels**:
List of label KEY=VALUE pairs to add.

**--maintenance-window-day**:
The day of week when the window starts, e.g. `sunday`.
`MAINTENANCE_WINDOW_DAY` must be one of:
`friday`, `monday`, `saturday`,
`sunday`, `thursday`, `tuesday`,
`wednesday`.

**--maintenance-window-duration**:
Duration in integer hours (`3` to `8`) of the maintenance
window.

**--maintenance-window-start-time**:
Hour of day (`0` to `23`) for the start of maintenance
window, in UTC time zone.

**--memcached-version**:
Optional major version of Memcached software to use with the instance. If not
provided, default of "1.5" will be used.
`MEMCACHED_VERSION` must be one of:

**`1.5`**:
Memcached major version 1.5

**`1.6.15`**:
Memcached version 1.6.15

**--parameters**:
User defined parameters to apply to the memcached process on each node. Possible
attributes include:

**`listen-backlog`**:
The backlog queue limit for the instance.

**`disable-flush-all`**:
If enabled, flush_all command will be disabled. Applicable to 1.4.24 and higher.

**`max-item-size`**:
Max bytes of the instnace. Must at least be equal to slab_chunk_max (which
defaults to 524288 bytes) and less than 134217728 bytes. Additionally it must be
a multiple of slab_chunk_max.

**`slab-min-size`**:
This is an integer in the range [1, 1024].

**`slab-growth-factor`**:
This is a float in the range [1.01, 100].

**`protocol`**:
This is an enum with acceptable values of ["ascii", "auto"].

**`disable-cas`**:
This is a boolean value.

**`disable-evictions`**:
This is a boolean value.

**`max-reqs-per-event`**:
This is an integer in the range [1, 1000].

**`track-sizes`**:
This is a boolean value.

**`worker-logbuf-size`**:
This is an integer in the range [48, 524288].

**`watcher-logbuf-size`**:
This is an integer in the range [0, 2097151].

**`lru-crawler`**:
This is a boolean value.

**`idle-timeout`**:
This is an integer in the range [1,86400].

**`lru-maintainer`**:
This is a boolean value.

**`maxconns-fast`**:
This is a boolean value.

**`hash-algorithm`**:
This is an enum with accepted values of ["jenkins", "murmur3"].

**--reserved-ip-range-id**:
Contains the name of allocated IP address ranges associated with the private
service access connection for example, "test-default" associated with IP range
10.0.0.0/29.

**--zones**:
List of zones for the memcache nodes. The nodes will be divided equally across
the given zones up to --node-count value. If not provided, the service will by
default create nodes in all zones in the region specified by --region flag.

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

: This command uses the `memcache/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memcache instances create
```

```
gcloud beta memcache instances create
```