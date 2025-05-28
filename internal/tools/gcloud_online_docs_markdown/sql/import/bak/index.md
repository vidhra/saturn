# gcloud sql import bak  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/import/bak](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak)*

**NAME**

: **gcloud sql import bak - import data into a Cloud SQL instance from a BAK file**

**SYNOPSIS**

: **`gcloud sql import bak` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#INSTANCE)` [`[URI](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#URI)`] `[--database](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--database)`=`DATABASE`, `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#DATABASE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--async)`] [`[--bak-type](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--bak-type)`=`BAK_TYPE`; default="FULL"] [`[--keep-encrypted](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--keep-encrypted)`] [`[--no-recovery](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--recovery)`] [`[--recovery-only](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--recovery-only)`] [`[--stop-at](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--stop-at)`=`STOP_AT`] [`[--stop-at-mark](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--stop-at-mark)`=`STOP_AT_MARK`] [`[--[no-]striped](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--[no-]striped)`] [`[--cert-path](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--cert-path)`=`CERT_PATH` `[--pvk-path](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--pvk-path)`=`PVK_PATH` (`[--prompt-for-pvk-password](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--prompt-for-pvk-password)` | `[--pvk-password](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#--pvk-password)`=`PVK_PASSWORD`)] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/import/bak#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud sql import bak imports data into a Cloud SQL instance from a BAK backup
file in Google Cloud Storage. You should use a full backup file with a single
backup set.
For detailed help on importing data into Cloud SQL, refer to this guide: [https://cloud.google.com/sql/docs/sqlserver/import-export/importing](https://cloud.google.com/sql/docs/sqlserver/import-export/importing)

**EXAMPLES**

: To import data from the BAK file `my-bucket/my-export.bak` into the
database `my-database` in the Cloud SQL instance
`my-instance`, run:

```
gcloud sql import bak my-instance gs://my-bucket/my-export.bak --database=my-database
```

To import data from the encrypted BAK file `my-bucket/my-export.bak`
into the database `my-database` in the Cloud SQL instance
`my-instance`, with the certificate
`gs://my-bucket/my-cert.crt`, private key
`gs://my-bucket/my-key.key` and prompting for the private key
password, run:

```
gcloud sql import bak my-instance gs://my-bucket/my-export.bak --database=my-database --cert-path=gs://my-bucket/my-cert.crt --pvk-path=gs://my-bucket/my-key.key --prompt-for-pvk-password
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**[`URI`]**:
Path to the BAK file file in Google Cloud Storage from which the import is made.
The URI is in the form `gs://bucketName/fileName`.

**REQUIRED FLAGS**

: **--database**:
A new database into which the import is made.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bak-type**:
Type of bak file that will be imported. Applicable to SQL Server only.
`BAK_TYPE` must be one of: `FULL`,
`DIFF`, `TLOG`.

**--keep-encrypted**:
Whether or not to decrypt the imported encrypted BAK file.

**--no-recovery**:
Whether or not the SQL Server import is execueted with NORECOVERY keyword.

**--recovery-only**:
Whether or not the SQL Server import skip download and bring database online.

**--stop-at**:
Equivalent to SQL Server STOPAT keyword. Used in transaction log import only.
Transaction log import stop at this timestamp. Format: YYYY-MM-DDTHH:MM:SS.

**--stop-at-mark**:
Equivalent to SQL Server STOPATMARK keyword. Used in transaction log import
only. Transaction log import stop at the given mark. To stop at given LSN, use
--stop-at-mark=lsn:xxx.

**--[no-]striped**:
Whether SQL Server import should be striped. Use `--striped` to
enable and `--no-striped` to disable.

**--cert-path**

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
gcloud alpha sql import bak
```

```
gcloud beta sql import bak
```