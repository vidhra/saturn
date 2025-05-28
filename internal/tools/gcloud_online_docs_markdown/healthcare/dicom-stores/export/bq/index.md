# gcloud healthcare dicom-stores export bq  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq)*

**NAME**

: **gcloud healthcare dicom-stores export bq - export a Cloud Healthcare API API DICOM store to BigQuery**

**SYNOPSIS**

: **`gcloud healthcare dicom-stores export bq` (`[DICOM_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#DICOM_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--location)`=`LOCATION`) `[--bq-table](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--bq-table)`=`BQ_TABLE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--async)`] [`[--overwrite-table](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--overwrite-table)`] [`[--write-disposition](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--write-disposition)`=`WRITE_DISPOSITION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a Cloud Healthcare API API DICOM store to BigQuery.

**EXAMPLES**

: To export the dicom-store ``test-dicom-store``
to the BigQuery table ``testtable`` in the
dataset ``testdataset``, overwriting any
existing table, run:

```
gcloud healthcare dicom-stores export bq test-dicom-store --bq-table=bq://my-project.testdataset.testtable --dataset=test-dataset --write-disposition=write-truncate
```

To export the dicom-store ``test-dicom-store``
to the BigQuery table ``testtable`` in the
dataset ``testdataset``, appending any existing
table, run:

```
gcloud healthcare dicom-stores export bq test-dicom-store --bq-table=bq://my-project.testdataset.testtable --dataset=test-dataset --write-disposition=write-append
```

**POSITIONAL ARGUMENTS**

: **DicomStore resource - Cloud Healthcare API DICOM store to export. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DICOM_STORE`**:
ID of the dicomStore or fully qualified identifier for the dicomStore.
To set the `dicom_store` attribute:

- provide the argument `dicom_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**REQUIRED FLAGS**

: **--bq-table**:
The BigQuery table where the DICOM store should be written. If this table does
not exist, a new table with the given name will be created.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--overwrite-table**:
If the destination table already exists and this flag is `TRUE`, the
table will be overwritten by the contents of the DICOM store. If the flag is not
set and the destination table already exists, the export call returns an error.

**--write-disposition**:
Determines whether the existing table in the destination is to be overwritten or
appended to. `WRITE_DISPOSITION` must be one of:

**`write-append`**:
Append data to the existing table.

**`write-empty`**:
Only export data if the destination table is empty.

**`write-truncate`**:
Erase all existing data in a table before writing the instances.

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

: This command uses the `healthcare/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/healthcare](https://cloud.google.com/healthcare)

**NOTES**

: These variants are also available:

```
gcloud alpha healthcare dicom-stores export bq
```

```
gcloud beta healthcare dicom-stores export bq
```