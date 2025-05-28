# gcloud firestore backups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/backups/delete](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/delete)*

**NAME**

: **gcloud firestore backups delete - deletes a Cloud Firestore backup**

**SYNOPSIS**

: **`gcloud firestore backups delete` `[--backup](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/delete#--backup)`=`BACKUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/delete#--location)`=`LOCATION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/backups/delete#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To delete `cf9f748a-7980-4703-b1a1-d1ffff591db0` backup in us-east1.

```
gcloud firestore backups delete --location=us-east1 --backup=cf9f748a-7980-4703-b1a1-d1ffff591db0
```

**REQUIRED FLAGS**

: **--backup**:
The backup to operate on.
For example, to operate on backup
`cf9f748a-7980-4703-b1a1-d1ffff591db0`:

```
gcloud firestore backups delete --backup='cf9f748a-7980-4703-b1a1-d1ffff591db0'
```

**--location**:
The location to operate on. Available locations are listed at [https://cloud.google.com/firestore/docs/locations](https://cloud.google.com/firestore/docs/locations).
For example, to operate on location `us-east1`:

```
gcloud firestore backups delete --location='us-east1'
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
gcloud alpha firestore backups delete
```

```
gcloud beta firestore backups delete
```