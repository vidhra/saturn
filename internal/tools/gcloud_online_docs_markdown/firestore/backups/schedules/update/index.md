# gcloud firestore backups schedules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/update](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/update)*

**NAME**

: **gcloud firestore backups schedules update - updates a Cloud Firestore backup schedule**

**SYNOPSIS**

: **`gcloud firestore backups schedules update` `[--backup-schedule](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/update#--backup-schedule)`=`BACKUP_SCHEDULE` `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/update#--database)`=`DATABASE` [`[--retention](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/update#--retention)`=`RETENTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update backup schedule 'cf9f748a-7980-4703-b1a1-d1ffff591db0' under database
testdb to 7 days retention.

```
gcloud firestore backups schedules update --database='testdb' --backup-schedule='cf9f748a-7980-4703-b1a1-d1ffff591db0' --retention='7d'
```

**REQUIRED FLAGS**

: **--backup-schedule**:
The backup schedule to operate on.
For example, to operate on backup schedule
`091a49a0-223f-4c98-8c69-a284abbdb26b`:

```
gcloud firestore backups schedules update --backup-schedule='091a49a0-223f-4c98-8c69-a284abbdb26b'
```

**--database**:
The database to operate on.
For example, to operate on database `foo`:

```
gcloud firestore backups schedules update --database='foo'
```

**OPTIONAL FLAGS**

: **--retention**:
The rention of the backup. At what relative time in the future, compared to the
creation time of the backup should the backup be deleted, i.e. keep backups for
7 days.
For example, to set retention as 7 days.

```
gcloud firestore backups schedules update --retention=7d
```

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
gcloud alpha firestore backups schedules update
```

```
gcloud beta firestore backups schedules update
```