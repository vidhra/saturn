# gcloud healthcare dicom-stores deidentify  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify)*

**NAME**

: **gcloud healthcare dicom-stores deidentify - de-identify data from the source store and write it to the destination store**

**SYNOPSIS**

: **`gcloud healthcare dicom-stores deidentify` (`[DICOM_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#DICOM_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#--location)`=`LOCATION`) `[--destination-store](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#--destination-store)`=`DESTINATION_STORE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#--async)`] [`[--dicom-filter-tags](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#--dicom-filter-tags)`=[`DICOM_FILTER_TAGS`,…]] [`[--text-redaction-mode](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#--text-redaction-mode)`=`TEXT_REDACTION_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: De-identify data from the source store and write it to the destination store.

**EXAMPLES**

: To generate a de-identified version of the DICOM store 'test-dicom-store', run
the command below.

```
gcloud healthcare dicom-stores deidentify test-dicom-store --destination-store=projects/{projectId}/locations/us-central1/datasets/{datasetId}/dicomStores/test-deid-dicom-store --dicom-filter-tags=MediaStorageSOPClassUID,SeriesInstanceUID,StudyInstanceUID
```

**POSITIONAL ARGUMENTS**

: **DicomStore resource - Source Cloud Healthcare API DICOM store to deidentify. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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

: **--destination-store**:
The name of the DICOM store to which the redacted data should be written (e.g.,
projects/{projectId}/locations/{locationId}/datasets/{datasetId}/dicomStores/{dicomStoreId}).
The destination DICOM store must already exist, or the request will fail.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--dicom-filter-tags**:
Tags to be filtered. Tags must be DICOM Data Elements, File Meta Elements, or
Directory Structuring Elements, as defined at:
http://dicom.nema.org/medical/dicom/current/output/html/part06.html#table_6-1,.
They may be provided by "Keyword" or "Tag". For example "PatientID",
"0010,0010".

**--text-redaction-mode**:
Determines how to redact text from image.
`TEXT_REDACTION_MODE` must be (only one value is
supported):

**`all`**:
Redact all text.

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
gcloud alpha healthcare dicom-stores deidentify
```

```
gcloud beta healthcare dicom-stores deidentify
```