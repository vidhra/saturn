# gcloud healthcare dicom-stores export gcs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs)*

**NAME**

: **gcloud healthcare dicom-stores export gcs - export a Cloud Healthcare API DICOM store to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud healthcare dicom-stores export gcs` (`[DICOM_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs#DICOM_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs#--location)`=`LOCATION`) `[--gcs-uri-prefix](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs#--gcs-uri-prefix)`=`GCS_URI_PREFIX` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs#--async)`] [`[--mime-type](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs#--mime-type)`=`MIME_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a Cloud Healthcare API DICOM store to Google Cloud Storage.

**EXAMPLES**

: To export the dicom-store 'test-dicom-store' to the existing bucket
'testGcsBucket' in the folder 'someFolder', with the mime-type
'application/dicom', run:

```
gcloud healthcare dicom-stores export gcs test-dicom-store --gcs-uri-prefix=gs://testGcsBucket/someFolder --mime-type=application/dicom --dataset=test-dataset
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

: **--gcs-uri-prefix**:
URI for a Google Cloud Storage directory to which result files should be written
(for example, `gs://bucket-id/path/to/destination/dir`). If there is
no trailing slash, the service will append one when composing the object path.
The user is responsible for creating the Google Cloud Storage bucket referenced
in `uri_prefix`.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--mime-type**:
'MIME types supported by DICOM spec. Each file will be written in the following
format:
`…/{study_id}/{series_id}/{instance_id}[/{frame_number}].{extension}`
The frame_number component will exist only for multi-frame instances. Refer to
the DICOM conformance statement for permissible MIME types: [https://cloud.google.com/healthcare/docs/dicom#wado-rs](https://cloud.google.com/healthcare/docs/dicom#wado-rs)
The following extensions will be used for output files:

- application/dicom -> .dcm
- image/jpeg -> .jpg
- image/png -> .png

If unspecified, the instances will be exported in their original DICOM format.'

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
gcloud alpha healthcare dicom-stores export gcs
```

```
gcloud beta healthcare dicom-stores export gcs
```