# gcloud firestore backups schedules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create)*

**NAME**

: **gcloud firestore backups schedules create - creates a Cloud Firestore backup schedule**

**SYNOPSIS**

: **`gcloud firestore backups schedules create` `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create#--database)`=`DATABASE` `[--retention](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create#--retention)`=`RETENTION` (`[--recurrence](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create#--recurrence)`=`RECURRENCE` : `[--day-of-week](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create#--day-of-week)`=`DAY_OF_WEEK`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a backup schedule with 7 days retention and daily recurrence under
database testdb.

```
gcloud firestore backups schedules create --database=testdb --retention=7d --recurrence=daily
```

To create a backup schedule with 7 days retention and weekly recurrence on
Monday under database testdb.

```
gcloud firestore backups schedules create --database=testdb --retention=7d --recurrence=weekly --day-of-week=MON
```

**REQUIRED FLAGS**

: **--database**:
The database to operate on.
For example, to operate on database `foo`:

```
gcloud firestore backups schedules create --database='foo'
```

**--retention**:
The rention of the backup. At what relative time in the future, compared to the
creation time of the backup should the backup be deleted, i.e. keep backups for
7 days.
For example, to set retention as 7 days.

```
gcloud firestore backups schedules create --retention=7d
```

**--recurrence**

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
gcloud alpha firestore backups schedules create
```

```
gcloud beta firestore backups schedules create
```