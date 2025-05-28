# gcloud redis instances reschedule-maintenance  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance)*

**NAME**

: **gcloud redis instances reschedule-maintenance - reschedule maintenance window for a Redis instance**

**SYNOPSIS**

: **`gcloud redis instances reschedule-maintenance` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance#--region)`=`REGION`) `[--reschedule-type](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance#--reschedule-type)`=`RESCHEDULE_TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance#--async)`] [`[--schedule-time](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance#--schedule-time)`=`SCHEDULE_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Reschedule maintenance window for a Redis instance.

**EXAMPLES**

: To reschedule maintenance window for an instance with the name
'my-redis-instance' in region 'us-central-1' with next available window, run:

```
gcloud redis instances reschedule-maintenance my-redis-instance --region=us-central1 --reschedule-type=next-available-window
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Cloud Memorystore for
Redis instance you want to reschedule maintenance window. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--reschedule-type**:
Reschedule type to use for the reschedule maintenance window. Reschedule Type
must be one of:IMMEDIATE, NEXT-AVAILABLE-WINDOW, or SPECIFIC-TIME.
`RESCHEDULE_TYPE` must be one of:

**`immediate`**:
Reschedule the maintenance window to perform now.

**`next-available-window`**:
Reschedule the maintenance window to the next available window.

**`specific-time`**:
Reschedule the maintenance window to a specific time.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--schedule-time**:
Time in RFC3339 format, for example: 2012-11-15T16:19:00.094Z

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
gcloud alpha redis instances reschedule-maintenance
```

```
gcloud beta redis instances reschedule-maintenance
```