# gcloud sql reschedule-maintenance  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance](https://cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance)*

**NAME**

: **gcloud sql reschedule-maintenance - reschedule a Cloud SQL instance's maintenance**

**SYNOPSIS**

: **`gcloud sql reschedule-maintenance` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance#INSTANCE)` `[--reschedule-type](https://cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance#--reschedule-type)`=`RESCHEDULE_TYPE` [`[--schedule-time](https://cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance#--schedule-time)`=`SCHEDULE_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud sql reschedule-maintenance reschedules a Cloud SQL instance's
maintenance.

**EXAMPLES**

: To run maintenance on instance `my-instance` immediately, run:

```
gcloud sql reschedule-maintenance my-instance --reschedule-type=IMMEDIATE
```

To reschedule maintenance on instance `my-instance` to the next
available window, run:

```
gcloud sql reschedule-maintenance my-instance --reschedule-type=NEXT_AVAILABLE_WINDOW
```

To reschedule maintenance on instance `my-instance` to 2019-11-07 at
4:00 am UTC, run:

```
gcloud sql reschedule-maintenance my-instance --reschedule-type=SPECIFIC_TIME --schedule-time=2019-11-07T04:00Z
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**REQUIRED FLAGS**

: **--reschedule-type**:
The type of reschedule operation to perform.
`RESCHEDULE_TYPE` must be one of: `IMMEDIATE`,
`NEXT_AVAILABLE_WINDOW`, `SPECIFIC_TIME`.

**OPTIONAL FLAGS**

: **--schedule-time**:
When specifying SPECIFIC_TIME, the date and time at which to schedule the
maintenance in ISO 8601 format.

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
gcloud alpha sql reschedule-maintenance
```

```
gcloud beta sql reschedule-maintenance
```