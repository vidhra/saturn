# gcloud memorystore instances reschedule-maintenance  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance)*

**NAME**

: **gcloud memorystore instances reschedule-maintenance - reschedule maintenance window for an instance**

**SYNOPSIS**

: **`gcloud memorystore instances reschedule-maintenance` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance#--location)`=`LOCATION`) `[--reschedule-type](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance#--reschedule-type)`=`RESCHEDULE_TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance#--async)`] [`[--schedule-time](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance#--schedule-time)`=`SCHEDULE_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Reschedule maintenance window for an instance.

**EXAMPLES**

: To reschedule maintenance window for an instance with the name
`my-instance` in region `us-central-1` with immediate,
run:

**POSITIONAL ARGUMENTS**

: **Instance resource - Name of the instance to reschedule maintenance for:
`projects/{project}/locations/{location_id}/instances/{instance}` The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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

**--location**:
The location id of the instance resource.
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--reschedule-type**:
If reschedule type is SPECIFIC_TIME, schedule_time must be set.
`RESCHEDULE_TYPE` must be one of:

**`immediate`**:
If the user wants to schedule the maintenance to happen now.

**`specific-time`**:
If the user wants to reschedule the maintenance to a specific time.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--schedule-time**:
Timestamp when the maintenance shall be rescheduled to if
reschedule_type=SPECIFIC_TIME, in RFC 3339 format. Example:
`2012-11-15T16:19:00.094Z`.

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
gcloud alpha memorystore instances reschedule-maintenance
```

```
gcloud beta memorystore instances reschedule-maintenance
```