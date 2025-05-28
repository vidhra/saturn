# gcloud spanner operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe](https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe)*

**NAME**

: **gcloud spanner operations describe - describe a Cloud Spanner operation**

**SYNOPSIS**

: **`gcloud spanner operations describe` `OPERATION-ID` (`[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe#--instance)`=`INSTANCE`     | `[--instance-config](https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe#--instance-config)`=`INSTANCE_CONFIG`) [`[--backup](https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe#--backup)`=`BACKUP`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe#--database)`=`DATABASE`] [`[--instance-partition](https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe#--instance-partition)`=`INSTANCE_PARTITION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Spanner operation.

**EXAMPLES**

: To describe a Cloud Spanner instance operation, run:

```
gcloud spanner operations describe _auto_12345 --instance=my-instance-id
```

To describe a Cloud Spanner database operation, run:

```
gcloud spanner operations describe _auto_12345 --instance=my-instance-id --database=my-database-id
```

To describe a Cloud Spanner backup operation, run:

```
gcloud spanner operations describe _auto_12345 --instance=my-instance-id --backup=my-backup-id
```

To describe an instance partition operation, run:

```
gcloud spanner operations describe _auto_12345 --instance=my-instance-id --instance-partition=my-partition-id
```

**POSITIONAL ARGUMENTS**

: **`OPERATION-ID`**:
ID of the operation

**REQUIRED FLAGS**

: **--instance**

**OPTIONAL FLAGS**

: **--backup**:
For a backup operation, the name of the backup the operation is executing on.

**--database**:
For a database operation, the name of the database the operation is executing
on.

**--instance-partition**:
For an instance partition operation, the name of the instance partition the
operation is executing on.

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
gcloud alpha spanner operations describe
```

```
gcloud beta spanner operations describe
```